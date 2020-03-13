import pygame
score=0
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
background = pygame.image.load('data/unknown.jpg').convert_alpha()
background = pygame.transform.scale(background, (width, height))
caption = pygame.display.set_caption('Invoker: Beginning')
pygame.display.set_icon(pygame.image.load('data/icon.png').convert_alpha())
hud_bar = pygame.image.load('data/HudBar.png').convert_alpha()
background_2 = pygame.image.load('data/NewBackground.jpg').convert_alpha()
background_2 = pygame.transform.scale(background_2, (width, height))
hud_x = 0
hud_y = 600 - 110
start_x = 605
start_y = 552
MainPlayer = ('ducky', start_x, start_y)
player_imgs = [
    [pygame.image.load('data/right.png').convert_alpha(), pygame.image.load('data/right1.png').convert_alpha(), pygame.image.load('data/right2.png').convert_alpha(),
     pygame.image.load('data/right3.png').convert_alpha(), pygame.image.load('data/right.png').convert_alpha(), pygame.image.load('data/right1.png').convert_alpha()],
    [pygame.image.load('data/left.png').convert_alpha(), pygame.image.load('data/left1.png').convert_alpha(), pygame.image.load('data/left2.png').convert_alpha(),
     pygame.image.load('data/left3.png').convert_alpha(), pygame.image.load('data/left.png').convert_alpha(), pygame.image.load('data/left1.png').convert_alpha()],
    [pygame.image.load('data/up.png').convert_alpha(), pygame.image.load('data/up1.png').convert_alpha(), pygame.image.load('data/up2.png').convert_alpha(),
     pygame.image.load('data/up3.png').convert_alpha(), pygame.image.load('data/up.png').convert_alpha(), pygame.image.load('data/up1.png').convert_alpha()],
    [pygame.image.load('data/down.png').convert_alpha(), pygame.image.load('data/down1.png').convert_alpha(), pygame.image.load('data/down2.png').convert_alpha(),
     pygame.image.load('data/down3.png').convert_alpha(), pygame.image.load('data/down.png').convert_alpha(), pygame.image.load('data/down1.png').convert_alpha()]]

hud_imgs = [
    [pygame.image.load('data/rights.png').convert_alpha(), pygame.image.load('data/rights1.png').convert_alpha(), pygame.image.load('data/rights2.png').convert_alpha(),
     pygame.image.load('data/rights3.png').convert_alpha()],
    [pygame.image.load('data/lefts.png').convert_alpha(), pygame.image.load('data/lefts1.png').convert_alpha(), pygame.image.load('data/lefts2.png').convert_alpha(),
     pygame.image.load('data/lefts3.png').convert_alpha()],
    [pygame.image.load('data/ups.png').convert_alpha(), pygame.image.load('data/ups1.png').convert_alpha(), pygame.image.load('data/ups2.png').convert_alpha(),
     pygame.image.load('data/ups3.png').convert_alpha()],
    [pygame.image.load('data/downs.png').convert_alpha(), pygame.image.load('data/downs1.png').convert_alpha(), pygame.image.load('data/downs2.png').convert_alpha(),
     pygame.image.load('data/downs3.png').convert_alpha()]]
# 32 48
image_counter = 0
image_hud = 0
right = 0
left = 1
up = 2
down = 3

speed = 5

max_hp = 100
max_mp = 60
attack_manacost = 10

mp_regen = 2
hp_regen = 1
demon_hp = 200
len_of_demons=2
mphp_tick = pygame.USEREVENT + 1
tick_time = 1000
spawn_mob = pygame.USEREVENT + 2
spawn_time = 600
demon_move = pygame.USEREVENT + 3
demon_move_delay = 2000
demon_remove = pygame.USEREVENT + 4
remove_time = 6000
demon_shoot = pygame.USEREVENT + 5
shoot_delay = 1200
demon_delay = pygame.USEREVENT + 6
demon_time_delay = 15000
#draw_effect = pygame.USEREVENT + 7
#effect_delay = 1500
Player_die = pygame.USEREVENT + 0
Player_die_delay = 1500



fireball_imgs = [pygame.image.load('data/ball1.png').convert_alpha(), pygame.image.load('data/ball2.png').convert_alpha(),
                 pygame.image.load('data/ball3.png').convert_alpha(), pygame.image.load('data/ball4.png').convert_alpha()]
fireball_speed = 7

fire = [pygame.image.load('data/fire.png').convert_alpha(), pygame.image.load('data/fire2.png').convert_alpha(),
        pygame.image.load('data/fire1.png').convert_alpha(), pygame.image.load('data/fire3.png').convert_alpha()]
fire_speed = 11

x = 500
y = 300
mobs = []
bots=[]

