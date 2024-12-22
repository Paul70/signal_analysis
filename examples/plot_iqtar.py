import matplotlib.pyplot as plt
import numpy
import sys

sys.path.append("/home/paul/Projects/Software/signal_analysis")
from iq import iqtar

iq_tar_file = f"../tests/data/dummy.iq.tar"
iq_data = iqtar.IqTar(iq_tar_file)

samplerate = iq_data.getSampleRate()
sample_interval = 1 / samplerate
samples = iq_data.getNofSamples()
time = numpy.linspace(0, samples*sample_interval, samples)

# Plot I component
plt.subplot(2, 1, 1)
plt.plot(time, numpy.real(iq_data.getData()), label='I Signal Component')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

# Plot Q component
plt.subplot(2, 1, 2)
plt.plot(time, numpy.imag(iq_data.getData()), label='Q Signal Component')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()


# import matplotlib.pyplot as plt
# import numpy
# import RsWaveform


# class IQData:

#     # Constructor
#     def __init__(self, file = None):
#         self.meta_data = {
#             'clock': 0,
#             'scalingfactor': 0
#         }
#         self.data = []
#         if file is not None:
#             self.file_name = file
#             self.__extractDataFromFile()
#         else:
#             self.file_name = ""
#         pass

#     def setMetaData(self, clock, scaling):
#         self.meta_data["clock"] = clock
#         self.meta_data["scalingfactor"] = scaling
#         pass

#     def plotIqDataOverTime(self):
#         sample_frequency = self.meta_data["clock"]
#         sample_interval = 1 / sample_frequency
#         samples = len(self.data)
#         time = numpy.linspace(0, samples*sample_interval, samples)

#         # Plot I component
#         plt.subplot(4, 1, 1)
#         plt.plot(time, numpy.real(self.data), label='I Signal Component')
#         plt.xlabel('Time (s)')
#         plt.ylabel('Amplitude')
#         plt.legend()

#         # Plot Q component
#         plt.subplot(4, 1, 2)
#         #plt.plot(time, np.imag(iq_signal), label='Q Component')
#         plt.plot(time, numpy.imag(self.data), label='Q Signal Component')
#         plt.xlabel('Time (s)')
#         plt.ylabel('Amplitude')
#         plt.legend()

#         plt.subplot(4, 1, 3)
#         #plt.plot(time, np.real(iq_signal)+np.imag(iq_signal), label='Q Component')
#         plt.plot(time, numpy.real(self.data)+numpy.imag(self.data), label='IQ Signal')
#         plt.xlabel('Time (s)')
#         plt.ylabel('Amplitude')
#         plt.legend()

#         plt.subplot(4, 1, 4)
#         #plt.plot(time, np.real(iq_signal)+np.imag(iq_signal), label='Q Component')
#         plt.plot(time, numpy.imag(self.data)*numpy.imag(self.data)+numpy.real(self.data)*numpy.real(self.data), label='Magnitude')
#         plt.xlabel('Time (s)')
#         plt.ylabel('Magnitude')
#         plt.legend()

#         plt.tight_layout()
#         plt.show()
        

#     def __extractDataFromFile(self):
#         file_parts = self.file_name.split('.')
#         if "iq" in file_parts and "tar" in file_parts and file_parts[-1] == "tar":
#             # case RS iq.tar file
#             iqtar = RsWaveform.IqTar(file=self.file_name)
#             self.data = iqtar.data[0]
#             self.meta_data = iqtar.meta[0]
#         elif file_parts[-1] == "float32":
#             # case float32 binary data file
#             self.data = numpy.fromfile(self.file_name, dtype="float32")
#             self.data = self.data[0::2] + 1j*self.data[1::2]
#         pass


# iq = IQData("iqsamples.float32")
# iq.setMetaData(1000000, 1)
# iq.plotIqDataOverTime()



# All what is done here is based on the tutorial at
# https://witestlab.poly.edu/~ffund/el9043/labs/lab1.html

# 1. Reading complex data from iqsamples.float32 file
# - every value in an even array field starting with zero is the real part of 
#   a complex number
# - every value in an odd array field starting with one is the imag part of 
#   a complex number
# - first complex number:  data[0] +j*data[1]
# - second complex number: data[2] +j*data[3] and so on


#data = np.fromfile("iqsamples.float32", dtype="float32")
#data = data[0::2] + 1j*data[1::2]

# data contains now complex numbers

