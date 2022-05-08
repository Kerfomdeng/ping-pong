from pygame import *
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
        if self.rect.x >=550:
            self.rect.x=250
            self.rect.y=200
        if self.rect.x <=5:
            self.rect.x=250
            self.rect.y=200
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
speed_x = 3
speed_y = 3
run=True
while game:
    for e in event.get():
            if e.type == QUIT:
                game = False
    if run !=False:
        racker1.update_l()
        racker2.update_r()
        window.fill(back)
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
        racker1.reset()
        racker2.reset()
        ball.reset()
    display.update()
    clock.tick(50)





