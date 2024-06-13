Explanation of Aliasing
Aliasing is an effect that occurs when a signal is sampled at a rate that is insufficient to capture the changes in the signal, causing different signals to become indistinguishable (or aliases of one another) when sampled.

Why Aliasing Occurs
Aliasing occurs when the sampling rate is less than twice the highest frequency present in the signal. This threshold is known as the Nyquist rate. According to the Nyquist-Shannon sampling theorem, a continuous signal can be completely represented in its samples and perfectly reconstructed if it is sampled at a rate greater than twice its highest frequency.

In mathematical terms:

Sampling Rate<2×Highest Frequency

Example with Explanation
Let's use the script provided to illustrate and explain aliasing:

Generate Original Signal:

Frequencies: 50 Hz, 120 Hz, 300 Hz
Sample rate: 1000 Hz (well above the Nyquist rate for these frequencies)
Sampling at a Lower Rate:

New sample rate: 150 Hz (less than twice the highest frequency of 300 Hz)
This new sample rate is below the Nyquist rate for the highest frequency component (300 Hz). When sampled at this lower rate, the signal's high-frequency components (above 75 Hz, which is half of 150 Hz) get misrepresented, leading to aliasing.

Aliasing Effect
The aliasing effect can be seen when plotting the spectrum of the reconstructed signal. Frequencies above 75 Hz fold back into the lower frequencies, causing distortion and creating "aliases."

How to Remove Aliasing
To avoid aliasing, one can:

Increase the Sampling Rate: Ensure that the sampling rate is at least twice the highest frequency present in the signal.
Use an Anti-Aliasing Filter: Apply a low-pass filter before sampling to remove high-frequency components above the Nyquist rate.