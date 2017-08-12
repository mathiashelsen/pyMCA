"""PyAudio Example: Play a WAVE file."""

import pyaudio
import wave
import sys
import argparse
import numpy as np

FRAMESIZE = 4096
SAMPLERATE = 44100

threshold = 0.05

def callbackFunction(in_data, frame_count, time_info, status):
	data = np.fromstring(in_data, dtype=np.float32)
	offset = np.ones(data.shape)*threshold
	crossings = np.where(np.diff(np.sign(data+offset)))[0]
	flag = pyaudio.paContinue
	if(len(crossings) > 0):
		print crossings
		flag = pyaudio.paComplete
		print "Found a crossing point"
	
	return (None, flag)

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--list", help="list available devices",
	action="store_true")
parser.add_argument("-d", "--device", help="index of the device to use",
	type=int)
parser.add_argument("-t", "--threshold", help="threshold value for triggering",
	type=int)
args = parser.parse_args()

p = pyaudio.PyAudio()

if args.list:
	for i in range(0, p.get_device_count()):
		print "Device", str(i), ":", p.get_device_info_by_index(i)['name']

device = 0
if args.device:
	device = args.device
	print p.get_device_info_by_index(device)

print device
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=SAMPLERATE,
                input=True,
				input_device_index = device,
                stream_callback=callbackFunction)

print "Press enter to exit"
raw_input()

p.terminate()
