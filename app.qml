import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import "components"

ApplicationWindow {
    title: "SoundBoard"
    visible: true
    width: 800
    height: 600

    header: ToolBar {
        RowLayout {
            anchors.fill: parent
            ComboBox {
                model: sounddevices
                currentIndex: logicmodel.selected_device
                onActivated: logicmodel.sounddevice_changed(currentIndex)
            }
            Label {
                text: qsTr("Sounds")
                elide: Label.ElideRight
                horizontalAlignment: Qt.AlignHCenter
                verticalAlignment: Qt.AlignVCenter
                Layout.fillWidth: true
            }
            RowLayout {
                ToolButton {
                    text: qsTr("-")
                    onClicked: logicmodel.remove()
                }
                ToolButton {
                    text: qsTr("+")
                    onClicked: logicmodel.add()
                }
            }
        }
    }

    GridView {
        anchors.fill: parent
        anchors.margins: 5
        cellHeight: 120
        cellWidth: 120
        model: soundbuttons
        delegate: soundbutton.soundbuttoncomponent

        SoundButton {
            id: soundbutton
            handlercontext: logicmodel
        }
    }
}
