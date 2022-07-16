from pynput.keyboard import Listener
from pydub import AudioSegment
from pydub.playback import play
from threading import Thread
import random

filename = 'Scout_needdispenser01.wav'

sound = AudioSegment.from_file(file=filename, format="wav")
sounds = [None] * 24

for idx, s in enumerate(sounds):
    sounds[idx] = idx
    sounds[idx] = int(sound.frame_rate * (1.05 ** idx))
    sounds[idx] = sound._spawn(sound.raw_data, overrides={'frame_rate': sounds[idx]})
    sounds[idx] = sounds[idx].set_frame_rate(44100)


def playsound(index):
    play(sounds[index])


def on_press(key):
    if not hasattr(key, 'char') or ord(key.char) < ord('a') or ord(key.char) > ord('z'):
        new_thread = Thread(target=playsound, args={random.randint(0, 23)})
        new_thread.start()
        return

    print('{0} pressed'.format(
        key))
    ind = ord('z') - ord(key.char) - 24
    print(ind)
    new_thread = Thread(target=playsound, args={ind})
    new_thread.start()


with Listener(
        on_press=on_press) as listener:
    listener.join()
