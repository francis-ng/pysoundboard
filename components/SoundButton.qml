import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import Qt.labs.platform

// https://stackoverflow.com/questions/55012315/how-to-access-qml-qtquick-controls-from-pyside
Item {
    property Component soundbuttoncomponent: soundbutton
    property variant handlercontext

    Component {
        id: soundbutton

        Item {
            FileDialog {
                id: filedialog
                title: qsTr("Select audio file")
                nameFilters: ["Audio files (*.wav *.mp3 *.ogg)"]
                onAccepted: handlercontext.browse(id, file)
            }

            GridLayout {
                width: 100
                height: 100
                columns: 2

                RoundButton {
                    id: control
                    // contentItem: Text {
                    //     text: control.text
                    //     font: control.font
                    //     opacity: enabled ? 1 : 0.3
                    //     color: control.down ? "#17a81a" : "#21be2b"
                    //     horizontalAlignment: Text.AlignHCenter
                    //     verticalAlignment: Text.AlignVCenter
                    //     elide: Text.ElideRight
                    // }
                    // background: Rectangle {
                    //     radius: 100
                    //     opacity: enabled ? 1 : 0.3
                    //     color: control.down ? "#d0d0d0" : "#e0e0e0"
                    // }
                    text: filename
                    Layout.row: 0
                    Layout.column: 0
                    Layout.rowSpan: 2
                    Layout.columnSpan: 2
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    onClicked: handlercontext.play(id)
                }

                // Slider {
                //     orientation: Qt.Vertical
                //     value: volume
                //     Layout.row: 0
                //     Layout.column: 2
                //     Layout.rowSpan: 2
                //     Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                //     onMoved: handlercontext.volumechange(id, value)
                // }

                Button {
                    text: qsTr("Browse")
                    Layout.row: 2
                    Layout.column: 0
                    Layout.columnSpan: 2
                    Layout.fillWidth: true
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    onClicked: filedialog.open()
                }
            }
        }
    }
}
