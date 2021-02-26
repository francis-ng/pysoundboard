import sys
import os
import sounddevice as sd
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from models import SoundBoard


def get_devices():
    all_devices = sd.query_devices()
    mme_devices = []
    mme_id = -1
    for idx, device in enumerate(sd.query_hostapis()):
        if "MME" in device["name"]:
            mme_id = idx
            break
    for device in all_devices:
        if device["hostapi"] == mme_id and device["max_output_channels"] > 0:
            mme_devices.append(device["name"])
    return mme_devices


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    sounddevices = get_devices()
    model = SoundBoard.SoundBoard(sounddevices)

    engine.rootContext().setContextProperty("soundbuttons", model.soundbuttons)
    engine.rootContext().setContextProperty("sounddevices", sounddevices)
    engine.rootContext().setContextProperty("logicmodel", model)

    qml_file = os.path.join(os.path.dirname(__file__), "app.qml")
    engine.load(QUrl.fromLocalFile(os.path.abspath(qml_file)))

    app.aboutToQuit.connect(model.handle_close)

    app.exec_()
