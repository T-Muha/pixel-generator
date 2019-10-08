import os




def ReadPalette(filename):
    hexArray = open('./palettes/' + filename).readlines()
    fileContents = [x.strip() for x in hexArray]
    RGBValues = []
    for hex in fileContents:
        if hex[0] == 'F':
            print(HexToRGB(hex))
            RGBValues.append(HexToRGB(hex))
    return RGBValues

def HexToRGB(hex):
    return tuple(int(hex[i:i+2], 16) for i in (2, 4, 6))

palettes = []

for filename in os.listdir('./palettes/'):
    palettes.append(ReadPalette(filename))