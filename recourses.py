import pygame
import os

main_folder = os.path.dirname(__file__)

fon_image = pygame.image.load(os.path.join(main_folder, "images/Fon1.png"))
no_image = pygame.image.load(os.path.join(main_folder, "images/no.png"))
yes_image = pygame.image.load(os.path.join(main_folder, "images/yes.png"))
exit_image = pygame.image.load(os.path.join(main_folder, "images/exit.jpg"))
poison_good = pygame.image.load(os.path.join(main_folder, "images/poison_+10.gif"))
poison_bad = pygame.image.load(os.path.join(main_folder, "images/poison_-10.gif"))
mushroom = pygame.image.load(os.path.join(main_folder, "images/mushroom.gif"))
key_x3 = pygame.image.load(os.path.join(main_folder, "images/keyx3.gif"))
key_x5 = pygame.image.load(os.path.join(main_folder, "images/keyx5.gif"))
key_x2 = pygame.image.load(os.path.join(main_folder, "images/keyx2.gif"))
strawberry = pygame.image.load(os.path.join(main_folder, "images/straw.gif"))
main_poze = pygame.image.load(os.path.join(main_folder, "images/main_poze.png"))
left_poze1 = pygame.image.load(os.path.join(main_folder, "images/left_poze1.png"))
left_poze2 = pygame.image.load(os.path.join(main_folder, "images/left_poze2.png"))
left_poze3 = pygame.image.load(os.path.join(main_folder, "images/left_poze3.png"))
right_poze1 = pygame.image.load(os.path.join(main_folder, "images/right_poze1.png"))
right_poze2 = pygame.image.load(os.path.join(main_folder, "images/right_poze2.png"))
right_poze3 = pygame.image.load(os.path.join(main_folder, "images/right_poze3.png"))
game_image = pygame.image.load(os.path.join(main_folder, "images/background.png"))
play_image = pygame.image.load(os.path.join(main_folder, "images/play_1.png"))
options_image = pygame.image.load(os.path.join(main_folder, "images/sett.jpg"))
options1_image = pygame.image.load(os.path.join(main_folder, "images/sett2.jpg"))
options3_image = pygame.image.load(os.path.join(main_folder, "images/setti3.jpg"))
play_2_image = pygame.image.load(os.path.join(main_folder, "images/play_2.png"))
play_3_image = pygame.image.load(os.path.join(main_folder, "images/play_3.png"))
back_image = pygame.image.load(os.path.join(main_folder, "images/back.png"))
game_over_image = pygame.image.load(os.path.join(main_folder, "images/game_over.gif"))
restart_image = pygame.image.load(os.path.join(main_folder, "images/restart.png"))
button_0 = pygame.image.load(os.path.join(main_folder, "images/0.png"))
button_1 = pygame.image.load(os.path.join(main_folder, "images/1.png"))
button_2 = pygame.image.load(os.path.join(main_folder, "images/2.png"))
button_3 = pygame.image.load(os.path.join(main_folder, "images/3.png"))
button_4 = pygame.image.load(os.path.join(main_folder, "images/4.png"))
button_5 = pygame.image.load(os.path.join(main_folder, "images/5.png"))
button_6 = pygame.image.load(os.path.join(main_folder, "images/6.png"))
button_7 = pygame.image.load(os.path.join(main_folder, "images/7.png"))
button_8 = pygame.image.load(os.path.join(main_folder, "images/8.png"))
button_9 = pygame.image.load(os.path.join(main_folder, "images/9.png"))
button_10 = pygame.image.load(os.path.join(main_folder, "images/10.png"))
button_30 = pygame.image.load(os.path.join(main_folder, "images/30.png"))
button_20 = pygame.image.load(os.path.join(main_folder, "images/20.png"))
button_40 = pygame.image.load(os.path.join(main_folder, "images/40.png"))
button_50 = pygame.image.load(os.path.join(main_folder, "images/50.png"))
button_60 = pygame.image.load(os.path.join(main_folder, "images/60.png"))
button_70 = pygame.image.load(os.path.join(main_folder, "images/70.png"))
button_80 = pygame.image.load(os.path.join(main_folder, "images/80.png"))
button_90 = pygame.image.load(os.path.join(main_folder, "images/90.png"))
button_100 = pygame.image.load(os.path.join(main_folder, "images/100.png"))
button_plus = pygame.image.load(os.path.join(main_folder, "images/+.png"))
button_minus = pygame.image.load(os.path.join(main_folder, "images/-.png"))
SHIRINA = 1920
VISOTA = 1040
volume_buttons = [button_0, button_10, button_20, button_30, button_40, button_50, button_60, button_70, button_80,
                  button_90, button_100]
point_value = [button_0, button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9]
play_2_image.set_colorkey((255, 255, 255))
play_3_image.set_colorkey((255, 255, 255))