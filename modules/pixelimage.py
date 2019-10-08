from PIL import Image
from modules import hexreader

class PixelImage():
    def __init__(self, inImage, *args, **kwargs):
        self.palettes = [x[:] for x in hexreader.palettes[:]]
        self.chosenPalette = 1
        self.originalImage = inImage
        self.pixelValues = list(inImage.getdata())
        self.dataLen = len(self.pixelValues)
        
        self.largestGroup = 1
        self.width = inImage.width
        self.height = inImage.height
        self.GetHighestGrouping()
        self.InitialGrouping()


        #self.area = self.image.width * self.image.height

        #if area > 100000:
        #    self.sizeGroup = 1
        #elif area > 50000:
        #    self.sizeGroup = 2
        #elif area > 10000:
        #    self.sizeGroup = 3
        #elif area > 5000:
        #    self.sizeGroup = 4
        #elif area > 1000:
        #    self.sizeGroup = 5
        #else:
        #    self.sizeGroup = 6

        

    def InitialGrouping(self):
        #group pixels inside rows, then rows and columns of size largestGrouping
        reduced = []
        tempGroup = []
        for i in range(0,self.height,self.largestGroup):
            for j in range(0,self.width, self.largestGroup):
                #reduced.append(self.pixelValues[i * self.width + j])
                tempGroup = []
                for x in range(0,self.largestGroup):
                    for y in range(0,self.largestGroup):
                        tempGroup.append(self.pixelValues[i * self.width + j + x + y])
                reduced.append(self.GetAverage(tempGroup))
        reduced = self.AdjustToPalette(reduced)
        im2 = Image.new('RGB', [int(self.width / self.largestGroup), int(self.height / self.largestGroup)])
        print(len(reduced))
        print(int(self.width / self.largestGroup))
        print(int(self.height / self.largestGroup))
        im2.putdata(reduced)
        im2.save('newTest.png')

        return
    
    def FindLines(self):
        return

    #returns single pixel made of the average of the square group
    def GetAverage(self, group):
        averagePixel = [0, 0, 0]
        
        for pixel in group:
            for color in range(len(pixel)):
                if color != 3:
                    averagePixel[color] += pixel[color]
        for i in range(len(averagePixel)):
            averagePixel[i] = int(averagePixel[i] / (self.largestGroup**2))
        return (averagePixel[0], averagePixel[1], averagePixel[2])

    #Finds the largest possible grouping size for pixelation
    def GetHighestGrouping(self):
        canGroup = True
        groupingValue = 2
        largestXGroup = 1
        largestYGroup = 1
        while canGroup:
            if not self.width % groupingValue:
                groupingValue *= 2
                largestXGroup *= 2
            else:
                canGroup = False
                groupingValue = 2
        canGroup = True
        while canGroup:
            if not self.height % groupingValue:
                groupingValue *= 2
                largestYGroup *= 2
            else:
                canGroup = False
        if largestXGroup <= largestYGroup:
            self.largestGroup = largestXGroup
        else:
            self.largestGroup = largestYGroup
        self.largestGroup = 4
        return

    def GetFlattenedImage(self):
        return [x for set in self.pixelValues for x in set]

    def AdjustToPalette(self, pixels):
        maxDif = 1000
        chosenColor = 0
        newPixels = []
        pixel = ()
        for pixel in pixels:
            #pixel = self.Contrast(pix)
            maxDif = 1000
            chosenColor = 0
            for color in self.palettes[self.chosenPalette]:
                tempDif = 0
                for valIndice in range(len(color)-1):
                    tempDif += abs(color[valIndice] - pixel[valIndice])
                if tempDif < maxDif:
                    maxDif = tempDif
                    chosenColor = color
            newPixels.append(chosenColor)
        return newPixels

    def Contrast(self, pixel):
        #average = self.GetAverage(self)
        newPixel = []
        for color in pixel:
            if color >= 120:
                diff = abs(255 - color)
                newPixel.append(int(255 - (3/4 * diff)))
            else:
                newPixel.append(int(color / 4))
        return (newPixel[0], newPixel[1], newPixel[2])

    #def GetAverage(self):
    #    average = []
    #    for pixel in self.pixelValues:
    #        for index in pixel:
    #            average[index] += pixel[index]
    #    for val in average:
    #        val /= len(self.pixelValues)
    #    return (average[0], average[1], average[2])

    #def AdjustToPalette(self):
    #    maxPixDif = 1000
    #    maxColorDif = 1000
    #    chosenColor = None
    #    newPixels = []
    #    pixel = ()
    #    for pix in self.pixelValues:
    #        pixel = self.Contrast(pix)
    #        maxPixDif = 1000
    #        maxColorDif = 1000
    #        chosenColor = None

    #        for color in pix:
    #            if 






    #        for color in self.palettes[self.chosenPalette]:
    #            tempDif = 0


                



    #            #for valIndice in range(len(color)):
    #            #    tempDif += abs(color[valIndice] - pixel[valIndice])
    #            #if tempDif < maxDif:
    #            #    chosenColor = color
    #        newPixels.append(chosenColor)
    #    return newPixels