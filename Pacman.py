from Classes import *
import pygame
import time
import numpy as np
import sys
import argparse

'''credits: http://ai.berkeley.edu/reinforcement.html; https://github.com/gauravmittal1995/Pyman'''
'''mode: manual, QLearning, SARSA, ApproxQ'''
'''gridName: miniGrid, xsmallGrid, smallGrid, mediumGrid, largeGrid'''


'''only manual and ApproxQ work for capsule atm'''


def getParams():
    parser = argparse.ArgumentParser()

    # hyper-params:
    parser.add_argument("-epsilon", action="store", type=float, default=0.05)
    parser.add_argument("-gamma", action="store", type=float, default=0.99)
    parser.add_argument("-lr", action="store", type=float, default=0.01)
    # train/test params
    parser.add_argument("-trainEpi", action="store", type=int, default=100)
    parser.add_argument("-trainDelay", action="store", type=int, default=1)
    parser.add_argument("-testEpi", action="store", type=int, default=100)
    parser.add_argument("-testDelay", action="store", type=int, default=55)
    # game mode/map
    parser.add_argument("-mode", action="store", type=str, default="ApproxQ")
    parser.add_argument("-grid", action="store", type=str, default="largeGrid")

    params = parser.parse_args()
    return params


if __name__ == "__main__" or __name__ == "Pacman":
    pygame.init()

    params = getParams()

    # game = Game(epsilon=0.05, gamma=0.99, lr=0.01,
    #             trainEpi=100, trainDelay=1, testEpi=1000, testDelay=80,
    #             mode="ApproxQ", gridName="largeGrid")

    game = Game(epsilon=params.epsilon, gamma=params.gamma, lr=params.lr,
                trainEpi=params.trainEpi, trainDelay=params.trainDelay,
                testEpi=params.testEpi, testDelay=params.testDelay,
                mode=params.mode, gridName=params.grid)

    pacman = Pacman(game)
    # ghosts = [Ghost(game, "GREEN")]
    ghosts = [Ghost(game, "GREEN"), Ghost(game, "RED")]
    # ghosts = [Ghost(game, "GREEN"), Ghost(game, "RED"), Ghost(game, "PINK")]

    run = Run(game, pacman, ghosts)
    run.flow()

    # a = run.MCST_Train(mode=True)

    # print(a)



