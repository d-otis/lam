import cv3
import matplotlib.pyplot as plt

cap = cv3.Video('sample.mp4')
frame = cap.read()

with cv3.Window('Demo') as window:
    window.imshow(frame)
    window.wait_key(0)