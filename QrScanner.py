from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
import webbrowser
import requests
import json
import os


KV = """
#:import ZBarCam kivy_garden.zbarcam.ZBarCam

BoxLayout:
    orientation: 'vertical'
    spacing: 10
    padding: 10

    ZBarCam:
        id: qrcodeCam
        on_symbols: app.update_label()

    HyperlinkLabel:
        id: result_label
        text: "Scan a QR code to display the result here."
        size_hint_y: None
        height: 50
        halign: 'center'
        valign: 'middle'
"""

class HyperlinkLabel(Label):
    """Custom label to behave like a hyperlink."""
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self.text.startswith("http") or self.text.startswith("www"):
                webbrowser.open(self.text)
        return super().on_touch_down(touch)

class QrCodeApp(App):
    def build(self):
        self.root = Builder.load_string(KV)
        return self.root

    def update_label(self):
        """Update the label with the scanned QR code data."""
        symbols = self.root.ids.qrcodeCam.symbols
        if symbols:
            qr_data = ' '.join([symbol.data.decode('utf-8') for symbol in symbols])
            self.root.ids.result_label.text = qr_data
            if qr_data.startswith("http"):
                self.fetch_and_save_files(qr_data)
        else:
            self.root.ids.result_label.text = "No QR Code detected."

    def fetch_and_save_files(self, url):
        """Fetch JSON data from the URL, and save image and video files."""
        try:
            response = requests.get(url)
            response.raise_for_status()

            # Parse JSON
            data = response.json()

            # Extract image and video URLs
            image_url = data.get("image_url")
            video_url = data.get("video_url")

            # Save files if URLs are available
            if image_url:
                self.download_file(image_url, "downloaded_image.jpeg")
            if video_url:
                self.download_file(video_url, "downloaded_video.mp4")

            print("Files downloaded successfully.")

        except requests.exceptions.RequestException as e:
            print(f"Error fetching the URL: {e}")
        except json.JSONDecodeError:
            print("Error: The content is not valid JSON.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    @staticmethod
    def download_file(file_url, file_name):
        """Download a file from a given URL and save it locally."""
        try:
            response = requests.get(file_url, stream=True)
            response.raise_for_status()

            # Create a directory for downloads if it doesn't exist
            os.makedirs("downloads", exist_ok=True)
            file_path = os.path.join("downloads", file_name)

            # Save file content
            with open(file_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

            print(f"Saved {file_name} to 'downloads' directory.")
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {file_url}: {e}")

if __name__ == '__main__':
    QrCodeApp().run()