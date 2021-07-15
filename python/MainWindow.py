from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtCore import QSize
from PyQt5.QtCore import QRect
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QMetaObject
from PyQt5.QtCore import QCoreApplication

from python.Constants import *
from python.utils import PlayerDataParser
from python.widgets.Button import Button
from python.widgets.CheckBox import Checkbox
from python.widgets.ComboBox import ComboBox
from python.widgets.DonateButton import DonateButton
from python.widgets.DoubleSpinBox import DoubleSpinBox
from python.widgets.Label import Label
from python.widgets.PlayerComboBox import PlayerComboBox
from python.widgets.SpinBox import SpinBox
from python.widgets.TextBox import TextBox


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Get player data
        self.player_dict = PlayerDataParser.parse()

        # UI Main Frame
        self.setObjectName(APPLICATION_NAME)
        self.resize(610, 680)
        self.setMinimumSize(QSize(610, 680))
        self.setMaximumSize(QSize(610, 680))
        self.setAutoFillBackground(False)
        self.setStyleSheet("")
        self.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        self.setTabShape(QTabWidget.Rounded)
        self.central_widget = QWidget(self)
        self.central_widget.setAutoFillBackground(True)
        self.central_widget.setStyleSheet("")
        self.central_widget.setObjectName("centralwidget")
        self.frame = QFrame(self.central_widget)
        self.frame.setGeometry(QRect(0, -1, 610, 680))
        self.frame.setStyleSheet(MAIN_WINDOW_STYLE_SHEET)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")

        # UI Player Frame - set up
        self.player_frame = QFrame(self.frame)
        self.player_frame.setGeometry(QRect(10, 11, 291, 151))
        self.player_frame.setAutoFillBackground(False)
        self.player_frame.setStyleSheet("")
        self.player_frame.setFrameShape(QFrame.Panel)
        self.player_frame.setFrameShadow(QFrame.Raised)
        self.player_frame.setObjectName(PLAYER_FRAME_ID)

        # UI Player Frame - labels & data widgets
        self.player_combo_box = PlayerComboBox(self.player_frame)
        self.player_combo_box.activated.connect(self.fill_fields)
        self.team_text_box = TextBox(self.player_frame, TEAM_TEXT_BOX_ID, QRect(160, 80, 115, 30))
        self.team_label = Label(self.player_frame, TEAM_LABEL_ID, QRect(20, 80, 130, 30))

        # UI Controller Frame - set up
        self.controller_frame = QFrame(self.frame)
        self.controller_frame.setGeometry(QRect(310, 230, 291, 371))
        self.controller_frame.setAutoFillBackground(False)
        self.controller_frame.setFrameShape(QFrame.Panel)
        self.controller_frame.setFrameShadow(QFrame.Raised)
        self.controller_frame.setObjectName(CONTROLLER_FRAME_ID)

        # UI Controller Frame - labels
        self.powerslide_label = Label(self.controller_frame, POWERSLIDE_LABEL_ID, QRect(20, 10, 130, 30))
        self.air_roll_label = Label(self.controller_frame, AIR_ROLL_LABEL_ID, QRect(20, 50, 130, 30))
        self.air_roll_left_label = Label(self.controller_frame, AIR_ROLL_LEFT_LABEL_ID, QRect(20, 90, 130, 30))
        self.air_roll_right_label = Label(self.controller_frame, AIR_ROLL_RIGHT_LABEL_ID, QRect(20, 130, 130, 30))
        self.boost_label = Label(self.controller_frame, BOOST_LABEL_ID, QRect(20, 170, 130, 30))
        self.jump_label = Label(self.controller_frame, JUMP_LABEL_ID, QRect(20, 210, 130, 30))
        self.ball_cam_label = Label(self.controller_frame, BALL_CAM_LABEL_ID, QRect(20, 250, 130, 30))
        self.brake_label = Label(self.controller_frame,BRAKE_LABEL_ID, QRect(20, 290, 130, 30))
        self.throttle_label = Label(self.controller_frame, THROTTLE_LABEL_ID, QRect(20, 330, 130, 30))

        # UI Controller Frame - data widgets
        self.powerslide_combo_box = ComboBox(self.controller_frame, POWERSLIDE_COMBO_BOX_ID, QRect(160, 10, 115, 30))
        self.air_roll_combo_box = ComboBox(self.controller_frame, AIR_ROLL_COMBO_BOX_ID, QRect(160, 50, 115, 30))
        self.air_roll_left_combo_box = ComboBox(self.controller_frame, AIR_ROLL_LEFT_COMBO_BOX_ID, QRect(160, 90, 115, 30))
        self.air_roll_right_combo_box = ComboBox(self.controller_frame, AIR_ROLL_RIGHT_COMBO_BOX_ID, QRect(160, 130, 115, 30))
        self.boost_combo_box = ComboBox(self.controller_frame, BOOST_COMBO_BOX_ID, QRect(160, 170, 115, 30))
        self.jump_combo_box = ComboBox(self.controller_frame, JUMP_COMBO_BOX_ID, QRect(160, 210, 115, 30))
        self.ball_cam_combo_box = ComboBox(self.controller_frame, BALL_CAM_COMBO_BOX_ID, QRect(160, 250, 115, 30))
        self.brake_combo_box = ComboBox(self.controller_frame, BRAKE_COMBO_BOX_ID, QRect(160, 290, 115, 30))
        self.throttle_combo_box = ComboBox(self.controller_frame, THROTTLE_COMBO_BOX_ID, QRect(160, 330, 115, 30))

        # UI Deadzone Frame - set up
        self.deadzone_frame = QFrame(self.frame)
        self.deadzone_frame.setGeometry(QRect(310, 11, 291, 211))
        self.deadzone_frame.setAutoFillBackground(False)
        self.deadzone_frame.setStyleSheet("")
        self.deadzone_frame.setFrameShape(QFrame.Panel)
        self.deadzone_frame.setFrameShadow(QFrame.Raised)
        self.deadzone_frame.setObjectName(DEADZONE_FRAME_ID)

        # UI Deadzone Frame - labels
        self.deadzone_label = Label(self.deadzone_frame, DEADZONE_LABEL_ID, QRect(10, 10, 141, 30))
        self.dodge_deadzone_label = Label(self.deadzone_frame, DODGE_DEADZONE_LABEL_ID, QRect(10, 50, 141, 30))
        self.aerial_sensitivity_label = Label(self.deadzone_frame, AERIAL_SENSITIVITY_LABEL_ID, QRect(10, 90, 141, 30))
        self.steering_sensitivity_label = Label(self.deadzone_frame, STEERING_SENSITIVITY_LABEL_ID, QRect(10, 130, 141, 30))
        self.last_updated_label = Label(self.deadzone_frame, LAST_UPDATED_LABEL_ID, QRect(10, 170, 141, 30))

        # UI Deadzone Frame - data widgets
        self.deadzone_spin_box = DoubleSpinBox(self.deadzone_frame,DEADZONE_SPIN_BOX_ID, QRect(161, 10, 115, 30), 0, 0.75, 0.2, 0.01)
        self.dodge_deadzone_spin_box = DoubleSpinBox(self.deadzone_frame, DODGE_DEADZONE_SPIN_BOX_ID, QRect(160, 50, 115, 30), 0.1, 1.0, 0.8, 0.01)
        self.aerial_sensitivity_spin_box = DoubleSpinBox(self.deadzone_frame, AERIAL_SENSITIVITY_SPIN_BOX_ID, QRect(160, 90, 115, 30), 1.0, 10.0, 1.0, 0.01)
        self.steering_sensitivity_spin_box = DoubleSpinBox(self.deadzone_frame, STEERING_SENSITIVITY_SPIN_BOX_ID, QRect(160, 130, 115, 30), 1.0, 10.0, 1.0, 0.01)
        self.last_updated_text_box = TextBox(self.deadzone_frame, LAST_UPDATED_TEXT_BOX_ID, QRect(161, 170, 115, 30))

        # UI Camera Frame - set up
        self.camera_frame = QFrame(self.frame)
        self.camera_frame.setGeometry(QRect(10, 171, 291, 411))
        self.camera_frame.setAutoFillBackground(False)
        self.camera_frame.setFrameShape(QFrame.Panel)
        self.camera_frame.setFrameShadow(QFrame.Raised)
        self.camera_frame.setObjectName(CAMERA_FRAME_ID)

        # UI Camera Frame - labels
        self.camera_shake_label = Label(self.camera_frame, CAMERA_SHAKE_LABEL_ID, QRect(20, 10, 130, 30))
        self.fov_label = Label(self.camera_frame, FOV_LABEL_ID, QRect(20, 50, 130, 30))
        self.height_label = Label(self.camera_frame, HEIGHT_LABEL_ID, QRect(20, 90, 130, 30))
        self.angle_label = Label(self.camera_frame, ANGLE_LABEL_ID, QRect(20, 130, 130, 30))
        self.distance_label = Label(self.camera_frame, DISTANCE_LABEL_ID, QRect(20, 170, 130, 30))
        self.stiffness_label = Label(self.camera_frame, STIFFNESS_LABEL_ID, QRect(20, 210, 130, 30))
        self.swivel_speed_label = Label(self.camera_frame, SWIVEL_SPEED_LABEL_ID, QRect(20, 250, 130, 30))
        self.transition_speed_label = Label(self.camera_frame, TRANSITION_SPEED_LABEL_ID, QRect(20, 290, 130, 30))
        self.ball_camera_label = Label(self.camera_frame, BALL_CAMERA_LABEL_ID, QRect(20, 330, 130, 30))
        self.last_updated_label_2 = Label(self.camera_frame, LAST_UPDATED_2_LABEL_ID, QRect(20, 370, 130, 30))

        # UI Camera Frame - data widgets
        self.camera_shake_checkbox = Checkbox(self.camera_frame, CAMERA_SHAKE_CHECKBOX_ID, QRect(160, 10, 115, 30))
        self.fov_spin_box = SpinBox(self.camera_frame, FOV_SPIN_BOX_ID, QRect(160, 50, 115, 30), 60, 110, 110, 1)
        self.height_spin_box = SpinBox(self.camera_frame, HEIGHT_SPIN_BOX_ID, QRect(160, 90, 115, 30), 40, 200, 100, 10)
        self.angle_spin_box = DoubleSpinBox(self.camera_frame, ANGLE_SPIN_BOX_ID, QRect(160, 130, 115, 30), -15, 0, -3, 1)
        self.distance_spin_box = SpinBox(self.camera_frame, DISTANCE_BOX_ID, QRect(160, 170, 115, 30), 100, 400, 270, 10)
        self.stiffness_spin_box = DoubleSpinBox(self.camera_frame, STIFFNESS_SPIN_BOX_ID, QRect(160, 210, 115, 30), 0, 1.0, 1.0, 0.05)
        self.swivel_speed_spin_box = DoubleSpinBox(self.camera_frame, SWIVEL_SPEED_SPIN_BOX_ID, QRect(160, 250, 115, 30), 1.0, 10.0, 2.5, 0.1)
        self.transition_speed_spin_box = DoubleSpinBox(self.camera_frame, TRANSITION_SPEED_SPIN_BOX_ID, QRect(160, 290, 115, 30), 1.0, 2.0, 1.0, 0.1)
        self.ball_camera_combo_box = ComboBox(self.camera_frame, BALL_CAMERA_COMBO_BOX_ID, QRect(160, 330, 115, 30))
        self.last_updated_text_box_2 = TextBox(self.camera_frame, LAST_UPDATED_2_TEXT_BOX_ID, QRect(160, 370, 115, 30))

        # UI Button Frame - set up
        self.button_frame = QFrame(self.frame)
        self.button_frame.setGeometry(QRect(20, 610, 571, 51))
        self.button_frame.setFrameShape(QFrame.Panel)
        self.button_frame.setFrameShadow(QFrame.Raised)
        self.button_frame.setObjectName(BUTTON_FRAME_ID)

        # UI Button Frame - buttons
        self.donate_button = DonateButton(self.button_frame, DONATE_BUTTON_LABEL_ID, QRect(20, 10, 81, 31))
        self.defaults_button = Button(self.button_frame, DEFAULTS_BUTTON_LABEL_ID, QRect(120, 10, 131, 31))
        self.reset_button = Button(self.button_frame, RESET_BUTTON_LABEL_ID, QRect(270, 10, 131, 31))
        self.apply_button = Button(self.button_frame, APPLY_BUTTON_LABEL_ID, QRect(420, 10, 131, 31))

        # UI Button Frame - button handlers
        self.defaults_button.clicked.connect(self.handle_defaults_button)
        self.reset_button.clicked.connect(self.handle_reset_button)

        self.setCentralWidget(self.central_widget)

        self.retranslate_ui()
        QMetaObject.connectSlotsByName(self)

    def handle_defaults_button(self):
        print("Resetting all settings to default")
        self.player_combo_box.setCurrentText(PLAYER_COMBO_BOX_DEFAULT)
        self.fill_fields()

    def handle_reset_button(self):
        print("Resetting settings back to selected players")
        self.fill_fields()

    def fill_fields(self):
        player = self.player_dict.get(str(self.player_combo_box.currentText()))
        print("Filling settings to " + player.name + "'s")

        if player.team is not None and str(player.team) != "":
            self.team_text_box.setText(player.team)
        else:
            self.team_text_box.setText(NOT_AVAILABLE)

        camera_settings = player.camera_settings
        if camera_settings is not None:
            self.fill_camera_settings_fields(
                camera_settings.camera_shake, camera_settings.fov, camera_settings.height,
                camera_settings.angle, camera_settings.distance, camera_settings.stiffness,
                camera_settings.swivel_speed, camera_settings.transition_speed,
                camera_settings.ball_camera, camera_settings.last_updated)
        else:
            self.fill_camera_settings_fields(CAMERA_SHAKE_DEFAULT_VALUE, FOV_DEFAULT_VALUE, HEIGHT_DEFAULT_VALUE, ANGLE_DEFAULT_VALUE, DISTANCE_DEFAULT_VALUE, STIFFNESS_DEFAULT_VALUE, SWIVEL_SPEED_DEFAULT_VALUE, TRANSITION_SPEED_DEFAULT_VALUE, BALL_CAMERA_DEFAULT_VALUE, NOT_AVAILABLE)

        controller_settings = player.controller_settings
        if controller_settings is not None:
            self.fill_controller_settings_fields(
                self.convert_control(controller_settings.powerslide),
                self.convert_control(controller_settings.air_roll),
                self.convert_control(controller_settings.air_roll),
                self.convert_control(controller_settings.air_roll),
                self.convert_control(controller_settings.boost),
                self.convert_control(controller_settings.jump),
                self.convert_control(controller_settings.ball_cam),
                self.convert_control(controller_settings.brake),
                self.convert_control(controller_settings.throttle))
        else:
            self.fill_controller_settings_fields(POWERSLIDE_DEFAULT_VALUE, AIR_ROLL_DEFAULT_VALUE, AIR_ROLL_LEFT_DEFAULT_VALUE, AIR_ROLL_RIGHT_DEFAULT_VALUE, BOOST_DEFAULT_VALUE, JUMP_DEFAULT_VALUE, BALL_CAM_DEFAULT_VALUE, BRAKE_DEFAULT_VALUE, THROTTLE_DEFAULT_VALUE)

        deadzone_settings = player.deadzone_settings
        if deadzone_settings is not None:
            self.fill_deadzone_settings_fields(
                deadzone_settings.deadzone,
                deadzone_settings.dodge_deadzone,
                deadzone_settings.aerial_sensitivity,
                deadzone_settings.steering_sensitivity,
                deadzone_settings.last_updated)
        else:
            self.fill_deadzone_settings_fields(DEADZONE_DEFAULT_VALUE, DODGE_DEADZONE_DEFAULT_VALUE, AERIAL_SENSITIVITY_DEFAULT_VALUE, STEERING_SENSITIVITY_DEFAULT_VALUE, NOT_AVAILABLE)

    def fill_deadzone_settings_fields(self, deadzone, dodge_deadzone, aerial_sensitivity,
                                      steering_sensitivity, last_updated):
        self.deadzone_spin_box.setValue(float(deadzone))
        self.dodge_deadzone_spin_box.setValue(float(dodge_deadzone))
        self.aerial_sensitivity_spin_box.setValue(float(aerial_sensitivity))
        self.steering_sensitivity_spin_box.setValue(float(steering_sensitivity))
        self.last_updated_text_box.setText(last_updated)

    def fill_controller_settings_fields(self, powerslide, air_roll, air_roll_left, air_roll_right, boost, jump,
                                        ball_cam, brake, throttle):
        self.powerslide_combo_box.setCurrentText(powerslide)
        self.air_roll_combo_box.setCurrentText(air_roll)
        self.air_roll_left_combo_box.setCurrentText(air_roll_left)
        self.air_roll_right_combo_box.setCurrentText(air_roll_right)
        self.boost_combo_box.setCurrentText(boost)
        self.jump_combo_box.setCurrentText(jump)
        self.ball_cam_combo_box.setCurrentText(ball_cam)
        self.brake_combo_box.setCurrentText(brake)
        self.throttle_combo_box.setCurrentText(throttle)

    def fill_camera_settings_fields(self, camera_shake, fov, height, angle, distance, stiffness, swivel_speed,
                                    transition_speed, ball_camera, last_updated):
        self.camera_shake_checkbox.setChecked(camera_shake == 'Yes')
        self.fov_spin_box.setValue(int(fov))
        self.height_spin_box.setValue(int(height))
        self.angle_spin_box.setValue(float(angle))
        self.distance_spin_box.setValue(int(distance))
        self.stiffness_spin_box.setValue(float(stiffness))
        self.swivel_speed_spin_box.setValue(float(swivel_speed))
        self.transition_speed_spin_box.setValue(float(transition_speed))
        self.ball_camera_combo_box.setCurrentText(ball_camera)
        self.last_updated_text_box_2.setText(last_updated)

    def convert_control(self, control):
        if control == PLAYSTATION_CROSS.upper() or control == XBOX_A:
            return PLAYSTATION_CROSS
        if control == PLAYSTATION_TRIANGLE.upper() or control == XBOX_Y:
            return PLAYSTATION_TRIANGLE
        if control == PLAYSTATION_CIRCLE.upper() or control == XBOX_B:
            return PLAYSTATION_CIRCLE
        if control == PLAYSTATION_SQUARE.upper() or control == XBOX_X:
            return PLAYSTATION_SQUARE
        if control == PLAYSTATION_L1 or control == XBOX_LB:
            return PLAYSTATION_L1
        if control == PLAYSTATION_L2 or control == XBOX_LT:
            return PLAYSTATION_L2
        if control == PLAYSTATION_R1 or control == XBOX_RB:
            return PLAYSTATION_R1
        if control == PLAYSTATION_R2 or control == XBOX_RT:
            return PLAYSTATION_R2
        else:
            return UNMAPPED

    def retranslate_ui(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate(MAIN_WINDOW_LABEL, APPLICATION_NAME))
        self.powerslide_label.setText(_translate(MAIN_WINDOW_LABEL, POWERSLIDE_LABEL))
        self.air_roll_label.setText(_translate(MAIN_WINDOW_LABEL, AIR_ROLL_LABEL))
        self.air_roll_left_label.setText(_translate(MAIN_WINDOW_LABEL, AIR_ROLL_LEFT_LABEL))
        self.air_roll_right_label.setText(_translate(MAIN_WINDOW_LABEL, AIR_ROLL_RIGHT_LABEL))
        self.jump_label.setText(_translate(MAIN_WINDOW_LABEL, JUMP_LABEL))
        self.brake_label.setText(_translate(MAIN_WINDOW_LABEL, BRAKE_LABEL))
        self.throttle_label.setText(_translate(MAIN_WINDOW_LABEL, THROTTLE_LABEL))
        self.ball_cam_label.setText(_translate(MAIN_WINDOW_LABEL, BALL_CAM_LABEL))
        self.boost_label.setText(_translate(MAIN_WINDOW_LABEL, BOOST_LABEL))
        self.powerslide_combo_box.setItemText(0, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_L1))
        self.powerslide_combo_box.setItemText(1, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_CROSS))
        self.powerslide_combo_box.setItemText(2, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_SQUARE))
        self.powerslide_combo_box.setItemText(3, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_CIRCLE))
        self.powerslide_combo_box.setItemText(4, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_TRIANGLE))
        self.powerslide_combo_box.setItemText(5, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_LEFT_STICK))
        self.powerslide_combo_box.setItemText(6, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_RIGHT_STICK))
        self.powerslide_combo_box.setItemText(7, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_R1))
        self.powerslide_combo_box.setItemText(8, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_R2))
        self.powerslide_combo_box.setItemText(9, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_L2))
        self.powerslide_combo_box.setItemText(10, _translate(MAIN_WINDOW_LABEL, UNMAPPED))
        self.air_roll_combo_box.setItemText(9, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_L1))
        self.air_roll_combo_box.setItemText(1, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_CROSS))
        self.air_roll_combo_box.setItemText(2, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_SQUARE))
        self.air_roll_combo_box.setItemText(3, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_CIRCLE))
        self.air_roll_combo_box.setItemText(4, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_TRIANGLE))
        self.air_roll_combo_box.setItemText(5, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_LEFT_STICK))
        self.air_roll_combo_box.setItemText(6, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_RIGHT_STICK))
        self.air_roll_combo_box.setItemText(7, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_R1))
        self.air_roll_combo_box.setItemText(8, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_R2))
        self.air_roll_combo_box.setItemText(10, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_L2))
        self.air_roll_combo_box.setItemText(0, _translate(MAIN_WINDOW_LABEL, UNMAPPED))
        self.air_roll_left_combo_box.setItemText(0, _translate(MAIN_WINDOW_LABEL, UNMAPPED))
        self.air_roll_left_combo_box.setItemText(1, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_CROSS))
        self.air_roll_left_combo_box.setItemText(2, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_SQUARE))
        self.air_roll_left_combo_box.setItemText(3, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_CIRCLE))
        self.air_roll_left_combo_box.setItemText(4, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_TRIANGLE))
        self.air_roll_left_combo_box.setItemText(5, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_LEFT_STICK))
        self.air_roll_left_combo_box.setItemText(6, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_RIGHT_STICK))
        self.air_roll_left_combo_box.setItemText(7, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_R1))
        self.air_roll_left_combo_box.setItemText(8, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_R2))
        self.air_roll_left_combo_box.setItemText(9, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_L1))
        self.air_roll_left_combo_box.setItemText(10, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_L2))
        self.air_roll_right_combo_box.setItemText(0, _translate(MAIN_WINDOW_LABEL, UNMAPPED))
        self.air_roll_right_combo_box.setItemText(1, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_CROSS))
        self.air_roll_right_combo_box.setItemText(2, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_SQUARE))
        self.air_roll_right_combo_box.setItemText(3, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_CIRCLE))
        self.air_roll_right_combo_box.setItemText(4, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_TRIANGLE))
        self.air_roll_right_combo_box.setItemText(5, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_LEFT_STICK))
        self.air_roll_right_combo_box.setItemText(6, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_RIGHT_STICK))
        self.air_roll_right_combo_box.setItemText(7, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_R2))
        self.air_roll_right_combo_box.setItemText(8, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_L1))
        self.air_roll_right_combo_box.setItemText(9, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_L2))
        self.air_roll_right_combo_box.setItemText(10, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_R1))
        self.boost_combo_box.setItemText(0, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_CIRCLE))
        self.boost_combo_box.setItemText(1, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_CROSS))
        self.boost_combo_box.setItemText(2, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_SQUARE))
        self.boost_combo_box.setItemText(3, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_TRIANGLE))
        self.boost_combo_box.setItemText(4, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_LEFT_STICK))
        self.boost_combo_box.setItemText(5, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_RIGHT_STICK))
        self.boost_combo_box.setItemText(6, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_R1))
        self.boost_combo_box.setItemText(7, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_R2))
        self.boost_combo_box.setItemText(8, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_L1))
        self.boost_combo_box.setItemText(9, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_L2))
        self.boost_combo_box.setItemText(10, _translate(MAIN_WINDOW_LABEL, UNMAPPED))
        self.jump_combo_box.setItemText(0, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_CROSS))
        self.jump_combo_box.setItemText(1, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_SQUARE))
        self.jump_combo_box.setItemText(2, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_CIRCLE))
        self.jump_combo_box.setItemText(3, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_TRIANGLE))
        self.jump_combo_box.setItemText(4, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_LEFT_STICK))
        self.jump_combo_box.setItemText(5, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_RIGHT_STICK))
        self.jump_combo_box.setItemText(6, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_R1))
        self.jump_combo_box.setItemText(7, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_R2))
        self.jump_combo_box.setItemText(8, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_L1))
        self.jump_combo_box.setItemText(9, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_L2))
        self.jump_combo_box.setItemText(10, _translate(MAIN_WINDOW_LABEL, UNMAPPED))
        self.brake_combo_box.setItemText(0, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_L2))
        self.brake_combo_box.setItemText(1, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_CROSS))
        self.brake_combo_box.setItemText(2, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_SQUARE))
        self.brake_combo_box.setItemText(3, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_CIRCLE))
        self.brake_combo_box.setItemText(4, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_TRIANGLE))
        self.brake_combo_box.setItemText(5, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_LEFT_STICK))
        self.brake_combo_box.setItemText(6, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_RIGHT_STICK))
        self.brake_combo_box.setItemText(7, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_R1))
        self.brake_combo_box.setItemText(8, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_R2))
        self.brake_combo_box.setItemText(9, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_L1))
        self.brake_combo_box.setItemText(10, _translate(MAIN_WINDOW_LABEL, UNMAPPED))
        self.throttle_combo_box.setItemText(0, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_R2))
        self.throttle_combo_box.setItemText(1, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_CROSS))
        self.throttle_combo_box.setItemText(2, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_SQUARE))
        self.throttle_combo_box.setItemText(3, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_CIRCLE))
        self.throttle_combo_box.setItemText(4, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_TRIANGLE))
        self.throttle_combo_box.setItemText(5, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_LEFT_STICK))
        self.throttle_combo_box.setItemText(6, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_RIGHT_STICK))
        self.throttle_combo_box.setItemText(7, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_R1))
        self.throttle_combo_box.setItemText(8, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_L1))
        self.throttle_combo_box.setItemText(9, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_L2))
        self.throttle_combo_box.setItemText(10, _translate(MAIN_WINDOW_LABEL, UNMAPPED))
        self.ball_cam_combo_box.setItemText(0, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_TRIANGLE))
        self.ball_cam_combo_box.setItemText(1, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_CROSS))
        self.ball_cam_combo_box.setItemText(2, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_SQUARE))
        self.ball_cam_combo_box.setItemText(3, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_CIRCLE))
        self.ball_cam_combo_box.setItemText(4, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_LEFT_STICK))
        self.ball_cam_combo_box.setItemText(5, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_RIGHT_STICK))
        self.ball_cam_combo_box.setItemText(6, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_R1))
        self.ball_cam_combo_box.setItemText(7, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_R2))
        self.ball_cam_combo_box.setItemText(8, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_L1))
        self.ball_cam_combo_box.setItemText(9, _translate(MAIN_WINDOW_LABEL, PLAYSTATION_L2))
        self.ball_cam_combo_box.setItemText(10, _translate(MAIN_WINDOW_LABEL, UNMAPPED))
        self.reset_button.setText(_translate(MAIN_WINDOW_LABEL, RESET_BUTTON_LABEL))
        self.apply_button.setText(_translate(MAIN_WINDOW_LABEL, APPLY_BUTTON_LABEL))
        self.defaults_button.setText(_translate(MAIN_WINDOW_LABEL, DEFAULTS_BUTTON_LABEL))
        self.donate_button.setText(_translate(MAIN_WINDOW_LABEL, DONATE_BUTTON_LABEL))
        self.deadzone_label.setText(_translate(MAIN_WINDOW_LABEL, DEADZONE_LABEL))
        self.aerial_sensitivity_label.setText(_translate(MAIN_WINDOW_LABEL, AERIAL_SENSITIVITY_LABEL))
        self.last_updated_label.setText(_translate(MAIN_WINDOW_LABEL, LAST_UPDATED_LABEL))
        self.steering_sensitivity_label.setText(_translate(MAIN_WINDOW_LABEL, STEERING_SENSITIVITY_LABEL))
        self.dodge_deadzone_label.setText(_translate(MAIN_WINDOW_LABEL, DODGE_DEADZONE_LABEL))
        # self.player_combo_box.setItemText(0, _translate(MAIN_WINDOW_LABEL, PLAYER_COMBO_BOX_DEFAULT))
        self.player_combo_box.addItems(self.player_dict.keys())
        self.team_text_box.setText(_translate(MAIN_WINDOW_LABEL, NOT_AVAILABLE))
        self.team_label.setText(_translate(MAIN_WINDOW_LABEL, TEAM_LABEL))
        self.camera_shake_label.setText(_translate(MAIN_WINDOW_LABEL, CAMERA_SHAKE_LABEL))
        self.fov_label.setText(_translate(MAIN_WINDOW_LABEL, FOV_LABEL))
        self.angle_label.setText(_translate(MAIN_WINDOW_LABEL, ANGLE_LABEL))
        self.stiffness_label.setText(_translate(MAIN_WINDOW_LABEL, STIFFNESS_LABEL))
        self.swivel_speed_label.setText(_translate(MAIN_WINDOW_LABEL, SWIVEL_SPEED_LABEL))
        self.transition_speed_label.setText(_translate(MAIN_WINDOW_LABEL, TRANSITION_SPEED_LABEL))
        self.distance_label.setText(_translate(MAIN_WINDOW_LABEL, DISTANCE_LABEL))
        self.height_label.setText(_translate(MAIN_WINDOW_LABEL, HEIGHT_LABEL))
        self.ball_camera_label.setText(_translate(MAIN_WINDOW_LABEL, BALL_CAMERA_LABEL))
        self.last_updated_label_2.setText(_translate(MAIN_WINDOW_LABEL, LAST_UPDATED_2_LABEL))
        self.ball_camera_combo_box.setItemText(0, _translate(MAIN_WINDOW_LABEL, TOGGLE))
        self.ball_camera_combo_box.setItemText(1, _translate(MAIN_WINDOW_LABEL, HOLD))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
