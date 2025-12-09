import sys
import numpy as np
import cv2 as cv
import time

sys.path.insert(1, './PythonLibs')
from windowcapture import WindowCapture

windowCaptureConfig = {
    'WINDOW_WIDTH': 1282,
    'WINDOW_HEIGHT': 752,
    'WIDNOW_NAME': 'Overgrowth'
}

gameWindow = WindowCapture(windowCaptureConfig)
# print(gameWindow.hwnd)
# cv.imwrite('screenshot.png', gameWindow.get_screenshot())

import characterActions

gameWindow.focus_window()

characterActions.skipCutscene()
characterActions.moveForward()
time.sleep(2)
characterActions._stopMoving()


# a = {'key1': 1}
# a['key2'] = 2
# print(a)
# # print("Test file executed.")
# instr = '[{"id":2,"is_knocked_out":0,"is_player":true,"perm_health":1.0,"temp_health":1.0},{"id":7,"is_knocked_out":0,"is_player":false,"perm_health":1.0,"temp_health":1.0}]'
# import json
# data = json.loads(instr)
# for i in data:
#     print(i['id'])