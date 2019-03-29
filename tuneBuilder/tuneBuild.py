import time
import librosa
import matplotlib.pyplot as plt
import librosa.display
import IPython.display
import numpy as np
# import pygame
import soundfile as sf


def generateSound(frequency, sr, duration):
    if type(frequency) is int or type(frequency) is float:
        tone = librosa.tone(frequency, sr=sr, duration=duration)
    else:
        tone = librosa.tone(261.63, sr=sr, duration=1)   # C
        tone = np.append(tone, librosa.tone(293.66, sr=sr, duration=1))  # D
        # tone = np.append(tone, librosa.tone(293.66, sr=sr, duration=1))  # D
        tone = np.append(tone, librosa.tone(329.63, sr=sr, duration=1))  # E
        tone = np.append(tone, librosa.tone(349.23, sr=sr, duration=1))  # F
        tone = np.append(tone, librosa.tone(392.00, sr=sr, duration=1))  # G
        tone = np.append(tone, librosa.tone(440.00, sr=sr, duration=1))  # A
        tone = np.append(tone, librosa.tone(493.88, sr=sr, duration=1))  # B
        tone = np.append(tone, librosa.tone(525.25, sr=sr, duration=1))  # C
    return tone


# prepare a tone
sr = 22050
duration = 10
tone = generateSound("C", sr, duration)

# write to wav
sf.write('tuneBuildTest.wav', tone, samplerate=sr, subtype='PCM_16')
y, sr2 = librosa.load('tuneBuildTest.wav')

# graph it
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
