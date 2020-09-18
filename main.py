import datetime
from random import *
from pydub import AudioSegment
from pydub.playback import play
import os

def run_ring_old():
    nms = os.listdir('actions')
    name = nms[randint(0, len(nms) - 1)]
    try:
        bit = from_mp3('actions\\' + name)
        play(bit)
    except:
        try:
            bit = from_wav('actions\\' + name)
            play(bit)
        except:
            os.startfile('actions\\' + name)

def run_ring():
    nms = os.listdir('actions')
    name = nms[randint(0, len(nms) - 1)]
    os.startfile('actions\\' + name)

print(datetime.datetime.now().time())
times = open('times.txt', 'r')
tms = []
while True:
    inp = times.readline()
    if 'end' in inp:
        break
    else:
        time_sep = inp.split(':')
        time = 60 * int(time_sep[0]) + int(time_sep[1])
        tms.append(time)
while True:
    tm = str(datetime.datetime.now().time()).split(':')
    time = 60 * int(tm[0]) + int(tm[1]) + float(tm[2]) * 0.01
    for tx in tms:
        if abs(tx - time) < 0.01:
            run_ring()
