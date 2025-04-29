#Bradley Smith
#replaced all "baddie" with meteor.
#Replaced white background with a color similar to background of the meteor image 
    # but left it slightly different to ensure player could see the edges of the shape.

#Sounds: from pixabay
    #Startup_Sound: Riser Wildfire by SoundReality
    #BG Music: Game Music Loop 3 by XtremeFreddy
    #GameOver: Game Over by Freesound_community

import pygame, random, sys
from pygame.locals import *

WINDOWWIDTH = 600
WINDOWHEIGHT = 600
TEXTCOLOR = (0, 0, 0)
BACKGROUNDCOLOR = (3, 61, 252)
FPS = 60
meteorMINSIZE = 10
meteorMAXSIZE = 40
meteorMINSPEED = 1
meteorMAXSPEED = 8
#reduced meteor rate by raising number
ADDNEWmeteorRATE = 20
PLAYERMOVERATE = 5

gameIcon = pygame.image.load('meteor_icon.jpg')
pygame.display.set_icon(gameIcon)

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Pressing ESC quits.
                    terminate()
                return

def playerHasHitmeteor(playerRect, meteors):
    for b in meteors:
        if playerRect.colliderect(b['rect']):
            return True
    return False

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Set up pygame, the window, and the mouse cursor.
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Meteor Dodge')
pygame.mouse.set_visible(False)

# Set up the fonts.
font = pygame.font.SysFont(None, 48)

# Set up sounds.
gameOverSound = pygame.mixer.Sound('gameover.mp3')
#loading a start up sound!
startup_sound = pygame.mixer.Sound('riser-wildfire.mp3')
pygame.mixer.music.load('game_music_loop_3.mp3')

# Set up images.
playerImage = pygame.image.load('player_jet.jpg')
#Image was too big so needed to add code that limited the size of the image. I chose a 50px square. 
playerImage = pygame.transform.scale(playerImage, (50, 50))
playerRect = playerImage.get_rect()
meteorImage = pygame.image.load('meteor.jpg')

# Show the "Start" screen.
windowSurface.fill(BACKGROUNDCOLOR)
drawText('Meteor Dodge', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('Press a key to start.', font, windowSurface, (WINDOWWIDTH / 3) - 40, (WINDOWHEIGHT / 3) + 50)

#included directions to the cheat buttons.
drawText('Press x and z to cheat.', font, windowSurface, (WINDOWWIDTH / 3) - 70, (WINDOWHEIGHT) - (WINDOWHEIGHT/5))
pygame.display.update()
waitForPlayerToPressKey()

topScore = 0
while True:
    # Set up the start of the game.
    meteors = []
    score = 0
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    meteorAddCounter = 0
    #plays the startup_sound on game start.
    startup_sound.play()
    pygame.mixer.music.play(-1, 0.0) #loops the background music.

    while True: # The game loop runs while the game part is playing.
        score += 1 # Increase score.

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == K_z:
                    reverseCheat = True
                if event.key == K_x:
                    slowCheat = True
                if event.key == K_LEFT or event.key == K_a:
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == K_d:
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == K_w:
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == K_s:
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP:
                if event.key == K_z:
                    reverseCheat = False
                    score = 0
                if event.key == K_x:
                    slowCheat = False
                    score = 0
                if event.key == K_ESCAPE:
                        terminate()

                if event.key == K_LEFT or event.key == K_a:
                    moveLeft = False
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = False
                if event.key == K_UP or event.key == K_w:
                    moveUp = False
                if event.key == K_DOWN or event.key == K_s:
                    moveDown = False

            if event.type == MOUSEMOTION:
                # If the mouse moves, move the player where to the cursor.
                playerRect.centerx = event.pos[0]
                playerRect.centery = event.pos[1]
        # Add new meteors at the top of the screen, if needed.
        if not reverseCheat and not slowCheat:
            meteorAddCounter += 1
        if meteorAddCounter == ADDNEWmeteorRATE:
            meteorAddCounter = 0
            meteorSize = random.randint(meteorMINSIZE, meteorMAXSIZE)
            newmeteor = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - meteorSize), 0 - meteorSize, meteorSize, meteorSize),
                        'speed': random.randint(meteorMINSPEED, meteorMAXSPEED),
                        'surface':pygame.transform.scale(meteorImage, (meteorSize, meteorSize)),
                        }

            meteors.append(newmeteor)

        # Move the player around.
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)

        # Move the meteors down.
        for b in meteors:
            if not reverseCheat and not slowCheat:
                b['rect'].move_ip(0, b['speed'])
            elif reverseCheat:
                b['rect'].move_ip(0, -5)
            elif slowCheat:
                b['rect'].move_ip(0, 1)

        # Delete meteors that have fallen past the bottom.
        for b in meteors[:]:
            if b['rect'].top > WINDOWHEIGHT:
                meteors.remove(b)

        # Draw the game world on the window.
        windowSurface.fill(BACKGROUNDCOLOR)

        # Draw the score and top score.
        drawText('Score: %s' % (score), font, windowSurface, 10, 0)
        drawText('Top Score: %s' % (topScore), font, windowSurface, 10, 40)

        # Draw the player's rectangle.
        windowSurface.blit(playerImage, playerRect)

        # Draw each meteor.
        for b in meteors:
            windowSurface.blit(b['surface'], b['rect'])

        pygame.display.update()

        # Check if any of the meteors have hit the player.
        if playerHasHitmeteor(playerRect, meteors):
            if score > topScore:
                topScore = score # set new top score
            break

        mainClock.tick(FPS)

    # Stop the game and show the "Game Over" screen.
    pygame.mixer.music.stop()
    gameOverSound.play()

    drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
    drawText('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
    pygame.display.update()
    waitForPlayerToPressKey()

    gameOverSound.stop()
