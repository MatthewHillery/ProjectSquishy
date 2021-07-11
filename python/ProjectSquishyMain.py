import requests
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout

from bs4 import BeautifulSoup

from python.Constants import *
from python.model.CameraSettings import CameraSettings
from python.model.ControllerSettings import ControllerSettings
from python.model.DeadzoneSettings import DeadzoneSettings
from python.model.Player import Player
from python.widgets.ComboBox import ComboBox
from python.widgets.Label import Label
from python.widgets.TextBox import TextBox


def main():
    # Parsing data
    player_dict = {}
    get_camera_settings(player_dict)
    get_deadzone_settings(player_dict)
    get_controller_settings(player_dict)

    for key, value in player_dict.items():
        print(vars(value))

    #  UI set up
    app = QApplication(sys.argv)
    main_widget = QWidget()
    main_widget.setGeometry(100, 100, 200, 50)
    main_widget.setFixedSize(600, 900)
    main_widget.setWindowTitle("Project Squishy")

    main_layout = QVBoxLayout()

    camera_layout = QVBoxLayout()
    deadzone_layout = QVBoxLayout()
    controller_layout = QVBoxLayout()
    player_layout = QVBoxLayout()

    top_layout = QHBoxLayout()
    bottom_layout = QHBoxLayout()

    player_list = ComboBox()
    player_list.addItems(player_dict.keys())

    player_layout.addWidget(player_list)
    top_layout.addLayout(player_layout)

    for cons in CAMERA_CONSTANTS:
        top_layout.addLayout(create_layout(cons, camera_layout))

    for cons in CONTROLLER_CONSTANTS:
        bottom_layout.addLayout(create_layout(cons, controller_layout))

    for cons in DEADZONE_CONSTANTS:
        bottom_layout.addLayout(create_layout(cons, deadzone_layout))

    main_layout.addLayout(top_layout)
    main_layout.addLayout(bottom_layout)
    main_widget.setLayout(main_layout)
    main_widget.show()
    sys.exit(app.exec_())


def fill_fields(player):
    print(player.currentText())


def create_layout(cons, setting_layout):
    layout = QHBoxLayout()
    layout.setObjectName(cons.get(ID))
    l = Label()
    t = TextBox()
    l.setText(cons.get(LABEL))
    layout.addWidget(l)
    layout.addWidget(t)
    setting_layout.addLayout(layout)
    return setting_layout


def get_controller_settings(player_dict):
    controller_page = requests.get(CONTROL_URL)
    soup = BeautifulSoup(controller_page.text, "lxml")
    controller_table = soup.find('table', class_='rl-responsive-table')
    controller_raw = controller_table.find_all('tr')
    for controller_player in controller_raw:
        data = controller_player.contents
        try:
            player = data[0].contents[1].text.strip()
            if player == "SquishyMuffinz":
                i = 0
            if player is None:
                continue
            controller = ControllerSettings(
                data[2].contents[0].attrs.get('alt'),
                data[3].contents[0].attrs.get('alt'),  # Can look at contents.len for airroll left or right
                data[4].contents[0].attrs.get('alt'),
                data[5].contents[0].attrs.get('alt'),
                data[6].contents[0].attrs.get('alt'),
                data[7].contents[0].attrs.get('alt'),
                data[8].contents[0].attrs.get('alt')
            )

            if player not in player_dict:
                p = Player(player, data[1].contents[0].strip().text, controller, None, None)
                player_dict.update({player: p})
            else:
                player_ob = player_dict.get(player)
                player_ob.controller_settings = controller
                player_dict.update({player: player_ob})
        except:
            pass

    print(len(player_dict))


def get_deadzone_settings(player_dict):
    deadzone_page = requests.get(DEADZONE_URL)
    soup = BeautifulSoup(deadzone_page.text, "lxml")
    deadzone_table = soup.find('table', class_='sortable rl-responsive-table-sortable')
    deadzone_raw = deadzone_table.find_all('tr')
    for deadzone_player in deadzone_raw:
        data = deadzone_player.text.split('\n')
        player = str(data[1]).split(' ')[0].strip()
        if player == "SquishyMuffinz":
            i = 0

        deadzone = DeadzoneSettings(
            data[3],
            data[5],
            data[7],
            data[9],
            data[11],
            data[13]
        )
        if player not in player_dict:
            p = Player(player, data[3], None, None, deadzone)
            player_dict.update({player: p})
        else:
            player_ob = player_dict.get(player)
            player_ob.deadzone_settings = deadzone
            player_dict.update({player: player_ob})
    print(len(player_dict))


def get_camera_settings(player_dict):
    camera_page = requests.get(CAMERA_URL)
    soup = BeautifulSoup(camera_page.text, "lxml")
    camera_table = soup.find('table', class_='sortable rl-responsive-table-sortable')
    camera_raw = camera_table.find_all('tr')
    for camera_player in camera_raw:
        data = camera_player.text.split('\n')
        player = data[1].strip()
        cam = CameraSettings(
            data[5],
            data[7],
            data[9],
            data[11],
            data[13],
            data[15],
            data[17],
            data[19],
            data[21],
            data[23]
        )
        if player not in player_dict:
            p = Player(player, data[3].strip(), None, cam, None)
            player_dict.update({player: p})
        else:
            player_ob = player_dict.get(player)
            player_ob.camera_settings = cam
            player_dict.update({player: player_ob})

    print(len(player_dict))


if __name__ == '__main__':
    main()
