import os
import json
import soundfile as sf
import sounddevice as sd
from PySide6.QtCore import QObject, QUrl, Slot
from models import SoundButtonListModel


# https://www.programmersought.com/article/32025290109/
# https://stackoverflow.com/questions/34180748/qml-how-to-access-element-from-another-qml
class SoundBoard(QObject):
    selected_device = 1
    audiofile_cache = []
    soundbuttons = SoundButtonListModel.SoundButtonListModel()

    def __init__(self, devices):
        super().__init__()
        self.sounddevices = devices
        if os.path.exists('data.json'):
            with open('data.json', 'r') as f:
                self.soundbuttons.items = json.load(f)
                self.soundbuttons.layoutChanged.emit()
                self.loadsounds()

    def loadsounds(self):
        for sound in self.soundbuttons.items:
            self.audiofile_cache.append(sf.read(sound["filepath"]))

    @Slot()
    def handle_close(self):
        with open('data.json', 'w') as f:
            json.dump(self.soundbuttons.items, f)
        print("Closing")

    @Slot(int)
    def sounddevice_changed(self, index):
        sd.default.device = self.sounddevices[index]

    @Slot()
    def add(self):
        self.audiofile_cache.append({})
        self.soundbuttons.items.append({"id": len(self.soundbuttons.items),
                                        "filename": "",
                                        "volume": 1.0,
                                        "filepath": ""})
        self.soundbuttons.layoutChanged.emit()

    @Slot()
    def remove(self):
        self.audiofile_cache.pop()
        self.soundbuttons.items.pop()
        self.soundbuttons.layoutChanged.emit()

    @Slot(int, float)
    def volumechange(self, id, vol):
        self.soundbuttons.setData(id,
                                  vol,
                                  self.soundbuttons.VOLUME)

    @Slot(int, QUrl)
    def browse(self, id, file):
        filepath = file.toLocalFile()

        self.soundbuttons.setData(id,
                                  os.path.splitext(os.path.basename(filepath))[0],
                                  self.soundbuttons.FILENAME)
        self.soundbuttons.setData(id,
                                  filepath,
                                  self.soundbuttons.FILEPATH)
        self.audiofile_cache[id] = sf.read(filepath)

    @Slot(int)
    def play(self, id):
        data, fs = self.audiofile_cache[id]
        sd.play(data, fs)
