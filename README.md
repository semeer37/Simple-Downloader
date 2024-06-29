# Simple-Downloader

This project is a multi-threaded file downloader written in Python. It supports downloading large files by splitting them into chunks, downloading the chunks concurrently, and then merging them into a single file. The downloader also handles retries for failed downloads and provides a progress bar to track the download status.

## Features

- Multi-threaded download
- Downloads files in chunks for faster performance
- Retries failed downloads up to a specified number of attempts
- Displays a progress bar to track the download status
- Merges downloaded chunks into a single file
- Cleans up partial downloads in case of failure

## Requirements

- Python 3.7+
- Required Python libraries:
  - `os`
  - `re`
  - `logging`
  - `requests`
  - `aiohttp`
  - `asyncio`
  - `threading`
  - `queue`
  - `tqdm`
  - `typer`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/semeer37/downloader.git
   cd downloader
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the downloader, run the script with the necessary arguments:

```bash
python downloader.py <URL> [OPTIONS]
```

### Arguments

- `URL`: The URL of the file to download.

### Options

- `--file-name TEXT`: The name of the output file. If not provided, the filename is extracted from the URL.
- `--num-chunks INTEGER`: The number of chunks to split the file into for downloading. Default is 4.
- `--max-retries INTEGER`: The maximum number of retry attempts for a failed download. Default is 5.
- `--chunk-size INTEGER`: The size of each chunk in bytes. If not provided, the chunk size is calculated based on the total file size and the number of chunks.

### Example

```bash
python downloader.py https://example.com/largefile.zip --file-name myfile.zip --num-chunks 8 --max-retries 3
```

## Functions

### `Downloader`

A class that manages the downloading process.

#### `__init__(self, url: str, file_name: Optional[str] = None, num_chunks: int = 4, max_retries: int = 5, chunk_size: Optional[int] = None)`

Initializes the downloader with the specified parameters.

#### `extract_filename(self) -> str`

Extracts the filename from the URL or Content-Disposition header.

#### `get_file_size(self) -> int`

Fetches the size of the file to be downloaded.

#### `download_chunk(self, session: aiohttp.ClientSession, start: int, end: int, chunk_index: int, retries: int = 0)`

Downloads a specific chunk of the file.

#### `fetch(self, start: int, end: int, chunk_index: int)`

Initiates the download of a chunk.

#### `thread_worker(self)`

Thread worker to download chunks.

#### `merge_chunks(self)`

Merges all the downloaded chunks into the final file.

#### `cleanup(self)`

Cleans up any partial download files.

#### `download(self)`

Manages the downloading process.

### `human_readable_bytes(num: int, suffix: str = 'B') -> str`

Converts bytes to a human-readable format.

### `main(url: str, file_name: Optional[str] = None, num_chunks: int = 4, max_retries: int = 5, chunk_size: Optional[int] = None)`

Main function to initiate the downloader with provided arguments.

## Logging

The script uses Python's built-in `logging` module to log messages. The log level is set to `INFO`, and the format includes the timestamp, log level, and message.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Feel free to contribute to this project by submitting issues or pull requests.
