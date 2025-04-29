
#code is from Coding with Russ https://www.youtube.com/playlist?list=PLjcN1EyupaQnB9-Ovkisq0Ss-1u0gOAv4

#Group Members: Peter and Bradley 
#we liked the two player element of this game and that the game progress It was neat to explore some of the collision features of pygame. 
#We thought about possibly adding power ups to accelerate the ball, or freeze the opponent's paddle. 
#we also discussed giving users the option to play against another human or against the computer.

#imports pygame
import pygame
from pygame.locals import *

pygame.init()
#sets screen size
screen_width = 600
screen_height = 500

#sets frames per second
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Peter and Braldey\'s Pong')


#sets font for all text on the game
font = pygame.font.SysFont('Comic Sans', 24)


#sets certain varibles to intergers
live_ball = False
margin = 50
cpu_score = 0
player_score = 0
fps = 60
winner = 0
speed_increase = 0




#defines the background color and the color white
bg = (50, 25, 50)
white = (255, 255, 255)

#fills the screen with the board color
def draw_board():
    screen.fill(bg)
    #draws a line for the scoreboard
    pygame.draw.line(screen, white, (0, margin), (screen_width, margin))


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

#creates the paddle, paddle location, and speed of this object.
class paddle():
    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.rect = Rect(self.x, self.y, 20, 100)
        self.speed = 5
    
        #sets the move functions with up and down keys for player 2.  
    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.rect.top> margin:
            self.rect.move_ip(0, -1 * self.speed)
        if key[pygame.K_DOWN] and self.rect.bottom < screen_height:
            self.rect.move_ip(0, self.speed)

     #sets the move functions with "w" and "s" keys for player 1.
    def ai(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and self.rect.top> margin:
            self.rect.move_ip(0, -1 * self.speed)
        if key[pygame.K_s] and self.rect.bottom < screen_height:
            self.rect.move_ip(0, self.speed)


    def draw(self):
        pygame.draw.rect(screen, white, self.rect)

#creates the ball and its features of the ball.
class ball():
    def __init__(self, x, y):

        
        self.reset(x, y)

    def move(self):

        
        if self.rect.top < margin:
            self.speed_y *= -1
        if self.rect.bottom > screen_height:
            self.speed_y *= -1

        
        if self.rect.left < 0:
            self.winner = 1
        if self.rect.right > screen_width:
            self.winner = -1

        
        if self.rect.colliderect(player_paddle) or self.rect.colliderect(cpu_paddle):
            self.speed_x *= -1



        
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        return self.winner 

    #creates the object of the ball
    def draw(self):
        pygame.draw.circle(screen, white, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad)

    
    def reset(self, x, y):
        self.x = x
        self.y = y
        self.ball_rad = 8
        self.rect = Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
        self.speed_x = -4
        self.speed_y = 4
        self.winner = 0 
        


#creates the paddles and their locations.
player_paddle = paddle(screen_width - 40, screen_height // 2)
cpu_paddle = paddle(20, screen_height // 2)


pong = ball(screen_width - 60, screen_height // 2 + 50)


#starts the game.
run = True
while run:

    fpsClock.tick(fps)

    draw_board()
    draw_text('Player 1: ' + str(cpu_score), font, white, 10, 8)
    draw_text('Player 2: ' + str(player_score), font, white, screen_width - 140, 8)
    draw_text('Ball Speed: ' + str(abs(pong.speed_x)), font, white, screen_width //2 - 100, 8)


    
    player_paddle.draw()
    cpu_paddle.draw()
    #increases ball speed when the game is running. Also add score to the winner player. 
    if live_ball == True:
        speed_increase += 1
        
        winner = pong.move()
        if winner == 0:
            #allows paddles to move when game is play
            player_paddle.move()
            cpu_paddle.ai()
            #allows ball to move when game is play
            pong.draw()
        #Stops gameplay and scores a point for the person who scored.
        else:
            live_ball = False
            if winner == 1:
                player_score += 1
            elif winner == -1:
                cpu_score += 1


    #once the ball is out of play it will display a message to the user to know who scored.
    if live_ball == False:
        if winner == 0:
            draw_text('Click anywhere to Start', font, white, 150, screen_height // 2 - 100)
        if winner == 1:
            draw_text('Player 2 Scored!', font, white, 180, screen_height // 2 - 100)
            draw_text('Click anywhere to Start', font, white, 150, screen_height //2 - 50)
        if winner == -1:
            draw_text('Player 1 Scored!', font, white, 180, screen_height // 2 - 100)
            draw_text('Click anywhere to Start', font, white, 150, screen_height //2 - 50)


    
    #how to end the game or play the next round.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and live_ball == False:
            live_ball = True
            pong.reset(screen_width - 60, screen_height // 2 +50)
    
    #Increases the speed of the ball on the x and y access and accounts for the increase in speed in both directions (left and right)
    if speed_increase > 500:
        speed_increase = 0
        if pong.speed_x < 0:
            pong.speed_x -= 1
        if pong.speed_x > 0:
            pong.speed_x += 1
        if pong.speed_y < 0:
            pong.speed_y -= 1
        if pong.speed_y > 0:
            pong.speed_y += 1



    pygame.display.update()


pygame.quit()
