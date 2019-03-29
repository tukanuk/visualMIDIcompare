#%% [markdown]
# # VisualMIDIcompare
# 
# A testing and analysis workflow
# 
#%% [markdown]
# ## Provide:
# 
# - [Spectrogram](https://en.wikipedia.org/wiki/Spectrogram)
# - ability to play MIDI files to compare
# - ability to convert to .wav using existing tools
# 
# Tool to generate a visual representation of a MIDI file. 
# Optionally, compare to a second MIDI file by diffing the images
# 
# ### Steps:
# 
# 1. Length of the MIDI file (x-axis of image).
# 2. 88 Keys (y-axis of image).
# 3. Plot each note on the image.
# 4. Grayscale to measure velocity (MIDI has 128 levels?)
# 5. Comparision emphasizes:
# 	1. notes with no match
# 	2. notes with differnet on/off points
# 	3. notes with different velocity
#     
# ### Reason: 
# 
# MIDI is a digitial format and can fairly straightforwaly be done numerically. This is not broadly useful to people. 
# 
# Existing MIDI editors have a visual editor but it is manual process to extract and line up images, and diff them.
#%% [markdown]
# ## Implementation:
# 
# - Python (jupyter notebook) 
# - use the same diff rules and colour as github.
# - command line tool
#%% [markdown]
# ## Optional:
# 
# 1. Add numeric comparisions
# 	- summary statistcs
# 	- note statistics
# 2. An interface where you can hover over images and get MIDI details
# 3. Choose output iamge format.
# 4. Choose to wrap the image (it will be a long image by default)
# 5. web interface
# 6. Chouse y-axis scale. Default will be 10px per 1/4 note.
#%% [markdown]
# # Imports 

#%%
from __future__ import print_function
#%%
# check environment
import sys
print("Path: {}".format(sys.path))
print("Executable: {}".format(sys.executable))




#%%
# Librosa Imports
import librosa
import librosa.display
import IPython.display
import numpy as np
import scipy


#%%
# Matplotlib Imports
import matplotlib.pyplot as plt
import matplotlib.style as ms
ms.use('seaborn-muted')
get_ipython().run_line_magic('matplotlib', 'inline')

#%% [markdown]
# # Source1 Track

#%%
# Source1 Audio Path
source1_audio_path = 'source/source1.wav'

# Load source1 track
y, sr = librosa.load(source1_audio_path)

# Get track duration
source1_duration = librosa.get_duration(y=y, sr=sr)

# Get a tuning estimate
# estimate_tuning: Estimate the tuning of an audio time series or spectrogram input
source1_tuning = librosa.estimate_tuning(y=y, sr=sr)

print("File: {} \nDuration: {:2.4f} sec".format(source1_audio_path, source1_duration))
print("Tuning estimate: {}".format(source1_tuning))

# Play back original track
IPython.display.Audio(data=y, rate=sr)

#%% [markdown]
# # Source 2 Track

#%%
# Source2 Audio Path
source2_audio_path = 'source/source2.wav'

# Load source2 track
y2, sr2 = librosa.load(source2_audio_path)

# Get track duration
source2_duration = librosa.get_duration(y=y, sr=sr)

# Get a tuning estimate
# estimate_tuning: Estimate the tuning of an audio time series or spectrogram input
source2_tuning = librosa.estimate_tuning(y=y, sr=sr)

print("File: {} \nDuration: {:2.4f} sec".format(
    source2_audio_path, source2_duration))
print("Tuning estimate: {}".format(source2_tuning))


# Play back original track
IPython.display.Audio(data=y2, rate=sr2)

#%% [markdown]
# # Prepare the tracks
#%% [markdown]
# ## Prepare Source1 Track

#%%
# mel-scaled power (energy-squared) spectrogram
S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)

# covert to log scale (dB). Using peak power (max) as reference.
log_S = librosa.power_to_db(S, ref=np.max)

# Prepare the graph
plt.figure(figsize=(12,8))

# Display spectrogram on a mel scale
# smaple rate and hop length parameters are used to render the time axis
plt.subplot(2,1,2)
librosa.display.specshow(log_S, sr=sr, x_axis='time', y_axis='mel')

# Give it a title
plt.title(source1_audio_path + " mel power spectrogram")

# draw a colour bar
plt.colorbar(format='%+02.0f dB')

# Plot
plt.tight_layout()

plt.subplot(2,1,1)
y_harm, y_perc = librosa.effects.hpss(y)
librosa.display.waveplot(y=y_harm, sr=sr, alpha=0.25)
librosa.display.waveplot(y=y_perc, sr=sr, color='r', alpha=0.25)
plt.colorbar().ax.set_visible(False)
plt.title('Harmonic + Percussive Waveplot')
plt.tight_layout()

#%% [markdown]
# ## Prepare Source2 Track

