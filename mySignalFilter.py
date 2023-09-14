# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 09:57:44 2023

"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
t = np.linspace(0, 10, 1000)
signal = np.sin(2 * np.pi * t) + 0.5 * np.random.normal(size=len(t))

def moving_average_filter(signal, window_size):
    window = np.ones(window_size) / float(window_size)
    filtered_signal = np.convolve(signal, window, "same")
    return filtered_signal

window_size = 20
filtered_signal = moving_average_filter(signal, window_size)

plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, signal, label="Noisy Signal", color="red")
plt.title("Noisy Signal")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t, filtered_signal, label="Filtered Signal", color="green")
plt.title("Filtered Signal")
plt.grid(True)

plt.tight_layout()
plt.show()
