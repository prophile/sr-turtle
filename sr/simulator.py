from __future__ import division

import threading, time, pygame
from random import random

from arena import Arena
from display import Display
from markers import Token

class Simulator(object):
    def __init__(self, num_tokens=5, size=(8, 8), frames_per_second=30):
        self.arena = Arena()

        self._generate_tokens(num_tokens)

        self.display = Display(self.arena)

        self._loop_thread = threading.Thread(target=self._main_loop, args=(frames_per_second,))
        self._loop_thread.start()

    def _generate_tokens(self, num_tokens):
        for i in range(num_tokens):
            token = Token(self.arena, Token.SILVER, i)
            token.location = (random() * 4 - 2, random() * 4 - 2)
            self.arena.objects.append(token)

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
