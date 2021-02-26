# Simplified BSD License, Copyright 2011 Al Sweigart
import sys
import os
sys.path.append(os.path.abspath('..'))

import pygcurse, pygame
from pygame.locals import *
win = pygcurse.PygcurseWindow(40, 25)
win.autoblit = True


inputBox = pygcurse.PygcurseInput(win, '> ', 0, 0, 20)

while True:
    for event in pygame.event.get():

        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            inputBox.sendkeyevent(event.key)

