

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 6.3
import QtQuick.Controls 6.3
import Home

Rectangle {
    width: Constants.width
    height: Constants.height

    color: Constants.backgroundColor
    property alias labelWidth: label.width

    Row {
        id: row
        x: 0
        y: 0
        width: 200
        height: 400

        Row {
            id: row2
            width: 300
            height: 150
            padding: 10
            rightPadding: 20
            leftPadding: 20

            Image {
                id: image
                width: 100
                height: 100
                anchors.left: parent.left
                source: "qrc:/qtquickplugin/images/template_image.png"
                anchors.leftMargin: 10
                fillMode: Image.PreserveAspectFit
            }

            Label {
                id: label
                property string name: "This is a string"
                width: 150
                text: qsTr("Azlan Chenlong Bin Mohammad Noh")
                anchors.verticalCenter: image.verticalCenter
                anchors.left: image.right
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                wrapMode: Text.WordWrap
                textFormat: Text.PlainText
                font.pointSize: 14
                anchors.verticalCenterOffset: 0
                anchors.leftMargin: 10
            }
        }
        Column {
            id: column
            width: 200
            height: 400

            Label {
                id: label1
                text: qsTr("Points:")
                horizontalAlignment: Text.AlignHCenter
                anchors.horizontalCenter: parent.horizontalCenter
                font.bold: true
                font.pointSize: 21
            }

            App {
                id: app
            }

            NumberAnimation {
                id: numberAnimation
                paused: false
                running: true
                to: 7349
                from: 0
            }


        }

        Row {
            id: row1
            width: 200
            height: 400

            ComboBox {
                id: comboBox
                height: 100
                clip: false
            }

            ComboBox {
                id: comboBox1
                height: 100
            }

            ComboBox {
                id: comboBox2
                height: 100
            }

            ComboBox {
                id: comboBox3
                height: 100
            }

            ComboBox {
                id: comboBox4
                height: 100
            }
        }
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.5}
}
##^##*/