# 2. Plot spectogram of complex data
# NFFT = number of samples of Fourier Trafo
# FS = Sampling rate (Abtastrate)
#plt.specgram(data, NFFT=1024, Fs=1000000) 
#plt.title("PSD (power spectral density) of 'signal' loaded from file")
#plt.xlabel("Time")
#plt.ylabel("Frequency")
#plt.show()  # if you've done this right, you should see a fun surprise here!

# PSD plot of the same data
#plt.psd(data, NFFT=2048, Fs=1000)
#plt.title("PSD of 'signal' loaded from file")
#plt.show() 

# And let's look at it on the complex plan
# Note that showing *every* data point would be time- and processing-intensive
# so we'll just show a few
#plt.scatter(np.real(data[0:100000]), np.imag(data[0:100000]))
#plt.title("Constellation of the 'signal' loaded from file")
#plt.show() 


import RsWaveform
import datetime
import numpy as np

import matplotlib.pyplot as plt
# include scipy's signal processing functions


#filename = "tests/data/dummy.iq.tar"
filename = "Swp5-PartSweep1_0.iq.tar"
iqtar = RsWaveform.IqTar(file=filename)
# default loader + saver will be used which is
# currently a ".iqw" type
# This is the same as iqtar = RsWaveform.IqTar(load=RsWaveform.iqtar.Load,
# save=RsWaveform.iqtar.Save, file=filename)
#iqtar.data[0] >> array([0.2 + 0.4j, 0.6 + 0.8j])
#iqtar.meta[0] >> {
#    'clock': 10000.0,
#    'scalingfactor': 1.0,
#    'datatype': 'float32',
#    'format': 'complex',
#    'name': 'Python iq.tar Writer (iqdata.py)',
#    'comment': 'RS WaveForm, TheAE-RA',
#    "datetime": datetime.datetime(2023, 3, 1, 10, 19, 37, 43312),
#}
#print(iqtar.data[0])
#result = RsWaveform.calculate_rms(iqtar.data[0])
#print(result)


#plt.specgram(iqtar.data[0], NFFT=512, Fs=62500000.000000)
#plt.title("PSD of 'signal' loaded from file")
#plt.xlabel("Time")
#plt.ylabel("Frequency")
#plt.show()  # if you've done this right, you should see a fun surprise here!

print(len(iqtar.data[0]))

sample_frequency = 60362105.263158
sample_interval = 1 / sample_frequency
samples = 9489712  # from xml file
time = np.linspace(0, samples*sample_interval, samples)



# Computes the FFT of the signal using np.fft.fft(), and then shifts the zero-frequency 
# component to the center of the spectrum using np.fft.fftshift(). 
# This effectively reorganizes the spectrum so that it is centered at zero frequency.
# Zero frequency is the frequency of the real signal (DC component) 
signal_spectrum = np.fft.fftshift(np.fft.fft(iqtar.data[0]))

#freqs = np.fft.fftfreq(time.size, sample_interval)


#Calculates the frequencies corresponding to the FFT binaries using np.fft.fftfreq(). 
#The d parameter specifies the sample spacing (wie viel Zeit zwischen den samples ist), 
#which is sample_interval. Like before, np.fft.fftshift() is used to center the frequencies around zero.
freqs = np.fft.fftshift(np.fft.fftfreq(samples, d=sample_interval))



#After running this code, you'll have signal_spectrum, which represents the frequency-domain representation of the generated signal, and freqs, which contains the corresponding frequency values. You can then use Matplotlib to plot the spectrum if desired.



    #plt.figure(figsize=(10,5)): Creates a new figure with a specified size of 10 inches in width and 5 inches in height.

    #plt.plot(freqs / 1e3, np.abs(signal_spectrum)): Plots the absolute value of the signal spectrum against frequency. freqs / 1e3 scales the frequency values from Hz to kHz for better readability on the plot. np.abs(signal_spectrum) extracts the magnitude of the spectrum.

    #plt.xlim(70, 170): Sets the limits of the x-axis (frequency axis) from 70 kHz to 170 kHz.
plt.figure(figsize=(10,5))
plt.plot(freqs / 1e3, np.abs(signal_spectrum))  # in kHz
plt.xlim(5, 300)
plt.show()


# das hab ich in meinen datan
#signal_frequency = 78e3  # 78 kHz
#signal = np.exp(2j*np.pi*signal_frequency*time)
