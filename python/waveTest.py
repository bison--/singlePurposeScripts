import struct
import wave
import matplotlib.pyplot as plt


def simple_chart(_wave_file):
    left_channel = []
    for i in range(0, length):
        wave_data = wave_file.readframes(1)
        data = struct.unpack("<2h", wave_data)
        left_channel.append(data[0])
        # print(int(data[0]))
        # print(data)

    # wavedata = wavefile.readframes(13)
    # data = struct.unpack("<13h", wavedata)

    plt.figure(1)
    plt.title("Signal Wave")
    plt.plot(left_channel)
    plt.show()

def complex(_wave_file):
    wave_data = wave_file.readframes(length)
    unpacked_data = []
    # data = struct.unpack("<2h", wave_data)
    window_size = 4
    for i in range(len(wave_data) - window_size + 1):
        data = struct.unpack("<2h", wave_data[i: i + window_size])
        unpacked_data.append(data)
        # print(data)

    frame_rate = wave_file.getframerate()

    print('FPS:', frame_rate)
    print('LENGTH:', length / frame_rate)
    print('LENGTH:', len(wave_data) / frame_rate)
    print('LENGTH:', len(unpacked_data) / 4 / frame_rate)
    print('data:', wave_data[0], unpacked_data[0])

wave_file = wave.open('temp/2022-01-09_CyberCyberCyber_wip2.wav', 'r')

length = wave_file.getnframes()
print('number frames:', length)

simple_chart(wave_file)
#complex(wave_file)

