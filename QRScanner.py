from kivy.app import App
from kivy.lang import Builder


class QrCodeApp(App):
    def build(self):
        return Builder.load_string(
            """
#:import ZBarCam kivy_garden.zbarcam.ZBarCam

BoxLayout:
    orientation: 'vertical'
    ZBarCam:
        id: qrcodeCam
    Label:
        size_hint: None, None
        size: self.texture_size[0], 50
        text: ' '.join([str(symbol) for symbol in qrcodeCam.symbols])
"""
        )


if __name__ == '__main__':
    QrCodeApp().run()
