import random

import cocos
import pyglet
from cocos.actions import *

from game.visualizer.global_stats import GlobalStats


class FireLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        super().__init__()
        self.display = display_size
        self.info = turn_info
        self.images = assets

        global_stats = GlobalStats()

        rates = -1
        # Check the rate
        try:
            for key, item in self.info['rates'].items():
                if key is "0":
                    rates = item
        except:
            print("YEET")

        # If the rate is 0, that means the Fire happened, so draw to screen
        if rates == 0:
            for n in range(random.randint(0,19)):
                section1_x = random.randint(self.display[0] / 2, self.display[0] / 2 + 120)
                section1_y = random.randint(self.display[1]/2 - 8, self.display[1]/2 + 160)

                self.fire = self.images["fire"][n]
                self.fire_x = random.randint(section1_x, section1_x)
                self.fire_y = random.randint(section1_y, section1_y)
                self.fire.position = (self.fire_x, self.fire_y)
                self.add(self.fire)


class TornadoLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        super().__init__()
        self.display = display_size
        self.info = turn_info
        self.images = assets

        global_stats = GlobalStats()

        rates = -1
        # Check the rate
        try:
            for key, item in self.info['rates'].items():
                if key is "1":
                    rates = item
        except:
            print("YEET")

        # If the rate is 0, that means the tornado happened, so draw to screen
        if rates == 0:
            self.tornado = self.images['tornado']
            self.tornado_x = 0
            self.tornado_y = int(self.display[1] / 2)

            self.tornado.position = (self.tornado_x, self.tornado_y)
            self.tornado.do(MoveBy((self.display[0], 0), global_stats.disaster_turn_time * global_stats.turn_speed))
            self.add(self.tornado)


class BlizzardLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        super().__init__()
        self.display = display_size
        self.info = turn_info
        self.images = assets

        rates = -1
        # Check the rate
        try:
            for key, item in self.info['rates'].items():
                if key is "2":
                    rates = item
        except:
            print("YEET")

        # If the rate is 0, that means the blizzard happened, so draw to screen
        if rates == 0:
            self.blizzard = self.images['blizzard']
            self.blizzard_x = int(self.display[0] / 2)
            self.blizzard_y = int((self.display[1] / 2) + 64)

            self.blizzard.position = (self.blizzard_x, self.blizzard_y)
            self.add(self.blizzard)


class EarthquakeLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        super().__init__()
        self.display = display_size
        self.info = turn_info
        self.images = assets

        rates = -1
        # Check the rate
        try:
            for key, item in self.info['rates'].items():
                if key is "3":
                    rates = item
        except:
            print("YEET")

        # If the rate is 0, that means the earthquake happened, so draw to screen
        if rates == 0:
            self.earthquake = self.images['earthquake']
            self.earthquake_x = int(self.display[0] / 2)
            self.earthquake_y = 104

            self.earthquake.position = (self.earthquake_x, self.earthquake_y)
            self.add(self.earthquake)


class MonsterLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        super().__init__()
        self.display = display_size
        self.info = turn_info
        self.images = assets

        global_stats = GlobalStats()

        rates = -1
        # Check the rate
        try:
            for key, item in self.info['rates'].items():
                if key is "4":
                    rates = item
        except:
            print("YEET")

        # If the rate is 0, that means the monster happened, so draw to screen
        if rates == 0:
            self.monster = self.images['monster']
            self.monster_x = int(self.display[0] / 4)
            self.monster_y = int(self.display[1])

            self.monster.position = (self.monster_x, self.monster_y)
            self.monster.do(MoveBy((self.monster_x, -400), global_stats.disaster_turn_time * global_stats.turn_speed))

            self.add(self.monster)


class UFOLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        super().__init__()
        self.display = display_size
        self.info = turn_info
        self.images = assets

        global_stats = GlobalStats()

        rates = -1
        # Check the rate
        try:
            for key, item in self.info['rates'].items():
                if key is "5":
                    rates = item
        except:
            print("YEET")

        # If the rate is 0, that means the ufo happened, so draw to screen
        if rates == 0:
            self.ufo = self.images['ufo']
            self.ufo_x = self.display[0]/2
            self.ufo_y = 400
            self.ufo.position = (self.ufo_x, self.ufo_y)
            # self.ufo.do(MoveBy((self.display[0], 0), global_stats.disaster_turn_time * global_stats.turn_speed))

            self.add(self.ufo)
