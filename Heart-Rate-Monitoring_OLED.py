import serial
import matplotlib.pyplot as plt
from collections import deque

ser = serial.Serial('COM3', 9600, timeout=1)
plt.ion()
bpm_values = deque(maxlen=50)

while True:
    if ser.in_waiting > 0:
        bpm = ser.readline().decode().strip()
        if bpm.isdigit():
            bpm_values.append(int(bpm))
            plt.clf()
            plt.plot(bpm_values)
            plt.ylim(40, 180)  # Heart rate range
            plt.xlabel('Time')
            plt.ylabel('BPM')
            plt.pause(0.01)
