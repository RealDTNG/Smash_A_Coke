# Dawson Hoyle 
# may 4 2023
# I DONT WANT TO WACK A COKE
'''
 > 900 x 1028 H     < Current Length and Width
'''
import pygame as pg
import random
from cokee import coke
from screeninfo import get_monitors
from button_class import Button

pg.init()
fps = 60
fpsClock = pg.time.Clock()
pg.font.init()
WINDOW_WIDTH = int((str(get_monitors()).split(","))[2][7:])
WINDOW_HEIGHT = int((str(get_monitors()).split(","))[3][8:])
coke_img = pg.image.load("coke_can.png")
window = pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pg.FULLSCREEN)
pg.display.set_caption("Smash The Coke!")
my_font = pg.font.Font('Bruno.ttf', 40)
start = True
playing = False
ending = False
score = 0
coke_group = pg.sprite.Group()
text_score = my_font.render(f'SCORE:{score}', False, (255, 176, 176))

def cann():
  global coke_can
  coke_can = coke(725-(91/2), 600, 91, 174, coke_img)
  coke_group.empty()
  coke_group.add(coke_can)

def starting():
    global start, playing, ending
    start = False
    playing = True
    ending = False
    cann()
    pg.display.update()
    
btn_start = Button(595, 500, 300, 100, 'Start', starting)
btn_restart = Button(595, 500, 300, 100, 'Restart', starting)

def display():
  global score
  if start == True:
      text_start1 = my_font.render('Welcome To....', False, (213, 232, 162))
      text_start2 = my_font.render('CRUSH THE COKE', False, (213, 232, 162))
      temp_width1 = text_start1.get_width()
      temp_width2 = text_start2.get_width()
      window.blit(text_start1, (745-(temp_width1/2),300))
      window.blit(text_start2, (745-(temp_width2/2),370))
      btn_start.process(window)
  elif playing == True:
    window.fill((207, 207, 207))
    text_playing1 = my_font.render('Crush The Cokes To Win!!', False, (255, 176, 176))
    temp_width3 = text_playing1.get_width()
    window.blit(text_playing1, (745-(temp_width3/2),100))
    text_score = my_font.render(f'SCORE:{score}', False, (255, 176, 176))
    temp_width4 = text_score.get_width()
    window.blit(text_score, (745-(temp_width4/2),150))
    text_help = my_font.render('Press "q" To Quit', False, (255, 176, 176))
    window.blit(text_help, (10,20))
    coke_group.draw(window)
  elif ending == True:
    pg.display.update()
    coke_group.empty()
    window.fill((207, 207, 207))
    text_ending1 = my_font.render('You Reached 500 Score\nYOU WINNN', False, (255, 176, 176))
    temp_width5 = text_ending1.get_width()
    window.blit(text_playing1, (745-(temp_width5/2),300))
    btn_restart.process(window)

while True:
    ev = pg.event.get()
    key_input = pg.key.get_pressed()
    if score >= 500:
      ending == True
      playing == False
    display()
    if key_input[pg.K_q]:
        exit()
    for event in ev:
      if event.type == pg.MOUSEBUTTONUP:
        pos = pg.mouse.get_pos()
        clicked_sprites = [s for s in coke_group if s.rect.collidepoint(pos)]
        handled = pg.mouse.get_pressed()[0]
        
      if pg.mouse.get_pressed()[0] and coke_can.rect.collidepoint(pg.mouse.get_pos()) and not handled:
        score += 10
        coke_can.rect.x = 500+(random.randint(0,400))
        coke_can.rect.y = 300+(random.randint(0,300))
        handled = pg.mouse.get_pressed()[0]
        if score == 500:
          ending == True
          playing == False
        
    for event in pg.event.get():
      if event.type == pg.QUIT:# if user  QUIT then the screen will close 
        exit()
    
    pg.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw
