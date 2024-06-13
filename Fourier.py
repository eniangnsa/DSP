import numpy as np
from matplotlib import pyplot as plt
from scipy.io.wavfile import write
from scipy.fft import fft, fftfreq


SAMPLE_RATE = 44100
DURATION = 5

def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    y = np.sin((2 * np.pi) * frequencies)
    return x, y

# generate 2 hertz sine wave that last for 5 seconds
x, y = generate_sine_wave(2, SAMPLE_RATE, DURATION)
# plt.plot(x, y)
# plt.show()

# mixing audio
# to mix two audio, all we need to do is to add the two signals
_, nice_tone = generate_sine_wave(400, SAMPLE_RATE, DURATION)
_, noise_tone =  generate_sine_wave(4000, SAMPLE_RATE, DURATION)

noise_tone = noise_tone * 0.3

mixed_tone = nice_tone + noise_tone

# normalization
normalized_tone = np.int16((mixed_tone / mixed_tone.max()) * 32767)

# plt.plot(normalized_tone[:1000])
# plt.show()

# save our audio
# write("mysinewave.wav", SAMPLE_RATE, normalized_tone)

# Fourier Transforms
N = SAMPLE_RATE * DURATION

yf = fft(normalized_tone)
xf = fftfreq(N, 1/SAMPLE_RATE)

plt.plot(xf, np.abs(yf))
plt.show()