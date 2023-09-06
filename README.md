# Gesture Volume Control
This Python code repository provides a hands-free audio volume control system using hand gestures. It utilizes the OpenCV, MediaPipe, and PyAutoGUI libraries to enable users to increase or decrease the system's audio volume by making specific hand gestures in front of a camera.

# Requirements
To run this code, you'll need the following Python libraries installed:
OpenCV (cv2)
NumPy (numpy)
MediaPipe (mediapipe)
PyAutoGUI (pyautogui)
You can install these libraries using pip:
pip install opencv-python numpy mediapipe pyautogui

# Usage
Clone or download this repository to your local machine.

Make sure you have a webcam or an external camera connected to your computer.

Run the gesture_volume_control.py script.

A webcam window will open, displaying your camera feed. Place your hand in front of the camera.

The code will detect your hand gestures. When you move your thumb and forefinger closer together, the system's volume will decrease. When you move them further apart, the volume will increase.

To exit the program, press the 'x' key while the camera window is in focus.

# Configuration
You can configure the camera settings by adjusting the wCam and hCam variables to set the desired camera resolution.
wCam, hCam = 1280, 820  # Adjust these values for your camera resolution
