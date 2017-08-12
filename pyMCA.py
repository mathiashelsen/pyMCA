"""PyAudio Example: Play a WAVE file."""

import pyaudio
import wave
import sys

p = pyaudio.PyAudio()

for i in range(0, p.get_device_count()):
	print p.get_device_info_by_index(i)['name']

p.terminate()
