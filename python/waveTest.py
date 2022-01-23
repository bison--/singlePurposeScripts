import struct
import wave
import matplotlib.pyplot as plt

wave_file = wave.open('temp/2022-01-09_CyberCyberCyber_wip2.wav', 'r')

length = wave_file.getnframes()
print(length)
left_channel = []
for i in range(0, length):
    wave_data = wave_file.readframes(1)
    data = struct.unpack("<2h", wave_data)
    left_channel.append(data[0])
    #print(int(data[0]))
    #print(data)

#wavedata = wavefile.readframes(13)
#data = struct.unpack("<13h", wavedata)

plt.figure(1)
plt.title("Signal Wave")
plt.plot(left_channel)
plt.show()

