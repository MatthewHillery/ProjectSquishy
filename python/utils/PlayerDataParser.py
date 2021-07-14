import requests

from bs4 import BeautifulSoup

from python.Constants import *
from python.model.CameraSettings import CameraSettings
from python.model.ControllerSettings import ControllerSettings
from python.model.DeadzoneSettings import DeadzoneSettings
from python.model.Player import Player


def parse():
    # Parsing data
    player_dict = {}
    set_default_player(player_dict)
    get_camera_settings(player_dict)
    get_deadzone_settings(player_dict)
    get_controller_settings(player_dict)

    # for key, value in player_dict.items():
    #     print(vars(value))
    player_dict.pop("Player")
    return player_dict


def get_controller_settings(player_dict):
    controller_page = requests.get(CONTROL_URL)
    soup = BeautifulSoup(controller_page.text, "lxml")
    controller_table = soup.find('table', class_='rl-responsive-table')
    controller_raw = controller_table.find_all('tr')
    for controller_player in controller_raw:
        data = controller_player.contents
        try:
            player = data[0].contents[1].text.strip()
            if player is None:
                continue
            controller = ControllerSettings(
                str(data[2].contents[0].attrs.get('alt')).upper(),
                str(data[3].contents[0].attrs.get('alt')).upper(),  # Can look at contents.len for airroll left or right
                str(data[4].contents[0].attrs.get('alt')).upper(),
                str(data[5].contents[0].attrs.get('alt')).upper(),
                str(data[6].contents[0].attrs.get('alt')).upper(),
                str(data[7].contents[0].attrs.get('alt')).upper(),
                str(data[8].contents[0].attrs.get('alt')).upper()
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

        deadzone = DeadzoneSettings(
            data[7],
            data[9],
            data[11],
            data[13],
            data[15],
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
        print(player)
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


def set_default_player(player_dict):
    player_dict.update({PLAYER_COMBO_BOX_DEFAULT:
                        Player(PLAYER_COMBO_BOX_DEFAULT, "N/A",
                               ControllerSettings(POWERSLIDE_DEFAULT_VALUE.upper(), AIR_ROLL_DEFAULT_VALUE.upper(), AIR_ROLL_LEFT_DEFAULT_VALUE.upper(), AIR_ROLL_RIGHT_DEFAULT_VALUE.upper(), BOOST_DEFAULT_VALUE.upper(), JUMP_DEFAULT_VALUE.upper(), BALL_CAM_DEFAULT_VALUE.upper(), BRAKE_DEFAULT_VALUE.upper(), THROTTLE_DEFAULT_VALUE.upper()),
                               CameraSettings(CAMERA_SHAKE_DEFAULT_VALUE, FOV_DEFAULT_VALUE, HEIGHT_DEFAULT_VALUE, ANGLE_DEFAULT_VALUE, DISTANCE_DEFAULT_VALUE, STIFFNESS_DEFAULT_VALUE, SWIVEL_SPEED_DEFAULT_VALUE, TRANSITION_SPEED_DEFAULT_VALUE, BALL_CAMERA_DEFAULT_VALUE, "N/A"),
                               DeadzoneSettings(DEADZONE_DEFAULT_VALUE, DODGE_DEADZONE_DEFAULT_VALUE, AERIAL_SENSITIVITY_DEFAULT_VALUE, STEERING_SENSITIVITY_DEFAULT_VALUE, "N/A"))})
