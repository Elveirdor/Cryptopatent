import numpy as np
import pyaudio
import matplotlib.pyplot as plt

# Define parameters
frequency = 440  # Hz, waves per second
duration = 1  # second
volume = 0.5  # range [0.0, 1.0]
fs = 44100  # sampling rate, Hz, must be integer
duration_s = 1  # in seconds, may be float

# Generate array with seconds*sample_rate steps, ranging from 0 to seconds
t = np.linspace(0, duration, int(fs * duration), False)

# Generate a sine wave
note = np.sin(frequency * t * 2 * np.pi)

# Ensure that highest value is in 16-bit range
audio = note * (2**15 - 1) / np.max(np.abs(note))
audio = audio.astype(np.int16)

# Start pyaudio
p = pyaudio.PyAudio()

# Open stream
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=fs,
                output=True)

# Play sound
stream.write(audio)

# Close and terminate everything properly
stream.stop_stream()
stream.close()
p.terminate()

# Plot the sound wave
plt.plot(t, note)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sound Wave')
plt.show()
