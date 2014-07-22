from __future__ import division

import threading, time, pygame
from random import random

from arena import Arena
from display import Display
from markers import Token

from math import sin, cos, pi

class Simulator(object):
    def __init__(self, frames_per_second=30):
        self.arena = Arena()

        self._generate_tokens()

        self.display = Display(self.arena)

        self._loop_thread = threading.Thread(target=self._main_loop, args=(frames_per_second,))
        self._loop_thread.start()

    def _generate_tokens(self):
        NUM_TOKENS_EACH = 6
        OUTER_DISTANCE = 1.2
        INNER_DISTANCE = 0.6
        for i in xrange(NUM_TOKENS_EACH):
            angle = 2 * pi * i / NUM_TOKENS_EACH
            token_outer = Token(self.arena, Token.SILVER if i % 2 == 0 else Token.GOLD, i)
            token_outer.location = (OUTER_DISTANCE*sin(angle), OUTER_DISTANCE*cos(angle))
            self.arena.objects.append(token_outer)
            token_inner = Token(self.arena, Token.SILVER if i % 2 == 1 else Token.GOLD, i)
            token_inner.location = (INNER_DISTANCE*sin(angle), INNER_DISTANCE*cos(angle))
            self.arena.objects.append(token_inner)

    def _main_loop(self, frames_per_second):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            self.display.tick(1/frames_per_second)
            clock.tick(frames_per_second)

    def __del__(self):
        pygame.quit()
