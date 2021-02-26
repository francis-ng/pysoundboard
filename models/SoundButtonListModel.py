from PySide6.QtCore import Qt, QModelIndex, QAbstractListModel


# https://www.programmersought.com/article/34085269941/
class SoundButtonListModel(QAbstractListModel):
    items = []
    ID = Qt.UserRole + 0
    FILENAME = Qt.UserRole + 1
    VOLUME = Qt.UserRole + 2
    FILEPATH = Qt.UserRole + 3

    def __init__(self, items=None):
        super().__init__()
        if items:
            self.items = items

    def rowCount(self, parent=None) -> int:
        return len(self.items)

    def setData(self, index, value, role):
        qindex = self.createIndex(index, 0)
        if role == self.ID:
            self.items[index]["id"] = value
            self.dataChanged.emit(qindex, qindex)
            return True
        if role == self.FILENAME:
            self.items[index]["filename"] = value
            self.dataChanged.emit(qindex, qindex)
            return True
        if role == self.VOLUME:
            self.items[index]["volume"] = value
            self.dataChanged.emit(qindex, qindex)
            return True
        if role == self.FILEPATH:
            self.items[index]["filepath"] = value
            self.dataChanged.emit(qindex, qindex)
            return True
        return False

    def data(self, index: QModelIndex, role: int = None):
        index = index.row()
        item = self.items[index]
        if role == self.ID:
            return item["id"]
        elif role == self.FILENAME:
            return item["filename"]
        elif role == self.VOLUME:
            return item["volume"]
        elif role == self.FILEPATH:
            return item["filepath"]

    def roleNames(self):
        return {
            self.ID: b'id',
            self.FILENAME: b'filename',
            self.VOLUME: b'volume',
            self.FILEPATH: b'filepath'
        }