#%%
# mel-scaled power (energy-squared) spectrogram
S2 = librosa.feature.melspectrogram(y2, sr=sr2, n_mels=128)

# covert to log scale (dB). Using peak power (max) as reference.
log_S2 = librosa.power_to_db(S2, ref=np.max)

# Prepare the graph
plt.figure(figsize=(12,8))

# Display spectrogram on a mel scale
# smaple rate and hop length parameters are used to render the time axis
plt.subplot(2,1,2)
librosa.display.specshow(log_S2, sr=sr2, x_axis='time', y_axis='mel')

# Give it a title
plt.title(source2_audio_path + " mel power spectrogram")

# draw a colour bar
plt.colorbar(format='%+02.0f dB')

# Plot
plt.tight_layout()

plt.subplot(2,1,1)
y_harm, y_perc = librosa.effects.hpss(y2)
librosa.display.waveplot(y=y_harm, sr=sr, alpha=0.25)
librosa.display.waveplot(y=y_perc, sr=sr, color='r', alpha=0.25)
plt.colorbar().ax.set_visible(False)
plt.title('Harmonic + Percussive Waveplot')
plt.tight_layout()

#%% [markdown]
# # Testing Methods
#%% [markdown]
# ## Chromagram Testing on S1

#%%
C = librosa.feature.chroma_cqt(y=y, sr=sr)
plt.figure(figsize=(12,4))
librosa.display.specshow(C, y_axis='chroma')
plt.colorbar()
plt.title('Chromagram')
plt.tight_layout()

#%% [markdown]
# ## Constant-Q Testing on S1

#%%
CQT = librosa.amplitude_to_db(np.abs(librosa.cqt(y, sr=sr)), ref=np.max)
plt.figure(figsize=(12,4))
plt.title('Constant-Q power spectrogram note')
librosa.display.specshow(CQT, y_axis='cqt_note')
plt.colorbar(format='%+2.0f dB')
plt.tight_layout()


#%%
chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr,
                                          n_chroma=12, n_fft=4096)
chroma_cq = librosa.feature.chroma_cqt(y=y, sr=sr)

plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
librosa.display.specshow(chroma_stft, y_axis='chroma')
plt.title('chroma_stft')
plt.colorbar()
plt.subplot(1,2,2)
librosa.display.specshow(chroma_cq, y_axis='chroma', x_axis='time')
plt.title('chroma_cqt')
plt.colorbar()
plt.tight_layout()

#%% [markdown]
# ## Compare source1 and source2 Chromagram

#%%
C = librosa.feature.chroma_cqt(y=y, sr=sr)
C2 = librosa.feature.chroma_cqt(y=y2, sr=sr2)
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
a = librosa.display.specshow(C, x_axis='time', y_axis='chroma')
# plt.savefig('output_images/source1_chromagram.png', dpi=300)
plt.colorbar()
plt.title(source1_audio_path + ' Chromagram')
plt.subplot(1,2,2)
b = librosa.display.specshow(C2, x_axis='time', y_axis='chroma')
# plt.savefig('output_images/source2_chromagram.png', dpi=300)
plt.colorbar()
plt.title(source2_audio_path + ' Chromagram')
plt.tight_layout()


#%%
C = librosa.feature.chroma_cqt(y=y, sr=sr)
C2 = librosa.feature.chroma_cqt(y=y2, sr=sr2)
plt.figure(figsize=(12,4))
plt.ioff()
librosa.display.specshow(C)
plt.ioff()
plt.savefig('output_images/source1_chromagram.png', dpi=100, bbox_inches='tight')
plt.figure(figsize=(12,4))
librosa.display.specshow(C2)
plt.ioff()
plt.savefig('output_images/source2_chromagram.png', dpi=100, bbox_inches='tight')

#%% [markdown]
# # Enhanced chroma and chroma variants
# [Enhanced chroma and chroma variants](http://librosa.github.io/librosa/auto_examples/plot_chroma.html#sphx-glr-auto-examples-plot-chroma-py)
#%% [markdown]
# ## Original

#%%
chroma_orig = librosa.feature.chroma_cqt(y=y, sr=sr)

# And for comparison, we'll show the CQT matrix as well.
C = np.abs(librosa.cqt(y=y, sr=sr, bins_per_octave=12*3, n_bins=7*12*3))

plt.figure(figsize=(12, 4))
plt.subplot(2, 1, 1)
librosa.display.specshow(librosa.amplitude_to_db(C, ref=np.max),
                         y_axis='cqt_note', bins_per_octave=12*3)
plt.colorbar()
plt.subplot(2, 1, 2)
librosa.display.specshow(chroma_orig, y_axis='chroma')
plt.colorbar()
plt.ylabel('Original')
plt.tight_layout()

#%% [markdown]
# ## Correct Tuning Deviations

