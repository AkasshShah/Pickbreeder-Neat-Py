import os
from PIL import Image, ImageOps

import GlobalVars as GV

def imageToGreyScaleAndReturnDimensions(imgRGBpath, imgGreyScalePath):
    im = Image.open(imgRGBpath).convert('L')
    im.save(imgGreyScalePath)
    si = im.size
    im.close()
    return(si)

def makeImage(arr, genNum, genomeNum):
    '''
    arr = 2d list of tuples containing greyscale and alpha values. length should be width*height of the original target greyscale
    genNum = which generation is this image from <- for storing names
    which particular genome is this image being made for <- for storing names
    '''
    xy = (GV.WIDTH, GV.HEIGHT)
    string_path = os.path.join(GV.runsDir, "gens", "gen_" + str(genNum))
    string_pathFile = os.path.join(string_path, str(genomeNum) + ".png")
    if not os.path.exists(string_path):
        os.makedirs(string_path)
    newGrey = Image.new('L', xy)
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            newGrey.putpixel((x, y), arr[y][x])
    newGrey.save(string_pathFile)
    newGrey.close()

def imageToArray(imgPath):
    arr = []
    img = Image.open(imgPath)
    im = img.load()
    for y in range(GV.HEIGHT):
        arrRow = []
        for x in range(GV.WIDTH):
            arrRow.append(int(im[x, y]))
        arr.append(arrRow)
    img.close()
    return arr