demon_imgs = [[pygame.image.load('data/right_mob1.png').convert_alpha(), pygame.image.load('data/right_mob2.png').convert_alpha(),
                 pygame.image.load('data/right_mob3.png').convert_alpha(), pygame.image.load('data/right_mob4.png').convert_alpha(),
                 pygame.image.load('data/right_mob1.png').convert_alpha(), pygame.image.load('data/right_mob2.png').convert_alpha()],
                [pygame.image.load('data/left_mob1.png').convert_alpha(), pygame.image.load('data/left_mob2.png').convert_alpha(),
                 pygame.image.load('data/left_mob3.png').convert_alpha(), pygame.image.load('data/left_mob4.png').convert_alpha(),
                 pygame.image.load('data/left_mob1.png').convert_alpha(), pygame.image.load('data/left_mob2.png').convert_alpha()],
                [pygame.image.load('data/up_mob1.png').convert_alpha(), pygame.image.load('data/up_mob2.png').convert_alpha(),
                 pygame.image.load('data/up_mob3.png').convert_alpha(), pygame.image.load('data/up_mob4.png').convert_alpha(),
                 pygame.image.load('data/up_mob1.png').convert_alpha(), pygame.image.load('data/up_mob2.png').convert_alpha()],
                [pygame.image.load('data/down_mob1.png').convert_alpha(), pygame.image.load('data/down_mob2.png').convert_alpha(),
                 pygame.image.load('data/down_mob3.png').convert_alpha(), pygame.image.load('data/down_mob4.png').convert_alpha(),
                 pygame.image.load('data/down_mob1.png').convert_alpha(), pygame.image.load('data/down_mob2.png').convert_alpha()]]

bog_imgs = [[pygame.image.load('data/right_bog.png').convert_alpha(), pygame.image.load('data/right_bog1.png').convert_alpha(),
                pygame.image.load('data/right_bog2.png').convert_alpha(), pygame.image.load('data/right_bog3.png').convert_alpha(),
                pygame.image.load('data/right_bog.png').convert_alpha(), pygame.image.load('data/right_bog1.png').convert_alpha()],
                [pygame.image.load('data/left_bog.png').convert_alpha(), pygame.image.load('data/left_bog1.png').convert_alpha(),
                pygame.image.load('data/left_bog2.png').convert_alpha(), pygame.image.load('data/left_bog3.png').convert_alpha(),
                pygame.image.load('data/left_bog.png').convert_alpha(), pygame.image.load('data/left_bog1.png').convert_alpha()],
                [pygame.image.load('data/up_bog.png').convert_alpha(), pygame.image.load('data/up_bog1.png').convert_alpha(),
                pygame.image.load('data/up_bog2.png').convert_alpha(), pygame.image.load('data/up_bog3.png').convert_alpha(),
                pygame.image.load('data/up_bog.png').convert_alpha(), pygame.image.load('data/up_bog1.png').convert_alpha()],
                [pygame.image.load('data/down_bog.png').convert_alpha(), pygame.image.load('data/down_bog1.png').convert_alpha(),
                pygame.image.load('data/down_bog2.png').convert_alpha(), pygame.image.load('data/down_bog3.png').convert_alpha(),
                pygame.image.load('data/down_bog.png').convert_alpha(), pygame.image.load('data/down_bog1.png').convert_alpha()]]

demon_width = 32
demon_height = 48


wall_image = pygame.image.load('data/wall.png').convert_alpha()
wall_image = pygame.transform.scale(wall_image, (40, 40))
tree_image = pygame.image.load('data/tree.png').convert_alpha()
effect = pygame.image.load('data/EffectNew.png').convert_alpha()

bot_imgs = [[pygame.image.load('data/right_mob1.png').convert_alpha(), pygame.image.load('data/right_mob2.png').convert_alpha(),
                 pygame.image.load('data/right_mob3.png').convert_alpha(), pygame.image.load('data/right_mob4.png').convert_alpha()],
                [pygame.image.load('data/left_mob1.png').convert_alpha(), pygame.image.load('data/left_mob2.png').convert_alpha(),
                 pygame.image.load('data/left_mob3.png').convert_alpha(), pygame.image.load('data/left_mob4.png').convert_alpha()],
                [pygame.image.load('data/up_mob1.png').convert_alpha(), pygame.image.load('data/up_mob2.png').convert_alpha(),
                 pygame.image.load('data/up_mob3.png').convert_alpha(), pygame.image.load('data/up_mob4.png').convert_alpha()],
                [pygame.image.load('data/down_mob1.png').convert_alpha(), pygame.image.load('data/down_mob2.png').convert_alpha(),
                 pygame.image.load('data/down_mob3.png').convert_alpha(), pygame.image.load('data/down_mob4.png').convert_alpha()]]



invent_img = pygame.image.load('data/unknown.jpg').convert_alpha()
invent_img = pygame.transform.scale(invent_img, (90, 66))

dagger_img = pygame.image.load('data/dagger.png').convert_alpha()
dagger_img = pygame.transform.scale(dagger_img, (40,40))
