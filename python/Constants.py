import os
from dotenv import load_dotenv

load_dotenv()
CAMERA_URL = os.getenv('CAMERA_URL')
CONTROL_URL = os.getenv('CONTROL_URL')
DEADZONE_URL = os.getenv('DEADZONE_URL')


# Global config
APPLICATION_NAME = "Project Squishy - hillnet"
FONT = "Arial"
FONT_SIZE = 12
MAIN_WINDOW_LABEL = "MainWindow"
MAIN_WINDOW_STYLE_SHEET = "background-color: rgb(236, 236, 236)"


# Player
PLAYER_FRAME_ID = "player_frame"
PLAYER_LABEL = "Player"
TEAM_LABEL = "Team"

PLAYER_LABEL_ID = "player_label"
TEAM_LABEL_ID = "team_label"
TEAM_TEXT_BOX_ID = "team_text_box"
PLAYER_COMBO_BOX_DEFAULT = "Select player..."


# Controller
CONTROLLER_FRAME_ID = "controller_frame"
POWERSLIDE_LABEL_ID = "powerslide_label"
AIR_ROLL_LABEL_ID = "air_roll_label"
AIR_ROLL_LEFT_LABEL_ID = "air_roll_left_label"
AIR_ROLL_RIGHT_LABEL_ID = "air_roll_right_label"
BOOST_LABEL_ID = "boost_label"
JUMP_LABEL_ID = "jump_label"
BALL_CAM_LABEL_ID = "ball_cam_label"
BRAKE_LABEL_ID = "brake_label"
THROTTLE_LABEL_ID = "throttle_label"

POWERSLIDE_LABEL = "Powerslide"
AIR_ROLL_LABEL = "Air Roll"
AIR_ROLL_LEFT_LABEL = "Air Roll Left"
AIR_ROLL_RIGHT_LABEL = "Air Roll Right"
BOOST_LABEL = "Boost"
JUMP_LABEL = "Jump"
BALL_CAM_LABEL = "Ball Cam"
BRAKE_LABEL = "Brake"
THROTTLE_LABEL = "Throttle"

POWERSLIDE_COMBO_BOX_ID = "powerslide_combo_box"
AIR_ROLL_COMBO_BOX_ID = "air_roll_combo_box"
AIR_ROLL_LEFT_COMBO_BOX_ID = "air_roll_left_combo_box"
AIR_ROLL_RIGHT_COMBO_BOX_ID = "air_roll_right_combo_box"
BOOST_COMBO_BOX_ID = "boost_combo_box"
JUMP_COMBO_BOX_ID = "jump_combo_box"
BALL_CAM_COMBO_BOX_ID = "ball_cam_combo_box"
BRAKE_COMBO_BOX_ID = "brake_combo_box"
THROTTLE_COMBO_BOX_ID = "throttle_combo_box"


# Deadzone
DEADZONE_FRAME_ID = "deadzone_frame"
DEADZONE_LABEL_ID = "deadzone_label"
DODGE_DEADZONE_LABEL_ID = "dodge_deadzone_label"
AERIAL_SENSITIVITY_LABEL_ID = "aerial_sensitivity_label"
STEERING_SENSITIVITY_LABEL_ID = "steering_sensitivity_label"
LAST_UPDATED_LABEL_ID = "last_updated_label"

DEADZONE_LABEL = "Deadzone"
DODGE_DEADZONE_LABEL = "Dodge Deadzone"
AERIAL_SENSITIVITY_LABEL = "Aerial Sensitivity"
STEERING_SENSITIVITY_LABEL = "Steering Sensitivity"
LAST_UPDATED_LABEL = "Last Updated"

DEADZONE_SPIN_BOX_ID = "deadzone_spin_box"
DODGE_DEADZONE_SPIN_BOX_ID = "dodge_deadzone_spin_box"
AERIAL_SENSITIVITY_SPIN_BOX_ID = "aerial_sensitivity_spin_box"
STEERING_SENSITIVITY_SPIN_BOX_ID = "steering_sensitivity_spin_box"
LAST_UPDATED_TEXT_BOX_ID = "last_updated_text_box"


# Camera
CAMERA_FRAME_ID = "camera_frame"
CAMERA_SHAKE_LABEL_ID = "camera_shake_label"
FOV_LABEL_ID = "fov_label"
HEIGHT_LABEL_ID = "height_label"
ANGLE_LABEL_ID = "angle_label"
DISTANCE_LABEL_ID = "distance_label"
STIFFNESS_LABEL_ID = "stiffness_label"
SWIVEL_SPEED_LABEL_ID = "swivel_speed_label"
TRANSITION_SPEED_LABEL_ID = "transition_speed_label"
BALL_CAMERA_LABEL_ID = "ball_camera_label"
LAST_UPDATED_2_LABEL_ID = "last_updated_label_2"

