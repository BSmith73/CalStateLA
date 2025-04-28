#Bradley Smith
#Import Pygame
import pygame
import os
pygame.font.init()
pygame.mixer.init()

#sets screen size
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#sets the name of the window that runs the game
pygame.display.set_caption("Space Game")

#Defines colors that can be called in the code.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

#sets the border that is in the middle of the screen. 
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

#defines sounds that can be used.
BULLET_HIT_SOUND = pygame.mixer.Sound('Assets/Grenade+1.mp3')
BULLET_FIRE_SOUND = pygame.mixer.Sound('Assets/Gun+Silencer.mp3')

#defines font styles that can be used.
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

#sets game parameters
#frames per second
FPS = 60
#change in x and y per second
VEL = 5
#speed of bullet
BULLET_VEL = 7
#sets number of bullet objects allowed per player.
MAX_BULLETS = 3
#sets transformation size of the spaceship
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

#sets the hit defintion as a userevent. The +1 and +2 represent the event number "id"
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

#imports images for the spaceships by calling the image from the assets folder.
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
#Rotates the yellow spaceship image by 90 degrees and resizes the spaceship to the defined size varibles
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

#imports images for the spaceships by calling the image from the assets folder.
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
#Rotates the red spaceship ship image by 270 degrees and resizes the spaceship to the defined size varibles
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

#loads space background image and sets the size of it to the width and height of the screen
SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

#Set the functions of the draw loop to update the screen
def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE, (0, 0))
    #draws the middle border by calling the border definition. 
    pygame.draw.rect(WIN, BLACK, BORDER)

    #draws the health text for each player and the health value in a string and the color of the text.
    red_health_text = HEALTH_FONT.render(
        "Health: " + str(red_health), 1, RED)
    yellow_health_text = HEALTH_FONT.render(
        "Health: " + str(yellow_health), 1, YELLOW)
    
    #Sets the position of the health texts.
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))

    #draws the position of the spaceships by referencing their starting positions in the gameloop code.
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()

#In this section I swaps the "yellow.height" and "width" an error was in the video and he didn't realize that since he rotated the images that the height and width are swapped.
def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # LEFT and prevents player from going off the left side of the screen by stopping the movement to an x coordinate less than 0.
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.height < BORDER.x:  # RIGHT and prevents player from going across the boarders position.
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # UP and prevents player from going off the top side of the screen by stopping the movement to an y coordinate less than 0.
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.width < HEIGHT:  # DOWN and prevents player from going off the bottom side of the screen by stopping the movement at the screen hieght -15.
        yellow.y += VEL

#See notes for yellow_handle_movements
def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.height < WIDTH:  # RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # UP
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.width < HEIGHT:  # DOWN
        red.y += VEL

#checks collision and removes bullets.
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    #rules for yellow
    for bullet in yellow_bullets:
        #moves yellow bullet to the right
        bullet.x += BULLET_VEL
        #checks if the bullet hit the red spaceship, counts the hit with the red hit fuction, and removes.
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        #if bullet position reaches the side of the screen then it is removed.
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    #similar idea but for red, bullets move to the left.
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

#draws winner text after the winner event is triggered.
def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, MAGENTA)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

#Game loop starts
def main():
    #sets the starting positions of the spaceships
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    #Player's bullets list, allows to check how many are in the list for MAX_BULLETS
    red_bullets = []
    yellow_bullets = []

    #Sets starting health for players
    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        #controls the frames per second to stablize across devices.
        clock.tick(FPS)
        for event in pygame.event.get():
            #allows users to quit
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            #Preps to have player press their bullet keys.
            if event.type == pygame.KEYDOWN:
                #changed the firing button to space.
                #also checks if a bullet will spawn against the max_bullets.
                if event.key == pygame.K_SPACE and len(yellow_bullets) < MAX_BULLETS:
                    #sets the starting position of yellow bullets.
                    #again fixed the flip with height and width.
                    bullet = pygame.Rect(
                        yellow.x + yellow.height, yellow.y + yellow.width//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                #also checks if a bullet will spawn against the max_bullets.
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    #sets the starting position of yellow bullets.
                    #again fixed the flip with height and width.
                    bullet = pygame.Rect(
                        red.x, red.y + red.width//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
            
            #modifies players' health by -1 with HIT events.
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

        #Triggers winner text if either players' health reaches 0 or less
        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins!"

        if yellow_health <= 0:
            winner_text = "Red Wins!"

        #displayes the text when winner_text has a value and calls the draw_winner function.
        if winner_text != "":
            draw_winner(winner_text)
            break

        #allows multiple keys to be presses at the same time. Calles the yellow and red movement codes.
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        #checks collision 
        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets,
                    red_health, yellow_health)
    
    #allows the game to restart
    main()


if __name__ == "__main__":
    main()
