🐍 # QR Scanner Downloader

This is a Kivy-based desktop application that scans QR codes using your webcam. If the QR code contains a URL pointing to a JSON file, the app fetches the JSON, downloads the image and video files specified in the JSON, and saves them locally.

## Features

- Scan QR codes using your webcam.
- Display scanned QR code data.
- If the QR code contains a URL to a JSON file, fetch and parse the JSON.
- Download image and video files specified in the JSON.
- Clickable hyperlink label for URLs.

## Requirements

- Python 3.x
- [Kivy](https://kivy.org/#download)
- [kivy_garden.zbarcam](https://github.com/kivy-garden/zbarcam)
- requests

## Installation

1. Install dependencies:

    ```sh
    pip install kivy kivy_garden.requests
    pip install kivy_garden.zbarcam
    ```

2. Save the [`QrScanner.py`](QrScanner.py) file in your project directory.

## Usage

Run the application:

```sh
python QrScanner.py
```

- Point your webcam at a QR code.
- If the QR code contains a URL to a JSON file with `image_url` and `video_url` fields, the files will be downloaded to the `downloads` folder.

## Example JSON Format

```json
{
    "image_url": "https://example.com/image.jpeg",
    "video_url": "https://example.com/video.mp4"
}
```

## License