CAMERA_SHAKE_LABEL = "Camera Shake"
FOV_LABEL = "FOV"
HEIGHT_LABEL = "Height"
ANGLE_LABEL = "Angle"
DISTANCE_LABEL = "Distance"
STIFFNESS_LABEL = "Stiffness"
SWIVEL_SPEED_LABEL = "Swivel Speed"
TRANSITION_SPEED_LABEL = "Transition Speed"
BALL_CAMERA_LABEL = "Ball Camera"
LAST_UPDATED_2_LABEL = "Last Updated"

CAMERA_SHAKE_CHECKBOX_ID = "camera_shake_checkbox"
FOV_SPIN_BOX_ID = "fov_spin_box"
HEIGHT_SPIN_BOX_ID = "height_spin_box"
ANGLE_SPIN_BOX_ID = "angle_spin_box"
DISTANCE_BOX_ID = "distance_spin_box"
STIFFNESS_SPIN_BOX_ID = "stiffness_spin_box"
SWIVEL_SPEED_SPIN_BOX_ID = "swivel_speed_spin_box"
TRANSITION_SPEED_SPIN_BOX_ID = "transition_speed_spin_box"
BALL_CAMERA_COMBO_BOX_ID = "ball_camera_combo_box"
LAST_UPDATED_2_TEXT_BOX_ID = "last_updated_text_box_2"


# Button
BUTTON_FRAME_ID = "buttom_frame"
DONATE_BUTTON_LABEL_ID = "donate_button"
DEFAULTS_BUTTON_LABEL_ID = "defaults_button"
RESET_BUTTON_LABEL_ID = "reset_button"
APPLY_BUTTON_LABEL_ID ="apply_button"

DONATE_BUTTON_LABEL = "Donate"
DEFAULTS_BUTTON_LABEL = "Defaults"
RESET_BUTTON_LABEL = "Reset"
APPLY_BUTTON_LABEL = "Apply"


# Controller buttons
PLAYSTATION_L1 = "L1"
PLAYSTATION_CROSS = "Cross"
PLAYSTATION_SQUARE = "Square"
PLAYSTATION_CIRCLE = "Circle"
PLAYSTATION_TRIANGLE = "Triangle"
PLAYSTATION_LEFT_STICK = "Left stick"
PLAYSTATION_RIGHT_STICK = "Right stick"
PLAYSTATION_R1 = "R1"
PLAYSTATION_R2 = "R2"
PLAYSTATION_L2 = "L2"

XBOX_A = "A"
XBOX_X = "X"
XBOX_B = "B"
XBOX_Y = "Y"
XBOX_LEFT_STICK = "Left stick"
XBOX_RIGHT_STICK = "Right stick"
XBOX_RB = "RB"
XBOX_RT = "RT"
XBOX_LB = "LB"
XBOX_LT = "LT"

UNMAPPED = "Unmapped"
TOGGLE = "Toggle"
HOLD = "Hold"

# Defaults
POWERSLIDE_DEFAULT_VALUE = PLAYSTATION_L1
AIR_ROLL_DEFAULT_VALUE = UNMAPPED
AIR_ROLL_LEFT_DEFAULT_VALUE = UNMAPPED
AIR_ROLL_RIGHT_DEFAULT_VALUE = UNMAPPED
BOOST_DEFAULT_VALUE = PLAYSTATION_CIRCLE
JUMP_DEFAULT_VALUE = PLAYSTATION_CROSS
BALL_CAM_DEFAULT_VALUE = PLAYSTATION_TRIANGLE
BRAKE_DEFAULT_VALUE = PLAYSTATION_L2
THROTTLE_DEFAULT_VALUE = PLAYSTATION_R2

CAMERA_SHAKE_DEFAULT_VALUE = "No"
FOV_DEFAULT_VALUE = 110
HEIGHT_DEFAULT_VALUE = 100
ANGLE_DEFAULT_VALUE = -3.0
DISTANCE_DEFAULT_VALUE = 270
STIFFNESS_DEFAULT_VALUE = 1.0
SWIVEL_SPEED_DEFAULT_VALUE = 2.5
TRANSITION_SPEED_DEFAULT_VALUE = 1
BALL_CAMERA_DEFAULT_VALUE = TOGGLE

DEADZONE_DEFAULT_VALUE = 0.20
DODGE_DEADZONE_DEFAULT_VALUE = 0.80
AERIAL_SENSITIVITY_DEFAULT_VALUE = 1.0
STEERING_SENSITIVITY_DEFAULT_VALUE = 1.0

