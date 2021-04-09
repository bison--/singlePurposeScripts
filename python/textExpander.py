import random

text = """
asobo-aicraft-pipistrel-0.1.33.fspackage
bf-texture-synth-lib
fs-base
fs-base-achievements
fs-base-base-aircraft-common
fs-base-aicraft-icao
fs-base-ai-traffic
fs-base-effects
fs-base-ingamepanels-atc
fs-base-ingamepanels-camera
fs-base-ingamepanels-checklist
fs-base-ingamepanels-controls
fs-base-ingamepanels-copilot
fs-base-ingamepanels-fuel
fs-base-ingamepanels-navlog
fs-base-ingamepanels-objectives
fs-base-ingamepanels-teleport
fs-base-ingamepanels-vfrmap
fs-base-ingamepanels-weather
fs-base-marketplace
fs-base-material-lib
fs-base-soundbanks
fs-base-ui-pages
fs-base-videos
pc-fs-base-bigfiles
fs-base-cgl-0.1.21.fspackage
fs-base-cgl-0.1.21.fspackage.002
fs-base-cgl-0.1.21.fspackage.003
fs-base-cgl-0.1.21.fspackage.004
fs-base-cgl-0.1.21.fspackage.005
"""


lines = text.split('\n')

cnt = 0
dots = 0
for line in lines:
    for i in range(0, 101, random.choice([20, 30, 40])):
        progress = i
        print("[{0}%] Downloading {1} {2}".format(progress, line, '.'*dots))
        cnt += 1

        dots += 1
        if dots > 3:
            dots = 0

    for i in range(dots, 4):
        print("Decompressing {0}".format(line), '.'*i)
        cnt += 1
    dots = 0

print('total lines:', cnt)
