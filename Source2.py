import thinkdsp as dsp
import numpy
import scipy
import matplotlib

signal = dsp.TriangleSignal(freq = 1000, amp = 1.0, offset = 0)
signal2 = dsp.SinSignal(freq = 440, amp = 1.0, offset = 0)
signal3 = dsp.SquareSignal(freq = 440, amp = 1.0, offset = 0)

period_sin = signal2.period

wave_triangle = signal.make_wave(duration = 1, start = 0, framerate = 11025)
wave_sin = signal2.make_wave(duration= 0.0125, start = 0, framerate = 11025)
wave_square = signal3.make_wave(duration = 0.0125, start=0, framerate=11025)

mix = signal + signal2
wave_mix = mix.make_wave(duration = 0.0125, start = 0, framerate = 11025)

#wave_triangle.plot()
#matplotlib.pyplot.show()
#wave_sin.plot()
#matplotlib.pyplot.show()

wave_triangle.plot()
matplotlib.pyplot.show()

wave_triangle.write(filename = "triangle.wav")
spectrum = wave_triangle.make_spectrum()
spectrum.plot()
matplotlib.pyplot.show()

print(spectrum.hs[0])
spectrum.hs[0] = 100

spectrum.plot()
matplotlib.pyplot.show()

def spetr_test(spectrum):
    spectrum.hs[0] = 0
    i = 0
    for i in range(len(spectrum.hs)):
        spectrum.hs[i] = spectrum.hs[i] / spectrum.fs[i]
        #print(spectrum.hs[i], " ", spectrum.fs[i])
    return spectrum

spectrum1 = spetr_test(spectrum)
spectrum1.plot()
matplotlib.pyplot.show()

spectrum1_wave = spectrum1.make_wave()

spectrum1_wave.plot()
matplotlib.pyplot.show()

spectrum1_wave.write(filename= "triangle2.wav")