#%%
chroma_os = librosa.feature.chroma_cqt(y=y, sr=sr, bins_per_octave=12*3)


plt.figure(figsize=(12, 4))

plt.subplot(2, 1, 1)
librosa.display.specshow(chroma_orig, y_axis='chroma')
plt.colorbar()
plt.ylabel('Original')


plt.subplot(2, 1, 2)
librosa.display.specshow(chroma_os, y_axis='chroma', x_axis='time')
plt.colorbar()
plt.ylabel('3x-over')
plt.tight_layout()

#%% [markdown]
# ## Isolate harmonic component

#%%
y_harm = librosa.effects.harmonic(y=y, margin=8)
chroma_os_harm = librosa.feature.chroma_cqt(y=y_harm, sr=sr, bins_per_octave=12*3)


plt.figure(figsize=(12, 4))

plt.subplot(2, 1, 1)
librosa.display.specshow(chroma_os, y_axis='chroma')
plt.colorbar()
plt.ylabel('3x-over')

plt.subplot(2, 1, 2)
librosa.display.specshow(chroma_os_harm, y_axis='chroma', x_axis='time')
plt.colorbar()
plt.ylabel('Harmonic')
plt.tight_layout()

#%% [markdown]
# ## Non-local filtering

#%%
chroma_filter = np.minimum(chroma_os_harm,
                           librosa.decompose.nn_filter(chroma_os_harm,
                                                       aggregate=np.median,
                                                       metric='cosine'))


plt.figure(figsize=(12, 4))

plt.subplot(2, 1, 1)
librosa.display.specshow(chroma_os_harm, y_axis='chroma')
plt.colorbar()
plt.ylabel('Harmonic')

plt.subplot(2, 1, 2)
librosa.display.specshow(chroma_filter, y_axis='chroma', x_axis='time')
plt.colorbar()
plt.ylabel('Non-local')
plt.tight_layout()

#%% [markdown]
# ## Horizontal Median Filter

#%%
chroma_smooth = scipy.ndimage.median_filter(chroma_filter, size=(1, 9))


plt.figure(figsize=(12, 4))

plt.subplot(2, 1, 1)
librosa.display.specshow(chroma_filter, y_axis='chroma')
plt.colorbar()
plt.ylabel('Non-local')

plt.subplot(2, 1, 2)
librosa.display.specshow(chroma_smooth, y_axis='chroma', x_axis='time')
plt.colorbar()
plt.ylabel('Median-filtered')
plt.tight_layout()

#%% [markdown]
# ## Before and After

#%%
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
librosa.display.specshow(librosa.amplitude_to_db(C, ref=np.max),
                         y_axis='cqt_note', bins_per_octave=12*3)
plt.colorbar()
plt.ylabel('CQT')
plt.subplot(3, 1, 2)
librosa.display.specshow(chroma_orig, y_axis='chroma')
plt.ylabel('Original')
plt.colorbar()
plt.subplot(3, 1, 3)
librosa.display.specshow(chroma_smooth, y_axis='chroma', x_axis='time')
plt.ylabel('Processed')
plt.colorbar()
plt.tight_layout()
plt.show()

#%% [markdown]
# # Applying chroma enchancement techniques to source files
#%% [markdown]
# ## Source1

#%%
# chroma_orig = librosa.feature.chroma_cqt(y=y, sr=sr)
# chroma_os = librosa.feature.chroma_cqt(y=y, sr=sr, bins_per_octave=12*3)

y_harm = librosa.effects.harmonic(y=y, margin=8)
chroma_os_harm = librosa.feature.chroma_cqt(y=y_harm, sr=sr, bins_per_octave=12*3)

chroma_filter = np.minimum(chroma_os_harm,
                           librosa.decompose.nn_filter(chroma_os_harm,
                                                       aggregate=np.median,
                                                       metric='cosine'))

chroma_smooth = scipy.ndimage.median_filter(chroma_filter, size=(1, 9))

plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
librosa.display.specshow(librosa.amplitude_to_db(C, ref=np.max),
                         y_axis='cqt_note', bins_per_octave=12*3)
plt.colorbar()
plt.ylabel('CQT')
plt.subplot(3, 1, 2)
librosa.display.specshow(chroma_orig, y_axis='chroma')
plt.ylabel('Original')
plt.colorbar()
plt.subplot(3, 1, 3)
librosa.display.specshow(chroma_smooth, y_axis='chroma', x_axis='time')
plt.ylabel('Processed')
plt.colorbar()
plt.tight_layout()
plt.show()

#%% [markdown]
# ## Source2

#%%
chroma_orig_2 = librosa.feature.chroma_cqt(y=y2, sr=sr2)

# And for comparison, we'll show the CQT matrix as well.
C2 = np.abs(librosa.cqt(y=y2, sr=sr2, bins_per_octave=12*3, n_bins=7*12*3))

