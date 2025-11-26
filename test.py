import sys
import numpy as np
import cv2 as cv

sys.path.insert(1, './PythonLibs')
from windowcapture import WindowCapture

windowCaptureConfig = {
    'WINDOW_WIDTH': 1282,
    'WINDOW_HEIGHT': 752,
    'WIDNOW_NAME': 'Overgrowth'
}

gameWindow = WindowCapture(windowCaptureConfig)
print(gameWindow.hwnd)
cv.imwrite('screenshot.png', gameWindow.get_screenshot())