#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        if self.name == 'Enemy3':
            self.moveY()
            self.rect.centerx -= ENTITY_SPEED['Enemy3']
        else:
            self.rect.centerx -= ENTITY_SPEED[self.name]

    def moveY(self):
        self.rect.centery += ENTITY_SPEED['Enemy3']
        RETURN3 = True

        if self.rect.top > 0 or RETURN3 == True:
            self.rect.centery -= ENTITY_SPEED['Enemy3']
        else:
            RETURN3 = False
            if RETURN3 == False:
                self.rect.centery += ENTITY_SPEED['Enemy3']
                if self.rect.bottom > WIN_HEIGHT:
                    RETURN3 = True

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