y_harm_2 = librosa.effects.harmonic(y=y2, margin=8)
chroma_os_harm_2 = librosa.feature.chroma_cqt(
    y=y_harm_2, sr=sr2, bins_per_octave=12*3)

chroma_filter_2 = np.minimum(chroma_os_harm_2,
                             librosa.decompose.nn_filter(chroma_os_harm_2,
                                                         aggregate=np.median,
                                                         metric='cosine'))

chroma_smooth_2 = scipy.ndimage.median_filter(chroma_filter_2, size=(1, 9))

plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
librosa.display.specshow(librosa.amplitude_to_db(C2, ref=np.max),
                         y_axis='cqt_note', bins_per_octave=12*3)
plt.colorbar()
plt.ylabel('CQT')
plt.subplot(3, 1, 2)
librosa.display.specshow(chroma_orig_2, y_axis='chroma')
plt.ylabel('Original')
plt.colorbar()
plt.subplot(3, 1, 3)
librosa.display.specshow(chroma_smooth_2, y_axis='chroma', x_axis='time')
plt.ylabel('Processed')
plt.colorbar()

plt.tight_layout()
plt.show()

#%% [markdown]
# # Output comparisions for testing
#%% [markdown]
# ## Compare STFT and CQT

#%%
chromagram_stft = librosa.feature.chroma_stft(y=y, sr=sr)
chromagram_cqt = librosa.feature.chroma_cqt(y=y, sr=sr)


plt.figure(figsize=(12, 4))

plt.subplot(2, 1, 1)
librosa.display.specshow(chromagram_stft, y_axis='chroma')
plt.colorbar()
plt.ylabel('STFT')

plt.subplot(2, 1, 2)
librosa.display.specshow(chromagram_cqt, y_axis='chroma', x_axis='time')
plt.colorbar()
plt.ylabel('CQT')
plt.tight_layout()

#%% [markdown]
# ## Applying CENS features

#%%
chromagram_cens = librosa.feature.chroma_cens(y=y, sr=sr)


plt.figure(figsize=(12, 4))

plt.subplot(2, 1, 1)
librosa.display.specshow(chromagram_cqt, y_axis='chroma')
plt.colorbar()
plt.ylabel('Orig')

plt.subplot(2, 1, 2)
librosa.display.specshow(chromagram_cens, y_axis='chroma', x_axis='time')
plt.colorbar()
plt.ylabel('CENS')
plt.tight_layout()

#%% [markdown]
# ## Apply filter to CENS

#%%
# chroma_orig = librosa.feature.chroma_cqt(y=y, sr=sr)
# chroma_os = librosa.feature.chroma_cqt(y=y, sr=sr, bins_per_octave=12*3)

y_harm = librosa.effects.harmonic(y=y, margin=8)
chroma_os_harm = librosa.feature.chroma_cens(y=y_harm, sr=sr, bins_per_octave=12*3)

chroma_filter = np.minimum(chroma_os_harm,
                           librosa.decompose.nn_filter(chroma_os_harm,
                                                       aggregate=np.median,
                                                       metric='cosine'))

chroma_smooth = scipy.ndimage.median_filter(chroma_filter, size=(1, 9))

plt.figure(figsize=(12, 8))
plt.subplot(4, 1, 1)
librosa.display.specshow(librosa.amplitude_to_db(C, ref=np.max),
                         y_axis='cqt_note', bins_per_octave=12*3)
plt.colorbar()
plt.ylabel('CQT')
plt.subplot(4, 1, 2)
librosa.display.specshow(chroma_orig, y_axis='chroma')
plt.ylabel('Original')
plt.colorbar()
plt.subplot(4, 1, 3)
librosa.display.specshow(chromagram_cens, y_axis='chroma')
plt.ylabel('CENS')
plt.colorbar()
plt.subplot(4, 1, 4)
librosa.display.specshow(chroma_smooth, y_axis='chroma', x_axis='time')
plt.ylabel('Processed')
plt.colorbar()
plt.tight_layout()
plt.show()


#%%
plt.figure(figsize=(12,4))
librosa.display.specshow(chroma_smooth)
plt.savefig('output_images/source1_chromagram.png', dpi=100, bbox_inches='tight')
plt.tight_layout()
plt.show()
plt.figure(figsize=(12,4))
librosa.display.specshow(chroma_smooth_2)
plt.savefig('output_images/source2_chromagram.png', dpi=100, bbox_inches='tight')
plt.tight_layout()
plt.show()


#%%
get_ipython().run_line_magic('run', '-i imageDiff/image_diff.py --first ../visualMIDIcompare/output_images/source1_chromagram.png --second ../visualMIDIcompare/output_images/source2_chromagram.png')


#%%


