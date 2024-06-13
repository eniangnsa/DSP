import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Function to plot signal and its spectrum
def plot_signal_and_spectrum(t, signal, title):
    # Plot signal
    plt.figure(figsize=(14, 5))
    plt.subplot(1, 2, 1)
    plt.plot(t, signal)
    plt.title(f'{title} - Signal')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    
    # Compute and plot spectrum
    N = len(signal)
    yf = fft(signal)
    xf = fftfreq(N, t[1] - t[0])
    plt.subplot(1, 2, 2)
    plt.plot(xf[:N//2], 2.0/N * np.abs(yf[:N//2]))
    plt.title(f'{title} - Spectrum')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.show()

# Generate original signal
def generate_signal(frequencies, t):
    signal = np.zeros_like(t)
    for f in frequencies:
        signal += np.sin(2 * np.pi * f * t)
    return signal

# Sampling and reconstruction
def sample_and_reconstruct(signal, t, sample_rate):
    sample_interval = int(1 / sample_rate / (t[1] - t[0]))
    sampled_signal = signal[::sample_interval]
    sampled_t = t[::sample_interval]
    
    # Zero-padding for reconstruction
    reconstructed_signal = np.zeros_like(t)
    reconstructed_signal[:len(sampled_signal)] = sampled_signal
    return reconstructed_signal, sampled_t

# Parameters
frequencies = [50, 120, 300]
T = 1.0     # seconds
sample_rate_original = 1000 # Hz
sample_rate_new = 150       # Hz

# Time vector
t = np.linspace(0, T, int(T * sample_rate_original), endpoint=False)

# Generate and plot original signal
original_signal = generate_signal(frequencies, t)
plot_signal_and_spectrum(t, original_signal, 'Original Signal')

# Sample and reconstruct
reconstructed_signal, sampled_t = sample_and_reconstruct(original_signal, t, sample_rate_new)
plot_signal_and_spectrum(t, reconstructed_signal, 'Reconstructed Signal')

# Compare original and reconstructed spectra
plt.figure(figsize=(14, 5))
N = len(original_signal)
yf_original = fft(original_signal)
yf_reconstructed = fft(reconstructed_signal)
xf = fftfreq(N, t[1] - t[0])

plt.plot(xf[:N//2], 2.0/N * np.abs(yf_original[:N//2]), label='Original Signal Spectrum')
plt.plot(xf[:N//2], 2.0/N * np.abs(yf_reconstructed[:N//2]), label='Reconstructed Signal Spectrum', linestyle='--')
plt.title('Comparison of Spectra')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()
plt.show()
