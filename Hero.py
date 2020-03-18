import pygame
from Constants import *
import Constants
from Main import *
import time
from Mob import *
import Menu
from Bot import *


class Player():
    def __init__(self, name):
        self.x = start_x
        self.y = start_y
        self.name = name
        self.image = player_imgs
        self.direction = down
        self.counter = image_counter
        self.speed = speed
        self.hp = max_hp
        self.mp = max_mp
        self.hp_regen = hp_regen
        self.mp_regen = mp_regen
        self.hud = image_hud
        self.imgs = hud_imgs
        self.max_mp = max_mp
        self.max_hp = max_hp
        self.hudx = hud_x
        self.hudy = hud_y
        self.status = True
        self.score = score
        self.len_of_dem = len_of_demons
        self.effect = effect
        self.seconds = 0
        self.ticks = 0
        self.effect_status = False
        self.effect_x = 0
        self.effect_y = 0
        self.effect_timer = 0
        self.effect_timer_sec = 0
        self.die = True
        self.dies = 0
        self.quest_delay = 0

    def render(self):
        key = pygame.key.get_pressed()
        if self.effect_status == True:
            self.effect_timer += 1
            self.effect_timer_sec = self.effect_timer // 25
            if self.effect_timer_sec < 1:
                screen.blit(self.effect, (self.effect_x, self.effect_y))
            else:
                self.effect_timer = 0
                self.effect_timer_sec = 0
                self.effect_status = False

        if self.status == True:
            self.quest_delay += 1
            screen.blit(self.image[self.direction][self.counter // 6], (self.x, self.y))
            screen.blit(self.imgs[self.direction][self.hud // 4], (self.hudx, self.hudy))
        else:
            screen.blit(pygame.image.load('data/demon_die.png'), (self.x, self.y))
            screen.blit(self.imgs[self.direction][self.hud // 4], (self.hudx, self.hudy))
            Constants.radiance = False
            Constants.damage = 40

    def render_of_score(self):
        key = pygame.key.get_pressed()
        self.ticks += 1
        self.seconds = self.ticks // 25

        screen.blit(pygame.image.load('data/hp1.png'), (110, 500))
        screen.blit(pygame.image.load('data/mp1.png'), (150, 500))

        if self.score >= 200 and self.mp >= 100:
            screen.blit(pygame.image.load('data/hp.png'), (110, 500))
        if self.score >= 200 and self.mp >= 100:
            screen.blit(pygame.image.load('data/mp.png'), (150, 500))
        if key[pygame.K_1]:
            if self.score >= 200 and self.mp >= 100:
                self.score -= 200
                self.mp -= 100
                self.hp_regen += 2
        if key[pygame.K_2]:
            if self.score >= 200 and self.mp >= 100:
                self.score -= 200
                self.mp -= 100
                self.mp_regen += 1
        screen.blit(pygame.image.load('data/hp2.png'), (190, 500))
        screen.blit(pygame.image.load('data/mp3.png'), (230, 500))
        if self.score >= 200 and self.mp >= 50:
            screen.blit(pygame.image.load('data/hp3.png'), (190, 500))
        if self.score >= 200 and self.mp >= 50:
            screen.blit(pygame.image.load('data/mp2.png'), (230, 500))
        if key[pygame.K_3]:
            if self.score >= 200 and self.mp >= 50:
                self.score -= 200
                self.mp -= 50
                self.max_hp += 20
        if key[pygame.K_4]:
            if self.score >= 200 and self.mp >= 50:
                self.score -= 200
                self.mp -= 50
                self.max_mp += 40
        if key[pygame.K_LSHIFT] and self.seconds > 5:
            self.ticks = 0
            self.seconds = 0
            self.effect_x = self.x
            self.effect_y = self.y
            if self.mp >= 35:
                self.effect_status = True
                if self.direction == up:
                    self.y -= 105
                    self.mp -= 35
                elif self.direction == down:
                    self.y += 105
                    self.mp -= 35
                elif self.direction == left:
                    self.x -= 105
                    self.mp -= 35
                elif self.direction == right:
                    self.x += 105
                    self.mp -= 35

    def move(self):
        key = pygame.key.get_pressed()
        if self.status == True:
            if key[pygame.K_d]:
                self.x += self.speed
                self.direction = right
                self.counter += 1
                self.hud += 1
                if self.counter == 36:
                    self.counter = 0
                if self.hud == 16:
                    self.hud = 0
            elif key[pygame.K_a]:
                self.x -= self.speed
                self.direction = left
                self.counter += 1
                self.hud += 1
                if self.counter == 36:
                    self.counter = 0
                if self.hud == 16:
                    self.hud = 0
            elif key[pygame.K_w]:
                self.y -= self.speed
                self.direction = up
                self.counter += 1
                self.hud += 1
                if self.counter == 36:
                    self.counter = 0
                if self.hud == 16:
                    self.hud = 0
            elif key[pygame.K_s]:
                self.y += self.speed
                self.direction = down
                self.counter += 1
                self.hud += 1
                if self.counter == 36:
                    self.counter = 0
                if self.hud == 16:
                    self.hud = 0

        if self.x <= 0:
            self.x = 0
        if self.x >= width - 32:
            self.x = width - 32
        if self.y <= 0:
            self.y = 0
        if self.y >= height - 48:
            self.y = height - 48

        if self.x < 310 and self.y >= height - 105:
            self.x = 310
        if self.y >= height - 111 and self.x < 310:
            self.y = height - 111

        if self.x < 110 and self.y > height - 150:
            self.x = 110
        if self.y > height - 155 and self.x < 110:
            self.y = height - 155

        if 100 < self.x < 300 and 450 < self.y < 520:
            self.y = 450
        if 100 < self.x < 310 and 465 < self.y < 505:
            self.x = 310

    def contact_check(self, mob):
        if mob.runstatus == False:
            if self.status == True:
                if mob.x - demon_width - 12 <= self.x < mob.x and mob.y - 30 < self.y <= mob.y + 40:
                    self.x = mob.x - demon_width - 12
                    self.hp -= 0.2
                    if self.hp <= 0:
                        self.hp = 0
                        self.hp_regen = 0
                        self.mp_regen = 0
                        self.status = False
                if mob.x - demon_width <= self.x < mob.x + 35 and mob.y - 30 < self.y <= mob.y + 40:
                    self.x = mob.x + 35
                    self.hp -= 0.2
                    if self.hp <= 0:
                        self.hp = 0
                        self.hp_regen = 0
                        self.mp_regen = 0
                        self.status = False
                if mob.x - demon_width + 10 <= self.x < mob.x + 25 and mob.y - 30 < self.y <= mob.y + 55:
                    self.y = mob.y + 55
                    self.hp -= 0.2
                    if self.hp <= 0:
                        self.hp = 0
                        self.hp_regen = 0
                        self.mp_regen = 0
                        self.status = False
                if mob.x - demon_width + 10 <= self.x < mob.x + 25 and mob.y - 55 < self.y <= mob.y + 50:
                    self.y = mob.y - 55
                    self.hp -= 0.2
                    if self.hp <= 0:
                        self.hp = 0
                        self.hp_regen = 0
                        self.mp_regen = 0
                        self.status = False

    def contact_check_bot(self, bot, screen, objects, fireballs, mobs, player):
        if self.status == True:
            if bot.status == True:
                if bot.x - demon_width - 12 <= self.x < bot.x and bot.y - 30 < self.y <= bot.y + 40:
                    bot.direction = 1
                    self.x = bot.x - demon_width - 12
                    bot.moves = [0,0,0,0]

                    if self.quest_delay > 120:
                        self.quest_message(screen, objects, fireballs, mobs, player)
                        self.quest_delay = 0

                if bot.x - demon_width <= self.x < bot.x + 35 and bot.y - 30 < self.y <= bot.y + 40:
                    bot.direction = 0
                    self.x = bot.x + 35
                    bot.moves = [0,0,0,0]

                    if self.quest_delay > 120:
                        self.quest_message(screen, objects, fireballs, mobs, player)
                        self.quest_delay = 0

                if bot.x - demon_width + 10 <= self.x < bot.x + 25 and bot.y - 30 < self.y <= bot.y + 55:
                    bot.direction = 3
                    self.y = bot.y + 55
                    bot.moves = [0,0,0,0]

                    if self.quest_delay > 120:
                        self.quest_message(screen, objects, fireballs, mobs, player)
                        self.quest_delay = 0

                if bot.x - demon_width + 10 <= self.x < bot.x + 25 and bot.y - 55 < self.y <= bot.y + 50:
                    bot.direction = 2
                    self.y = bot.y - 55
                    bot.moves = [0,0,0,0]

                    if self.quest_delay > 120:
                        self.quest_message(screen, objects, fireballs, mobs, player)
                        self.quest_delay = 0

    def quest_message(self, screen, objects, fireballs, mobs, player):
        font = pygame.font.Font('data/font1.ttf', 18)
        quest = font.render('Квест: убить 10 мобов', 1, (255,0,0))
        kills = font.render('Убито: ' + str(self.dies), 1, (255,0,0))
        ok = font.render('OK', 1, (200,200,200))


        for mob in mobs:
            mob.draw_hp()
            mob.render_shot(objects, player)
            mob.render()
        for wall in objects:
            wall.render()

        while True:
            key = pygame.key.get_pressed()
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            if key[pygame.K_SPACE]:
                return False
            elif key[pygame.K_ESCAPE]:
                return False
            if 387 < mouse[0] < 415 and 284 < mouse[1] < 297 and pygame.mouse.get_pressed()[0]:
                return False

            pygame.draw.rect(screen, (0,0,0), (290, 235, 220, 75))
            pygame.draw.line(screen, (255,255,255), (290, 235), (290+218, 235), 2)
            pygame.draw.line(screen, (255,255,255), (290, 235), (290, 235+75), 2)
            pygame.draw.line(screen, (255,255,255), (290+218, 235), (290+218, 235+75), 2)
            pygame.draw.line(screen, (255,255,255), (290, 235+75), (290+218, 235+75), 2)
            screen.blit(quest, (330, 243))
            screen.blit(kills, (377, 263))
            screen.blit(ok, (393, 284))
            pygame.display.update()

    def contact_check_reseiler(self, bot, screen):
        if self.status == True:
            if bot.x - demon_width - 12 <= self.x < bot.x and bot.y - 30 < self.y <= bot.y + 40:
                bot.direction = 1
                self.x = bot.x - demon_width - 12
                bot.moves = [0,0,0,0]

                if self.quest_delay > 120:
                    self.shop_message(screen)
                    self.quest_delay = 0

            if bot.x - demon_width <= self.x < bot.x + 35 and bot.y - 30 < self.y <= bot.y + 40:
                bot.direction = 0
                self.x = bot.x + 35
                bot.moves = [0,0,0,0]

                if self.quest_delay > 120:
                    self.shop_message(screen)
                    self.quest_delay = 0

            if bot.x - demon_width + 10 <= self.x < bot.x + 25 and bot.y - 30 < self.y <= bot.y + 55:
                bot.direction = 3
                self.y = bot.y + 55
                bot.moves = [0,0,0,0]

                if self.quest_delay > 120:
                    self.shop_message(screen)
                    self.quest_delay = 0

            if bot.x - demon_width + 10 <= self.x < bot.x + 25 and bot.y - 55 < self.y <= bot.y + 50:
                bot.direction = 2
                self.y = bot.y - 55
                bot.moves = [0,0,0,0]

                if self.quest_delay > 120:
                    self.shop_message(screen)
                    self.quest_delay = 0




    def shop_message(self, screen):
        font = pygame.font.Font('data/font1.ttf', 18)
        question = font.render('Желаете купить что-то?', 1, (200,200,200))
        YES = font.render('Да', 1, (0,255,0))
        NO = font.render('Нет', 1, (255,0,0))

        while True:
            key = pygame.key.get_pressed()
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            if key[pygame.K_ESCAPE]:
                return False

            if 454 < mouse[0] < 487 and 287 < mouse[1] < 305 and pygame.mouse.get_pressed()[0]: # button NO
                return False
            elif 317 < mouse[0] < 335 and 287 < mouse[1] < 305 and pygame.mouse.get_pressed()[0]:
                self.shop(screen)
                return False


            pygame.draw.rect(screen, (0,0,0), (290, 235, 220, 75))
            pygame.draw.line(screen, (255,255,255), (290, 235), (290+218, 235), 2)
            pygame.draw.line(screen, (255,255,255), (290, 235), (290, 235+75), 2)
            pygame.draw.line(screen, (255,255,255), (290+218, 235), (290+218, 235+75), 2)
            pygame.draw.line(screen, (255,255,255), (290, 235+75), (290+218, 235+75), 2)
            screen.blit(question, (320, 243))
            screen.blit(YES, (315, 284))
            screen.blit(NO, (460, 284))
            if self.score >= 250:
                score = font.render('Score:' + str(self.score), 1, (255,215,0))
                screen.blit(score, (368 ,265))
            else:
                score = font.render('Score:' + str(self.score), 1, (200,200,200))
                screen.blit(score, (368, 265))
            pygame.display.update()

    def shop(self, screen):
        pygame.time.wait(500)
        font = pygame.font.Font('data/font1.ttf', 22)
        shop = font.render('SHOP', 1, (200,200,200))
        exit = font.render('EXIT', 1, (255,0,0))
        haveit = font.render('Bought', 1, (255,0,0))
        sword_cost = font.render('Cost: 250', 1, (255,215,0))
        radiance_cost = font.render('Cost: 1000', 1, (255,215,0))
        while True:
            key = pygame.key.get_pressed()
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            if key[pygame.K_ESCAPE]:
                return False

            if 275 < mouse[0] < 375 and 250 < mouse[1] < 350 and pygame.mouse.get_pressed()[0] and self.score >= 250:
                Constants.damage += 10
                self.score -= 250
                return False
            elif 430 < mouse[0] < 530 and 250 < mouse[1] < 350 and pygame.mouse.get_pressed()[0] and self.score >= 1000 and Constants.radiance == False:
                Constants.radiance = True
                self.score -= 1000
                return False
            elif 384 < mouse[0] < 418 and 361 < mouse[1] < 381 and pygame.mouse.get_pressed()[0]:
                return False

            pygame.draw.rect(screen, (0,0,0), (200, 200, 400, 200))
            pygame.draw.line(screen, (255,255,255), (200, 200), (600, 200), 2)
            pygame.draw.line(screen, (255,255,255), (600, 200), (600, 400), 2)
            pygame.draw.line(screen, (255,255,255), (200, 400), (600, 400), 2)
            pygame.draw.line(screen, (255,255,255), (200, 200), (200, 400), 2)
            screen.blit(sword_cost, (288, 230))
            screen.blit(radiance_cost, (440 ,230))
            if self.score >= 250:
                screen.blit(pygame.image.load('data/Sword.png').convert_alpha(), (275, 250))
            else:
                screen.blit(pygame.image.load('data/sword1.png').convert_alpha(), (275, 250))
            if self.score >= 1000 and Constants.radiance == False:
                screen.blit(pygame.image.load('data/radiance.png').convert_alpha(), (430, 250))
            elif Constants.radiance == True:
                screen.blit(pygame.image.load('data/radiance1.png').convert_alpha(), (430, 250))
                screen.blit(haveit, (452, 288))
            else:
                screen.blit(pygame.image.load('data/radiance1.png').convert_alpha(), (430, 250))
            screen.blit(shop, (385, 213))
            screen.blit(exit, (385, 360))
            pygame.display.update()



    def contact_wall(self, wall):
        if wall.x - 30 < self.x < wall.x + 20 and wall.y - 40 < self.y < wall.y + 30:
            self.x = wall.x - 30
        if wall.x - 30 < self.x < wall.x + 40 and wall.y - 40 < self.y < wall.y + 30:
            self.x = wall.x + 40
        if wall.x - 30 < self.x < wall.x + 40 and wall.y - 40 < self.y < wall.y + 42:
            self.y = wall.y + 42
        if wall.x - 30 < self.x < wall.x + 40 and wall.y - 50 < self.y < wall.y + 42:
            self.y = wall.y - 50

    def contact_tree(self, tree):
        if tree.x - 33 < self.x < tree.x + 20 and tree.y - 42 < self.y < tree.y + 50:
            self.x = tree.x - 33
        if tree.x - 30 < self.x < tree.x + 26 and tree.y - 42 < self.y < tree.y + 50:
            self.x = tree.x + 26
        if tree.x - 30 < self.x < tree.x + 20 and tree.y - 40 < self.y < tree.y + 60:
            self.y = tree.y + 60
        if tree.x - 30 < self.x < tree.x + 20 and tree.y - 50 < self.y < tree.y + 42:
            self.y = tree.y - 50

    def draw_score(self):
        font_size = 20
        font = pygame.font.Font('data/font1.ttf', font_size)
        score_render = font.render(str(self.score), 1, (255, 215, 0))
        screen.blit(score_render, (5, 465))

    def draw_hp_mp(self):
        font_size = 18
        font = pygame.font.Font('data/font1.ttf', font_size)
        hp_render = font.render(
            'Health:' + ' ' + str(int(self.hp)) + '/' + str(self.max_hp) + '       +' + str(self.hp_regen), 1,
            (255, 0, 0))
        mp_render = font.render(
            'Mana:' + ' ' + str(int(self.mp)) + '/' + str(self.max_mp) + '          +' + str(self.mp_regen), 1,
            (0, 0, 255))
        name_render = font.render(self.name, 1, (255, 0, 0))
        screen.blit(hp_render, (130, height - 50))
        screen.blit(mp_render, (130, height - 30))
        screen.blit(name_render, (37, height - 106))

    def draw_status(self, screen):
        font = pygame.font.Font('data/font1.ttf', 14)
        damage = font.render('Damage: ' + str(Constants.damage), 1, (200,200,200))
        mouse = pygame.mouse.get_pos()

        if 10 < mouse[0] < 80 and 525 < mouse[1] < 590:
            pygame.draw.rect(screen, (0,0,0), (10, 522, 90, 67))
            if Constants.damage <= 99:
                screen.blit(damage, (24, 529))
            elif 100 <= Constants.damage <= 999:
                screen.blit(damage, (21, 529))
            else:
                screen.blit(damage, (19, 529))
            if Constants.radiance == True:
                screen.blit(radiance_true, (40, 549))
            else:
                screen.blit(radiance_false, (40, 549))


    def pool_actions(self):
        if self.mp < self.max_mp:
            self.mp += self.mp_regen
        if self.mp > self.max_mp:
            self.mp = self.max_mp
        if self.hp < self.max_hp:
            self.hp += self.hp_regen
        if self.hp > self.max_hp:
            self.hp = self.max_hp
