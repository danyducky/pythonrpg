#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import sys
from Constants import *
from Hero import *
from Objects import *
# from Mob import *
import Mob
import Menu
from Walls import *
import random
import time
import Bot

pygame.init()


class Main():
    def __init__(self, background, Player, start_x, start_y, mobs):
        self.background = background
        self.caption = caption
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.Player = Player
        self.Player.x = start_x
        self.Player.y = start_y
        self.mobs = mobs
        self.fireballs = []
        self.objects = []
        self.bots = []
        self.len_of_demons = 2
        self.demon_dies = 0
        self.Main_loop()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == mphp_tick:
                self.Player.pool_actions()
            elif event.type == spawn_mob:
                self.spawn_mob()
            elif event.type == demon_move:
                for mob in self.mobs:
                    mob.rand_move()
                for bot in self.bots:
                    bot.rand_move()
            elif event.type == demon_remove:
                for mob in self.mobs:
                    mob.remove(self.mobs, mob)
            elif event.type == demon_delay:
                if self.len_of_demons < 5:
                    self.len_of_demons += 1
            elif event.type == demon_shoot:
                for mob in self.mobs:
                    if mob.status == True:
                        mob.shoot()
            elif event.type == Player_die:
                self.Player_die()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.pause()
                if event.key == pygame.K_SPACE:
                    if self.Player.status == True:
                        if self.Player.mp >= attack_manacost:
                            self.Player.mp -= attack_manacost
                            if self.Player.direction == up:
                                self.fireballs.append(
                                    fireball(self.Player.x + 7, self.Player.y + 10, self.Player.direction,
                                             fireball_speed))
                            elif self.Player.direction == down:
                                self.fireballs.append(
                                    fireball(self.Player.x + 7, self.Player.y + 25, self.Player.direction,
                                             fireball_speed))
                            elif self.Player.direction == left:
                                self.fireballs.append(
                                    fireball(self.Player.x - 10, self.Player.y + 10, self.Player.direction,
                                             fireball_speed))
                            else:
                                self.fireballs.append(
                                    fireball(self.Player.x + 10, self.Player.y + 10, self.Player.direction,
                                             fireball_speed))

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(pygame.image.load('data/spawn.png').convert_alpha(), (750, 550))
        self.screen.blit(hud_bar, (110, height - 60))
        if self.Player.dies >= 10:
            self.screen.blit(pygame.image.load('data/Boss.png').convert_alpha(), (750, 0))
        self.Player.render()
        self.Player.draw_score()
        self.Player.draw_hp_mp()
        self.Player.render_of_score()
        font = pygame.font.Font('data/font1.ttf', 18)
        fps = font.render('FPS: ' + str((round(self.clock.get_fps(), 2))), 1, (255, 255, 255))
        self.screen.blit(fps, (5, 5))


        for fireball in self.fireballs:
            fireball.move()
            fireball.render(fireball, self.fireballs)
            fireball.hud_contact(fireball, self.fireballs)
            for mob in self.mobs:
                mob.fireball_contact(self.mobs, mob, self.fireballs, fireball, self.Player)

            for wall in self.objects:
                wall.fireball_contact(fireball, self.fireballs)

        for bot in self.bots:
            bot.move()
            bot.render(self.Player)
            self.Player.contact_check_bot(bot, self.screen)

        for mob in self.mobs:
            mob.move()
            mob.draw_hp()
            mob.render_shot(self.objects, self.Player)
            mob.render()
            self.Player.contact_check(mob)
            for wall in self.objects:
                mob.contact_wall(wall)

        for wall in self.objects:
            wall.render()
            self.Player.contact_wall(wall)


        self.clock.tick(30)
        pygame.display.update()

    def pause(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return False

            mouse = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0] and 5 < mouse[0] < 75 and 76 < mouse[1] < 105:
                sys.exit()

            Menu.menu.background()
            Menu.menu.text('Morikov', 30, (15, 10), (255, 255, 255))
            Menu.menu.text('Vinokurov', 30, (15, 40), (255, 255, 255))
            Menu.menu.text('EXIT', 40, (15, 70), (255, 30, 0))
            self.clock.tick(15)
            pygame.display.update()

    def menu():
        import pygame
        import Menu
        import Hero
        pygame.init()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
            mouse = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0] and 340 < mouse[0] < 435 and 75 < mouse[1] < 115:
                Main(background, Hero.Player('ducky'), start_x, start_y, mobs=[])
            elif pygame.mouse.get_pressed()[0] and 5 < mouse[0] < 75 and 76 < mouse[1] < 105:
                sys.exit()
            elif pygame.mouse.get_pressed()[0] and 5 < mouse[0] < 100 and 125 < mouse[1] < 160:
                Menu.menu.text('W, A, S, D - КНОПКИ ПЕРЕДВИЖЕНИЯ', 15, (15, 200), (255, 255, 255))
                Menu.menu.text('1,2,3,4 -КНОПКИ ОТВЕЧАЮЩИЕ ЗА СВОСОБНОСТИ ,КОТОРЫЕ АКТИВНЫ ПРИ ОПРЕДЕЛЕННЫХ УСЛОВИЯХ', 15, (15, 230), (255, 255, 255))
                Menu.menu.text('SHIFT- КНОПКА ОТВЕЧАЮЩАЯ ЗА БЛИНК ПЕРСОНАЖА',15, (15, 260), (255, 255, 255))
                pygame.display.update()


            Menu.menu.background()
            Menu.menu.text('Morikov', 30, (15, 10), (255, 255, 255))
            Menu.menu.text('Vinokurov', 30, (15, 40), (255, 255, 255))
            Menu.menu.text('PLAY', 50, (350, 70), (0, 30, 0))
            Menu.menu.text('EXIT', 40, (15, 70), (255, 30, 0))
            Menu.menu.text('TRAINING', 40, (15, 120), (255, 255, 255))
            pygame.display.update()

    def wall_render(self):
        f = 800
        s = 50
        t = 540
        if len(self.objects) < 10:
            for i in range(10):
                self.objects.append(Wall(f, 508))
                f -= 40
            for i in range(9):
                self.objects.append(Wall(60, s))
                s += 40
            for i in range(10):
                self.objects.append(Wall(t, 410))
                t -= 40

    def spawn_mob(self):
        if 718 <= self.Player.x <= 800 and 545 <= self.Player.y <= 600:
            if len(self.mobs) < self.len_of_demons:
                self.mobs.append(Mob.Demon(random.randrange(200, 400, 50), random.randrange(200, 400, 50), random.randint(0, 3), 2))

    def spawn_bots(self):
        if len(self.bots)<1:
            self.bots.append(Bot.Milena(random.randrange(710, 750), random.randrange(400, 440), random.randint(0, 3), 2))


    def Player_die(self):
        if self.Player.status == False:
            while True:
                font = pygame.font.Font('data/font1.ttf', 40)
                Die = font.render('Press Space To Main Menu', 1, (255, 0, 0))
                Esc = font.render('ESC to EXIT', 1, (255, 0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            sys.exit()
                        elif event.key == pygame.K_SPACE:
                            Main.menu()
                            # self.Player.status = True
                            # self.Player.hp = max_hp
                            # self.Player.mp = max_mp
                            # self.Player.max_mp = max_mp
                            # self.Player.max_hp = max_hp
                            # self.Player.hp_regen = hp_regen
                            # self.Player.mp_regen = mp_regen
                            # self.Player.score = score
                            # Main(background, self.Player, start_x, start_y, mobs=[])
                self.screen.blit(Die, (240, 220))
                self.screen.blit(Esc, (330, 260))
                self.clock.tick(15)
                pygame.display.update()

    def NewLoc(self):
        if self.Player.dies >= 10:
            if 740 <= self.Player.x <= 800 and 0 <= self.Player.y <= 35:
                Location(background_2, self.Player, start_x, start_y - 80, mobs=[])

    def Main_loop(self):
        pygame.time.set_timer(mphp_tick, tick_time)
        pygame.time.set_timer(spawn_mob, spawn_time)
        pygame.time.set_timer(demon_move, demon_move_delay)
        pygame.time.set_timer(demon_remove, remove_time)
        pygame.time.set_timer(demon_shoot, shoot_delay)
        pygame.time.set_timer(demon_delay, demon_time_delay)
        pygame.time.set_timer(Player_die, Player_die_delay)

        while True:
            self.event()
            self.Player.move()
            self.render()
            self.spawn_bots()
            self.NewLoc()
            self.wall_render()


if __name__ == '__main__':
    Main.menu()


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
class Location(Main):
    def __init__(self, background, Player, start_x, start_y, mobs):
        Main.__init__(self, background, Player, start_x, start_y, mobs)

    def wall_render(self):
        if len(self.objects) < 15:
            self.objects.append(Tree(random.randrange(0, 750, 75), random.randrange(0, 400, 75)))

    def spawn_mob(self):
        if len(self.mobs) < self.len_of_demons - 1:
            self.mobs.append(
                Mob.Bog(random.randrange(200, 400, 50), random.randrange(200, 400, 50), random.randint(0, 3), 3))

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(hud_bar, (110, height - 60))
        self.screen.blit(pygame.image.load('data/Area.png').convert_alpha(), (750, 0))
        self.Player.render()
        self.Player.draw_score()
        self.Player.draw_hp_mp()
        self.Player.render_of_score()
        font = pygame.font.Font('data/font1.ttf', 18)
        fps = font.render('FPS: ' + str((round(self.clock.get_fps(), 2))), 1, (255, 255, 255))
        self.screen.blit(fps, (5, 5))

        for fireball in self.fireballs:
            fireball.move()
            fireball.render(fireball, self.fireballs)
            fireball.hud_contact(fireball, self.fireballs)

            for mob in self.mobs:
                mob.fireball_contact(self.mobs, mob, self.fireballs, fireball, self.Player)
                if mob.status == False:
                    while True:
                        for tree in self.objects:
                            tree.render()
                        font = pygame.font.Font('data/font1.ttf', 40)
                        Over = font.render('Game Over', 1, (255, 0, 0))
                        Esc = font.render('ESC to EXIT', 1, (255, 0, 0))
                        Space = font.render('SPACE to REgame', 1, (0, 0, 0))
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                sys.exit()
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    sys.exit()
                                elif event.key == pygame.K_SPACE:
                                    Main.menu()

                        self.screen.blit(Over, (350, 210))
                        self.screen.blit(Esc, (345, 250))
                        self.screen.blit(Space, (308, 290))
                        self.clock.tick(15)
                        pygame.display.update()

            for tree in self.objects:
                tree.fireball_contact(fireball, self.fireballs)

        for mob in self.mobs:
            mob.move()
            mob.draw_hp()
            mob.render_shot(self.objects, self.Player)
            mob.render()
            self.Player.contact_check(mob)
            for tree in self.objects:
                mob.contact_tree(tree)

        for tree in self.objects:
            tree.render()
            self.Player.contact_tree(tree)

        self.clock.tick(30)
        pygame.display.update()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == mphp_tick:
                self.Player.pool_actions()
            elif event.type == spawn_mob:
                self.spawn_mob()
            elif event.type == demon_move:
                for mob in self.mobs:
                    mob.rand_move()
            elif event.type == demon_remove:
                for mob in self.mobs:
                    mob.remove(self.mobs, mob)
            elif event.type == demon_shoot:
                for mob in self.mobs:
                    if mob.status == True:
                        mob.shoot()
            elif event.type == Player_die:
                self.Player_die()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.pause()
                if event.key == pygame.K_SPACE:
                    if self.Player.status == True:
                        if self.Player.mp >= attack_manacost:
                            self.Player.mp -= attack_manacost
                            if self.Player.direction == up:
                                self.fireballs.append(
                                    fireball(self.Player.x + 7, self.Player.y + 10, self.Player.direction,
                                             fireball_speed))
                            elif self.Player.direction == down:
                                self.fireballs.append(
                                    fireball(self.Player.x + 7, self.Player.y + 25, self.Player.direction,
                                             fireball_speed))
                            elif self.Player.direction == left:
                                self.fireballs.append(
                                    fireball(self.Player.x - 10, self.Player.y + 10, self.Player.direction,
                                             fireball_speed))
                            else:
                                self.fireballs.append(
                                    fireball(self.Player.x + 10, self.Player.y + 10, self.Player.direction,
                                             fireball_speed))

    def NewLoc(self):
        if 740 <= self.Player.x <= 800 and 0 <= self.Player.y <= 35:
            Main(background, self.Player, start_x, start_y, mobs)
