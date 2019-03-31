
# import time
import librosa
# import matplotlib.pyplot as plt
import librosa.display
import IPython.display
import numpy as np
# import pygame
import soundfile as sf
import argparse

"""Basic tone builder

Creates tones at a specified frequency
Generates a simple C scale
Generates a C scale with an error
"""

# Basic argument parser
ap = argparse.ArgumentParser(description="Generates tone[s]")
ap.add_argument("-f", "--frequency", required=False, help="frequency in hertz")
ap.add_argument("-s", "--scale", required=False,
                help="major scale (only C right now)")
ap.add_argument("-e", "--errors", required=False,
                help="number of errors in scale (only 1 for now)")
args = vars(ap.parse_args())


# generate a pure tone cosine wave
def generateSound(sr, duration, frequency=0, scale="", erros=0):
    global name
    if frequency is not None:
        frequency = int(frequency)
        name = str(frequency)
        tone = librosa.tone(frequency, sr=sr, duration=duration)
    elif scale is not None and errors is None:
        name = str(scale + "_scale")
        tone = librosa.tone(261.63, sr=sr, duration=1)                   # C
        tone = np.append(tone, librosa.tone(293.66, sr=sr, duration=1))  # D
        tone = np.append(tone, librosa.tone(329.63, sr=sr, duration=1))  # E
        tone = np.append(tone, librosa.tone(349.23, sr=sr, duration=1))  # F
        tone = np.append(tone, librosa.tone(392.00, sr=sr, duration=1))  # G
        tone = np.append(tone, librosa.tone(440.00, sr=sr, duration=1))  # A
        tone = np.append(tone, librosa.tone(493.88, sr=sr, duration=1))  # B
        tone = np.append(tone, librosa.tone(525.25, sr=sr, duration=1))  # C
    elif int(errors) == 1:
        name = str(scale + "_scale_e" + str(errors))
        tone = librosa.tone(261.63, sr=sr, duration=1)                   # C
        tone = np.append(tone, librosa.tone(293.66, sr=sr, duration=1))  # D
        tone = np.append(tone, librosa.tone(293.66, sr=sr, duration=1))  # D
        tone = np.append(tone, librosa.tone(349.23, sr=sr, duration=1))  # F
        tone = np.append(tone, librosa.tone(392.00, sr=sr, duration=1))  # G
        tone = np.append(tone, librosa.tone(440.00, sr=sr, duration=1))  # A
        tone = np.append(tone, librosa.tone(493.88, sr=sr, duration=1))  # B
        tone = np.append(tone, librosa.tone(525.25, sr=sr, duration=1))  # C
    else:
        name = "A440"
        tone = librosa.tone(440.00, sr=sr, duration=1)  # A
    return tone


# prepare a tone
sr = 22050
duration = 10
frequency = args["frequency"]
scale = args["scale"]
errors = args["errors"]
name = ""
tone = generateSound(sr, duration, frequency, scale, errors)

# write to wav
sf.write('tuneBuildTest_{}.wav'.format(str(name)),
         tone, samplerate=sr, subtype='PCM_16')

# graph it
# y, sr2 = librosa.load('tuneBuildTest.wav')
# plt.figure()
# S = librosa.feature.melspectrogram(y=tone)
# librosa.display.specshow(librosa.power_to_db(S, ref=np.max),
#                          x_axis='time', y_axis='mel')

# play it back
# pygame.mixer.init()
# pygame.mixer.music.load('tuneBuildTest.wav')
# pygame.mixer.music.set_volume(0.1)
# pygame.mixer.music.play()

# display player in notebook
# IPython.display.Audio(data=y, rate=sr2)
