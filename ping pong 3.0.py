from pygame import *
import time as time_
z=0
v=0
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(wight,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 345:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 345:
            self.rect.y += self.speed
    def update_ball(self):    
        global wait_time
        global z
        global v
        if self.rect.x >=550:
            self.rect.x=250
            self.rect.y=200
            z+=1
            wait_time = time_.time()
        if self.rect.x <=5:
            self.rect.x=250
            self.rect.y=200
            v+=1 
            wait_time = time_.time()   
    #Игровая сцена
back = (200,255,255)
win_width = 600
win_height = 500
window = display.set_mode((win_width,win_height))
window.fill(back)

#Состояние игры
game = True
clock = time.Clock()
FPS = 60

#Ракетки и мяч
racker1 = Player("racket.png",30,200,4,50,150)
racker2 = Player("racket.png",520,200,4,50,150)
ball = Player("tenis_ball.png",200,200,4,50,50)

#Работа с текстом
font.init()
font = font.Font(None, 50)
lose1 = font.render("Игрок n1 продул",True,(180,0,0))
lose2 = font.render("Игрок n2 продул",True,(180,0,0))
numbers=font.render("Счёт",True,(0,0,0))
numbers1=font.render(str(z),True,(0,0,0))
numbers2=font.render(str(v),True,(0,0,0))
wait_time=0
w_t_t=font.render(str(wait_time),True,(255,255,255))
speed_x = 3
speed_y = 3
run=True
while game:
    for e in event.get():
            if e.type == QUIT:
                game = False
    if run !=False:
        window.blit(numbers, (200, 5))
        window.blit(numbers1, (210, 40))
        window.blit(numbers2, (250, 40))
        racker1.update_l()
        racker2.update_r()
        window.blit(numbers, (200, 5))
        window.blit(numbers1, (210, 40))
        window.blit(numbers2, (250, 40))
        if int(time_.time()-wait_time) <=3:
            ball.rect.x=250  
            ball.rect.y=200    
            w_t_t=font.render(str(int(time_.time()-wait_time)),True,(180,0,0))
            window.blit(w_t_t,(300,200))
        window.blit(lose2, (250, 250))
        numbers=font.render("Счёт",True,(0,0,0))
        numbers1=font.render(str(z),True,(0,0,0))
        numbers2=font.render(str(v),True,(0,0,0))
        window.fill(back)
        window.blit(numbers, (200, 5))
        window.blit(numbers1, (210, 40))
        window.blit(numbers2, (250, 40))
        racker1.update_l()
        racker2.update_r()
        ball.update_ball()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > 450 or ball.rect.y <0:
            speed_y *= -1
        if sprite.collide_rect(racker1,ball) or sprite.collide_rect(racker2,ball):
            speed_x *= -1
            speed_y *= 1
        if z == 7:
            window.blit(lose2, (200, 250))
            run = False
        if v == 7:
            window.blit(lose1, (200, 250))
            run = False            
        racker1.reset()
        racker2.reset()
        ball.reset()
    display.update()
    clock.tick(50)





