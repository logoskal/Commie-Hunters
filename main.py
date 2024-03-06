import pygame

#CONSTANTS
WIDTH, HEIGHT = 750, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 40, 60
PLAYER_VELOCITY = 5
run = True

#SET PROPERTIES
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge")
BG = pygame.transform.scale(pygame.image.load("bg.jpg"),(WIDTH, HEIGHT))

#LOAD AND PLAY THE MAIN MUSIC FILE
pygame.mixer.init()
pygame.mixer.music.load('screech1.mp3')
pygame.mixer.music.play(loops=2, start=1)
pygame.mixer.music.set_volume(0.5)


#THE DRAWER
def draw(player):
    WIN.blit(BG, (0,0))
    pygame.draw.rect(WIN, "red", player)
    pygame.display.update()


#THE MAIN FUNCTION
def main():

    #THE PLAYER
    player = pygame.Rect(WIDTH/2 - PLAYER_WIDTH/2, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    
    #TICKS - Basically an FPS
    clock = pygame.time.Clock()

    global run
    while run:
        clock.tick(120)

        #EXIT CONDITION
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        #KEY LOGGER
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player.x - PLAYER_VELOCITY >= 0:
            player.x -= PLAYER_VELOCITY
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VELOCITY + PLAYER_WIDTH <= WIDTH:
            player.x += PLAYER_VELOCITY
        if keys[pygame.K_UP] and player.y - PLAYER_VELOCITY >= 0:
            player.y -= PLAYER_VELOCITY
        if keys[pygame.K_DOWN] and player.y + PLAYER_VELOCITY + PLAYER_HEIGHT <= HEIGHT:
            player.y += PLAYER_VELOCITY

        
        #DRAW THE CODE
        draw(player)
        

if __name__ == "__main__":
    main()
