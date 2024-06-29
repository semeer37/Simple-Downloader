import os
import re
import logging
import requests
import aiohttp
import asyncio
from threading import Thread, Lock
from queue import Queue
from tqdm import tqdm
import typer
from typing import Optional

class Downloader:
    def __init__(self, url: str, file_name: Optional[str] = None, num_chunks: int = 4, max_retries: int = 5, chunk_size: Optional[int] = None):
        self.url = url
        self.file_name = file_name or self.extract_filename()
        self.num_chunks = num_chunks
        self.queue = Queue()
        self.lock = Lock()
        self.progress_bar = None
        self.chunk_size = chunk_size
        self.total_size = 0
        self.max_retries = max_retries

        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def extract_filename(self) -> str:
        """Extracts the filename from the URL or Content-Disposition header."""
        try:
            response = requests.head(self.url, allow_redirects=True)
            response.raise_for_status()
            
            content_disposition = response.headers.get('content-disposition')
            if content_disposition:
                filenames = re.findall('filename="(.+)"', content_disposition)
                if filenames:
                    return filenames[0]
            
            url_path = os.path.basename(response.url)
            if url_path and '.' in url_path:
                return url_path
        except requests.RequestException as e:
            logging.error(f"Error fetching file name from headers: {e}")
        
        return "downloaded_file"

    def get_file_size(self) -> int:
        """Fetches the size of the file to be downloaded."""
        try:
            response = requests.head(self.url, allow_redirects=True)
            response.raise_for_status()
            return int(response.headers.get('content-length', 0))
        except requests.RequestException as e:
            logging.error(f"Error fetching file size: {e}")
            return 0

    async def download_chunk(self, session: aiohttp.ClientSession, start: int, end: int, chunk_index: int, retries: int = 0):
        """Downloads a specific chunk of the file."""
        headers = {'Range': f'bytes={start}-{end}'}
        try:
            async with session.get(self.url, headers=headers) as response:
                response.raise_for_status()
                with open(f'{self.file_name}.part{chunk_index}', 'wb') as f:
                    async for chunk in response.content.iter_chunked(1024):
                        if chunk:
                            f.write(chunk)
                            with self.lock:
                                self.progress_bar.update(len(chunk))
            logging.info(f'Chunk {chunk_index} downloaded.')
        except aiohttp.ClientError as e:
            if retries < self.max_retries:
                delay = 2 ** retries
                logging.warning(f"Error downloading chunk {chunk_index}, retrying in {delay} seconds... ({retries + 1}/{self.max_retries})")
                await asyncio.sleep(delay)
                await self.download_chunk(session, start, end, chunk_index, retries + 1)
            else:
                logging.error(f"Failed to download chunk {chunk_index} after {self.max_retries} retries: {e}")

    async def fetch(self, start: int, end: int, chunk_index: int):
        """Initiates the download of a chunk."""
        async with aiohttp.ClientSession() as session:
            await self.download_chunk(session, start, end, chunk_index)

    def thread_worker(self):
        """Thread worker to download chunks."""
        while not self.queue.empty():
            start, end, chunk_index = self.queue.get()
            asyncio.run(self.fetch(start, end, chunk_index))
            self.queue.task_done()

    def merge_chunks(self):
        """Merges all the downloaded chunks into the final file."""
        try:
            with open(self.file_name, 'wb') as final_file:
                for i in range(self.num_chunks):
                    with open(f'{self.file_name}.part{i}', 'rb') as part_file:
                        final_file.write(part_file.read())
                    os.remove(f'{self.file_name}.part{i}')
            logging.info('Chunks merged successfully.')
        except IOError as e:
            logging.error(f"Error merging chunks: {e}")

    def cleanup(self):
        """Cleans up any partial download files."""
        for i in range(self.num_chunks):
            part_file = f'{self.file_name}.part{i}'
            if os.path.exists(part_file):
                os.remove(part_file)
                logging.info(f"Cleaned up partial file {part_file}")

    def download(self):
        """Manages the downloading process."""
        self.total_size = self.get_file_size()
        if self.total_size == 0:
            logging.error("Unable to determine file size.")
            return

        self.chunk_size = self.chunk_size or self.total_size // self.num_chunks

        for i in range(self.num_chunks):
            start = i * self.chunk_size
            end = start + self.chunk_size - 1 if i != self.num_chunks - 1 else self.total_size
            self.queue.put((start, end, i))

        self.progress_bar = tqdm(total=self.total_size, unit='B', unit_scale=True, desc=self.file_name)

        threads = []
        for _ in range(self.num_chunks):
            thread = Thread(target=self.thread_worker)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        self.progress_bar.close()

        if not self.queue.empty():
            logging.error('Download failed. Cleaning up partial files.')
            self.cleanup()
        else:
            self.merge_chunks()
            logging.info('Download completed!')

def human_readable_bytes(num: int, suffix: str = 'B') -> str:
    """Converts bytes to a human-readable format."""
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"

def main(url: str, file_name: Optional[str] = None, num_chunks: int = 4, max_retries: int = 5, chunk_size: Optional[int] = None):
    """Main function to initiate the downloader with provided arguments."""
    downloader = Downloader(url, file_name, num_chunks, max_retries, chunk_size)
    downloader.download()

if __name__ == "__main__":
    typer.run(main)
