import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dimension = (width, height)

f = cv2.VideoWriter_fourcc(*"XVID")

output = VideoWriter("test.mp4", f, 30.0, dimension)

now_start_time = time.time()
print("Enter the duration of the video :")
duration = int(input())
end_time = now_start_time + duration
while True:
    image = pyautogui.screenshot()
    frame_1 = np.array(image)
    frame = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB)
    output.write(frame)
    current_time = time.time()
    if current_time > end_time:
        break
output.release()
print("END")
