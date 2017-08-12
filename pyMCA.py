"""PyAudio Example: Play a WAVE file."""

import pyaudio
import wave
import sys
import argparse

FRAMESIZE = 4096
SAMPLERATE = 44100

def callbackFunction(in_data, frame_count, time_info, status):
	return (None, pyaudio.paContinue)
	

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


stream = p.open(format=pyaudio.paFloat32,
                channels=2,
                rate=SAMPLERATE,
                input=True,
				input_device_index = device,
                stream_callback=callbackFunction)

print "Press enter to exit"
raw_input()

p.terminate()
