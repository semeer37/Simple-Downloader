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
  - `requests`
  - `aiohttp`
  - `asyncio`
  - `tqdm`
  - `typer`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/semeer37/Simple-Downloader.git
   cd Simple-Downloader
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

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Feel free to contribute to this project by submitting issues or pull requests.
