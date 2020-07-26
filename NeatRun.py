import math
import neat
import numpy as np

import GlobalVars as GV
import PictureOperations as POps

def logOutput(out):
    if GV.MIN_OUTPUT == None or GV.MIN_OUTPUT > out:
        GV.MIN_OUTPUT = out
    if GV.MAX_OUTPUT == None or GV.MAX_OUTPUT < out:
        GV.MAX_OUTPUT = out


def logD(D):
    GV.ALL_D.append(D)
    if GV.MIN_D == None or GV.MIN_D > D:
        GV.MIN_D = D
    if GV.MAX_D == None or GV.MAX_D < D:
        GV.MAX_D = D

def MSE(genomeArr):
    totDiff = 0
    # Now calculate MSE...
    for y in range(GV.HEIGHT):
        for x in range(GV.WIDTH):
            diff = genomeArr[y][x] - GV.TARGET_GREYSCALE_ARRAY[y][x]
            sq = diff ** 2
            totDiff += sq
    totDiff = totDiff / (GV.HEIGHT*GV.WIDTH)
    mse = totDiff ** (0.5)
    return(mse)

def normD():
    # GV.MAX_D_th = max(GV.WIDTH - GV.CENTER[0], GV.HEIGHT - GV.CENTER[1])
    GV.MAX_D_th = float(((GV.WIDTH - GV.CENTER[0])**2 + (GV.HEIGHT - GV.CENTER[1])**2)**(0.5))

def calcNormD(x, y):
    diff_x = x - GV.CENTER[0]
    diff_y = y - GV.CENTER[1]
    diff = float(((diff_x ** 2) + (diff_y ** 2))**(0.5))
    return(float(diff/GV.MAX_D_th))

def eval_genomes(genomes, config):
    GV.CURR_GEN += 1
    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        imgArr = []
        for y in range(GV.HEIGHT):
            arrRow = []
            for x in range(GV.WIDTH):
                inputNormD = calcNormD(x, y)
                logD(inputNormD)
                spread = 1.0
                factor = 0.5
                fancy_x = (float(x - (factor * GV.WIDTH)) /
                           float(GV.WIDTH/2.0)) * spread
                fancy_y = (float(y - (factor * GV.HEIGHT)) /
                           float(GV.HEIGHT/2.0)) * spread
                inpu = (GV.INPUT_BIAS, inputNormD, fancy_x, fancy_y)
                # inpu = (GV.INPUT_BIAS, fancy_x, fancy_y)
                output = net.activate(inpu)
                logOutput(output[0])
                outputPix = int((255.0/spread) * (output[0]))
                arrRow.append(outputPix)
            imgArr.append(arrRow)
        POps.makeImage(arr=imgArr, genNum=GV.CURR_GEN, genomeNum=str(genome_id))
        # draw_net(config, genome, GV.CURR_GEN, genome_id)
        # draw_net(config, genome, GV.CURR_GEN, genome_id, node_names=GV.NODE_NAMES)
        genome.fitness = 0 - MSE(imgArr)

def run(config_file):
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation, config_file)
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    winner = p.run(eval_genomes, GV.MAX_GENS)
    print('\nBest genome:\n{!s}'.format(winner))