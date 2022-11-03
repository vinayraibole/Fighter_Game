#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import time
import pygame as pg, sys
from pygame.locals import *
import os


# # Defnining the Width & Height of the Game Window

# In[ ]:


width = 1280
height = 720


# # Initializing pygame and setting up the screen

# In[ ]:


pg.init()
screen = pg.display.set_mode((width,height))
main_font = pg.font.SysFont('cambria',30)


# # Function to return font with given size

# In[ ]:


def get_font(size):
    return pg.font.SysFont('cambria', size)


# # Defining Button class

# In[ ]:


class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)


# # Defining the main menu

# In[ ]:


def main_menu():
    
    pg.display.set_caption('UFC - Menu')
    
    btn = pg.image.load("./Assets/Button.png")
    btn = pg.transform.scale(btn,(width*20/100,height*10/100))

    background = pg.image.load("./Assets/Background.jpeg")
    background = pg.transform.scale(background,(width,height))
    
    minilogo = pg.image.load("./Assets/MiniLogo.png")
    minilogo = pg.transform.scale(minilogo,(width*10/100,height*10/100))
    
    while True:
        screen.blit(background,(0,0))
        
        menu_mouse_pos = pg.mouse.get_pos()
        
        menu_logo = screen.blit(minilogo,minilogo.get_rect(center = (width/2,height*10/100)))
        
        menu_text = get_font(100).render('BEGIN FIGHTS!!',True,'#8b0000')
        menu_rect = menu_text.get_rect(center = (width/2,height*25/100))
        
        play_button = Button(btn,(width/2,height*40/100),
                             'PLAY',get_font(30),'red','white')
        quit_button = Button(btn,(width/2,height*50/100),
                             'QUIT',get_font(30),'red','white')
        
        screen.blit(menu_text, menu_rect)
        
        for button in [play_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)
            
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if ev.type == pg.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_mouse_pos):
                    new_game()
                if quit_button.checkForInput(menu_mouse_pos):
                    pg.quit()
                    exit()
        
        pg.display.update()
        


# # Defining the game

# In[ ]:


def new_game():
    
    pg.init()
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption('ULTIMATE FIGHTING CHAMPIONSHIP')
    
    opening = pg.image.load("./Assets/Homepage.jpeg")
    opening = pg.transform.scale(opening,(width,height))
    background = pg.image.load("./Assets/Background.jpeg")
    background = pg.transform.scale(background,(width,height))
    minilogo = pg.image.load("./Assets/MiniLogo.png")
    minilogo = pg.transform.scale(minilogo,(width*10/100,height*10/100))

    screen.blit(opening,(0,0))
    pg.display.update()
    time.sleep(3)
    
    screen.blit(background,(0,0))
    pg.display.update()
    time.sleep(2)
    
    screen.blit(minilogo,minilogo.get_rect(center = (width/2,height*10/100/2)))
    pg.display.update()
    
    p1_fighter = [i for i in os.listdir("./Assets/P1 Fighter/") if i != '.DS_Store']
    p2_fighter = [i for i in os.listdir("./Assets/P2 Fighter/") if i != '.DS_Store']
    p3_fighter = [i for i in os.listdir("./Assets/P3 Fighter/") if i != '.DS_Store']

    today_fighter = [random.choice(p1_fighter),random.choice(p2_fighter),random.choice(p3_fighter)]

    font = pg.font.Font(None,60)
    text = font.render("Get Ready for Today's Champions!!!",1,('#8b0000'))
    text_rect = text.get_rect(center = (width/2, height*20/100))
    screen.blit(text, text_rect)
    pg.display.update()
    time.sleep(2)
    

    font = pg.font.Font(None,40)
    text = font.render("P1'S FIGHTER",1,('#880808'))
    screen.blit(text, (width - 3 * width/3 + width*8/100,height*75/100))
    pg.display.update()
    time.sleep(2)
    
    text = font.render(today_fighter[0].split('.')[0],1,('#880808'))
    screen.blit(text, (width - 3 * width/3 + width*8/100,height*82/100))
    fighter = pg.image.load("./Assets/P1 Fighter/"+today_fighter[0])
    fighter = pg.transform.scale(fighter,(width*25/100,height*40/100))
    screen.blit(fighter, (width - 3 * width/3 + width*5/100,height*30/100))
    pg.display.update()
    time.sleep(2)
    
    text = font.render("P2'S FIGHTER",1,('#880808'))
    screen.blit(text, (width - 2 * width/3 + width*8/100,height*75/100))
    pg.display.update()
    time.sleep(2)
    
    text = font.render(today_fighter[1].split('.')[0],1,('#880808'))
    screen.blit(text, (width - 2 * width/3 + width*8/100,height*82/100))
    fighter = pg.image.load("./Assets/P2 Fighter/"+today_fighter[1])
    fighter = pg.transform.scale(fighter,(width*25/100,height*40/100))
    screen.blit(fighter, (width - 2 * width/3 + width*5/100,height*30/100))
    pg.display.update()
    time.sleep(2)
    
    text = font.render("P3'S FIGHTER",1,('#880808'))
    screen.blit(text, (width - 1 * width/3 + width*8/100,height*75/100))
    pg.display.update()
    time.sleep(2)
    
    text = font.render(today_fighter[2].split('.')[0],1,('#880808'))
    screen.blit(text, (width - 1 * width/3 + width*8/100,height*82/100))
    fighter = pg.image.load("./Assets/P3 Fighter/"+today_fighter[2])
    fighter = pg.transform.scale(fighter,(width*25/100,height*40/100))
    screen.blit(fighter, (width - 1 * width/3 + width*5/100,height*30/100))
    pg.display.update()
    time.sleep(2)

    screen.blit(background,(0,0))
    pg.display.update()
    
    font = pg.font.Font(None,60)
    text = font.render("LET'S FIGHT",1,('#8b0000'))
    text_rect = text.get_rect(center = (width/2, height*10/100))
    screen.blit(text, text_rect)
    pg.display.update()
    time.sleep(2)
    
    text = font.render("THE FIGHT BEGINS",1,('#8b0000'))
    text_rect = text.get_rect(center = (width/2, height*20/100))
    screen.blit(text, text_rect)
    pg.display.update()
    time.sleep(2)
    
    text = font.render("AND THE WINNER IS!!!",1,('#8b0000'))
    text_rect = text.get_rect(center = (width/2, height*30/100))
    screen.blit(text, text_rect)
    pg.display.update()
    time.sleep(2)
    
    choice = random.choice([0,1,2])
    if choice == 0:
        fighter = pg.image.load("./Assets/P1 Fighter/"+today_fighter[choice])
    elif choice == 1:
        fighter = pg.image.load("./Assets/P2 Fighter/"+today_fighter[choice])
    elif choice == 2:
        fighter = pg.image.load("./Assets/P3 Fighter/"+today_fighter[choice])

    fighter = pg.transform.scale(fighter,(width*25/100,height*40/100))
    
    screen.blit(fighter, (width*38/100, height*40/100))
    
    text = font.render(today_fighter[choice].split('.')[0],1,('#880808'))
    screen.blit(text, (width*39/100, height*85/100))
    pg.display.update()

    time.sleep(10)


# In[ ]:


main_menu()


# In[ ]:




