import sys
import numpy as np
import cv2 as cv
import time
from gym_overgrowth.overgrowth_env import OvergrowthEnv
import gymnasium as gym 

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

# -------------------------------------------------------------------------------------------

import characterActions

gameWindow.focus_window()
env = OvergrowthEnv()
env.reset()
try:
    for _ in range(1000):
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
        print(f"Action: {action}, Reward: {reward}, Done: {done}")
        if done:
            env.reset()
            print("Done")
            break
except Exception as e:
    print(f"An error occurred: {e}")
    env.reset()

env.playerStateController.releaseAllKeys()
print(obs.shape,obs.dtype)

# characterActions.skipCutscene()
# characterActions.moveForward()
# time.sleep(2)
# characterActions._stopMoving()
# time.sleep(0.5)
# characterActions.moveLeft()
# time.sleep(2)
# characterActions._stopMoving()
# time.sleep(0.5)
# characterActions.moveRight()
# time.sleep(2)
# characterActions._stopMoving()
# time.sleep(0.5)
# characterActions.crouch()
# time.sleep(0.1)
# characterActions.moveBackwards()
# time.sleep(2)
# characterActions.moveRight()
# time.sleep(2)
# characterActions._stopMoving()
# time.sleep(1)
# characterActions.uncrouch()
# time.sleep(0.5)
# characterActions.holdJump()
# time.sleep(0.5)
# characterActions.releaseJump()




# a = {'key1': 1}
# a['key2'] = 2
# print(a)
# # print("Test file executed.")
# instr = '[{"id":2,"is_knocked_out":0,"is_player":true,"perm_health":1.0,"temp_health":1.0},{"id":7,"is_knocked_out":0,"is_player":false,"perm_health":1.0,"temp_health":1.0}]'
# import json
# data = json.loads(instr)
# for i in data:
#     print(i['id'])