import os
import datetime
import json
import shutil

import GlobalVars as GV
import PictureOperations as POps
import NeatRun as NR

progConfigFile = "progConfig.json"

if __name__ == "__main__":
    GV.initVars()
    f = open(progConfigFile)
    progConfig = json.load(f)
    f.close()
    GV.runsDir = os.path.join(os.getcwd(), "runs", datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    try:
        os.makedirs(GV.runsDir)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise  # This was not a "directory exist" error..
            exit()

    # makes a copy of the current target img to the current runsDir
    shutil.copy(os.path.join(os.getcwd(), progConfig["targetImage"]["RGB"]), GV.runsDir)
    # makes a copy of the current neat config file to the current runsDir
    shutil.copy(os.path.join(os.getcwd(), progConfig["neatPythonConfig"]["configFile"]), GV.runsDir)
    # makes a copy of the current prog config file to the current runsDir
    shutil.copy(os.path.join(os.getcwd(), progConfigFile), GV.runsDir)

    GV.INPUT_BIAS = progConfig["neatPythonConfig"]["InputBias"]
    GV.MAX_GENS = progConfig["neatPythonConfig"]["MaxGens"]
    imgGreyScalePath=os.path.join(GV.runsDir, progConfig["targetImage"]["GreyScale"])
    GV.WIDTH, GV.HEIGHT = POps.imageToGreyScaleAndReturnDimensions(imgRGBpath=os.path.join(os.getcwd(), progConfig["targetImage"]["RGB"]), imgGreyScalePath=imgGreyScalePath)
    GV.CENTER = [int(GV.WIDTH/2), int(GV.HEIGHT/2)]
    GV.TARGET_GREYSCALE_ARRAY = POps.imageToArray(imgPath=imgGreyScalePath)
    NR.normD()
    if GV.MAX_D_th == 0:
        print('error. GV.MAX_D = 0')
        exit()
        quit()
    NR.run(config_file=progConfig["neatPythonConfig"]["configFile"])
    print("Min D = "+str(GV.MIN_D))
    print("Max D = "+str(GV.MAX_D))
    print(GV.MAX_D_th)
    
