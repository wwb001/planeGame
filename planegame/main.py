import sys

import pygame

from constants import BG_IMG, BG_MUSIC, IMG_GAME_TITLE, IMG_GAME_START_BTN
from game.plane import OurPlane, SmallEnemyPlane
from game.war import PlaneWar


def main():
    """游戏入口，main方法"""
    war = PlaneWar()
    # 添加小型敌方飞机
    war.add_small_enemies(6)
    war.run_game()


if __name__ == '__main__':
    main()
