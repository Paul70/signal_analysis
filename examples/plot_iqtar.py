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