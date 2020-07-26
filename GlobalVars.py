def initVars():
    global CURR_GEN
    global TARGET_GREYSCALE_ARRAY
    global MIN_D
    global MAX_D
    global MAX_D_th
    global ALL_D
    global NODE_NAMES
    global WIDTH
    global HEIGHT
    global CENTER
    global INPUT_BIAS
    global runsDir
    global MAX_GENS
    global MIN_OUTPUT
    global MAX_OUTPUT

    CURR_GEN = -1
    TARGET_GREYSCALE_ARRAY = []
    MIN_D = None
    MAX_D = None
    MAX_D_th = 0.0
    ALL_D = []
    NODE_NAMES = {0: "Out", -1: "Bias", -2: "Dist", -3: "fancy_x", -4: "fancy_y"}
    WIDTH = 0
    HEIGHT = 0
    CENTER = [0, 0]
    INPUT_BIAS = 0
    runsDir = ""
    MAX_GENS = 2
    MIN_OUTPUT = None
    MAX_OUTPUT = None