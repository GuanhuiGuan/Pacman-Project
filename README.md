# Pacman-Project

A Pacman environment is developed and algorithms like Approximate Q Learning are implemented. This version of Pacman and Approximate Q Learning realization are my works. 

Teammates: Guanhui Guan(me), Jiahao Li, Jingyi Qian, Yuekun Guo, Qiao Zhang

### Refs:

http://ai.berkeley.edu/reinforcement.html

https://github.com/gauravmittal1995/Pyman


## HOW TO PLAY
Windows:

1. Requirement: Python3 and following packages(pygame, numpy, argparse, matplotlib)

2. Open cmd and go to the directory, run >python pacman.py
   , and then the game will run in default settings

3. Can tweak parameters from command line, e.g. >python pacman.py -epsilon 0.08 -trainEpi 70

4. RL algorithm hyper parameters: -epsilon -gamma, -lr
   
   training/testing parameters(stand for training episodes and the delay between two frames): -trainEpi -trainDelay -testEpi -testDelay
   
   game settings: -mode(choose from "manual, QLearning, SARSA, ApproxQ")
		  -grid(choose from "miniGrid, xsmallGrid, smallGrid, mediumGrid, largeGrid")
