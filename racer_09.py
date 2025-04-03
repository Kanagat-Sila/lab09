import pygame
from pygame.locals import *
import random

pygame.init()
clock = pygame.time.Clock()


cell_size = 30
cell_number = 20
Score = 0
Level = 1
coin_score = 0
# COLORS
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
White = (255, 255, 255)
Black = (0, 0, 0)

# Player class to detect position and making rectangle
class Player:
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos
        self.im = pygame.image.load(r"C:\Users\Admin\Desktop\pp2\lab07\lab08\Player.png")
        self.im = pygame.transform.scale(self.im, (50,100))
        
    
    def image(self):
        return self.im.get_rect(center = (self.x, self.y))
    

    def damage(self):
        pass



# Enemy class to detect position and making rectangle

class Enemy:
    def __init__(self, x_pos , y_pos, speed):
        self.im = pygame.image.load(r"C:\Users\Admin\Desktop\pp2\lab07\lab08\Enemy.png")
        self.x = x_pos
        self.y = y_pos
        self.speed = speed


    def image(self):
        enemy = self.im.get_rect(midbottom = (self.x, self.y))
        return enemy

# Coins class to detect position and making rectangle
class Coins:
    def __init__(self, x_pos , y_pos, speed):
        self.im = pygame.image.load(r"C:\Users\Admin\Desktop\pp2\lab07\lab08\dollar.png")
        self.im = pygame.transform.scale(self.im, (50,50))
        self.x = x_pos
        self.y = y_pos
        self.speed = speed


    def image(self):
        coin = self.im.get_rect(midbottom = (self.x, self.y))
        return coin



    






        

#setting screen size
screen = pygame.display.set_mode((cell_size * cell_number, cell_number * cell_size))

font = pygame.font.Font('Pixeltype.ttf', 50)
message = font.render("GAME OVER", True, Red)
message_rect = message.get_rect(center=((cell_number * cell_size) // 2, (cell_number * cell_size) // 2))

bg = pygame.image.load(r"C:\Users\Admin\Desktop\pp2\lab07\lab08\AnimatedStreet.png")
bg = pygame.transform.scale(bg, (cell_size * cell_number, cell_number * cell_size))
bg_rect = bg.get_rect(topleft = (0, 0))

# Background music
musics = [
    r"C:\Users\Admin\Desktop\pp2\lab07\lab08\background.wav",
    r"C:\Users\Admin\Desktop\pp2\lab07\lab08\crash.wav"
]

current_track = 0
pygame.mixer.music.load(musics[current_track])
pygame.mixer.music.play(-1)


done = False

# Player default position
pl_x = 300
pl_y = 500

# enemy default position
enemy_pos_y = -1
enemy_pos_x = random.randint(100, 500)
speed = 5

# Coins position
coin_pos_x = random.randint(100, 500)
coin_pos_y = -1

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
    pygame.display.set_caption(f"Level: {Level}         RACER         Score: {Score}          Coins: {coin_score//2}")

        
        

    # Player movement
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        pl_x -= 10
    elif key[pygame.K_RIGHT]:
        pl_x += 10        


    




    
    player = Player(pl_x, pl_y)
    enemy = Enemy(enemy_pos_x,enemy_pos_y, speed)
    coins = Coins(coin_pos_x, coin_pos_y, speed)


    enem = enemy.image()
    car = player.image()
    coin = coins.image()

    # Enemey and coins speed
    enemy_pos_y += speed
    coin_pos_y += speed - 2




    # Checking collision of car and enemy
    if car.colliderect(enem) or car.left > 500 or car.right < 100:
        current_track += 1
        pygame.mixer.music.load(musics[current_track])
        pygame.mixer.music.play()
        screen.fill(White)
        screen.blit(message, message_rect)
        pygame.display.flip()
        pygame.time.delay(2000)  
        done = True
        break  

    # Checking collision of car and coin
    if car.colliderect(coin):
        coin_sound =  pygame.mixer.Sound('coins-135571.mp3')
        coin_sound.play()
        coin_score += 1 
        coin_pos_x = random.randint(100, 500) 
        coin_pos_y = -1
        coin_score += 1
        




    
    
    screen.blit(bg, bg_rect)
    screen.blit(player.im, car)
    screen.blit(enemy.im, enem)
    screen.blit(coins.im, coin)


    # Generating new enemy and adding 1 poin to score
    if enem.top > 600:
        enemy_pos_x = random.randint(100, 500) 
        enemy_pos_y = -1
        Score += 1

    # Generating new coins
    if coin.top > 600:
        while True:
            coin_pos_x = random.randint(100, 500) 
            if coin_pos_x != enemy_pos_x or abs(coin_pos_x - enemy_pos_x) > 50:
                 break

            

        coin_pos_y = -10
        coin_score += 1

    # New level condition
    if Score > 5:
        Level += 1
        Score = 0
        speed += 5


   

    
    pygame.display.flip()
    clock.tick(60)


