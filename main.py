import pygame

#ASSET LOAD
SHOOTER_IMAGE = pygame.image.load('assets/shooter.png')
BG = 'assets/bg.jpg'
SOUND1 = 'assets/screech1.mp3'

#CONSTANTS
FPS = 60
WIDTH, HEIGHT = 800, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 75, 65
PLAYER_VELOCITY = 12
SHOOTER_STARTING_X = WIDTH/2 - PLAYER_WIDTH/2
SHOOTER_STARTING_Y = HEIGHT - PLAYER_HEIGHT - 10
MAX_BULLETS = 3
BULLET_VEL = 3
SHOOTER_HIT = pygame.USEREVENT + 1

bullets= []
run = True

#CREATE CHARACTERS
SHOOTER_BOX = pygame.Rect(WIDTH/2 - PLAYER_WIDTH/2, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
SHOOTER = pygame.transform.rotate(pygame.transform.scale(SHOOTER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT)), 180)

#SET PROPERTIES
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge")
BG = pygame.transform.scale(pygame.image.load(BG).convert(),(WIDTH, HEIGHT))
TRANS = pygame.Surface((WIDTH, HEIGHT))
TRANS.set_alpha(128)
BG.blit(TRANS, (0,0))

#LOAD AND PLAY THE MAIN MUSIC FILE
def playSound(track):
    pygame.mixer.init()
    if track == 1:
        pygame.mixer.music.load(SOUND1)
        pygame.mixer.music.play(loops=2, start=1)
        pygame.mixer.music.set_volume(0.5)

def shooterMovement(keys, shooter):
    if keys[pygame.K_LEFT] and shooter.x - PLAYER_VELOCITY >= 0:
        shooter.x -= PLAYER_VELOCITY
    if keys[pygame.K_RIGHT] and shooter.x + PLAYER_VELOCITY + PLAYER_WIDTH <= WIDTH:
        shooter.x += PLAYER_VELOCITY
    if keys[pygame.K_UP] and shooter.y - PLAYER_VELOCITY >= 0:
        shooter.y -= PLAYER_VELOCITY
    if keys[pygame.K_DOWN] and shooter.y + PLAYER_VELOCITY + PLAYER_HEIGHT <= HEIGHT:
        shooter.y += PLAYER_VELOCITY

def fireMovement(bullets, shooter):
    for bullet in bullets:
        bullet.y -= BULLET_VEL
        if bullet.colliderect(shooter) or bullet.y < 0:
            pygame.event.post(pygame.event.Event(SHOOTER_HIT))
            bullets.remove(bullet)

#THE DRAWER
def draw(shooter, bullets):
    WIN.blit(BG, (0,0))
    WIN.blit(SHOOTER, (shooter.x, shooter.y))
    for bulle in bullets:
        pygame.draw.rect(WIN, 'red', bulle)
    #pygame.draw.rect(WIN, "red", player)
    pygame.display.update()


#THE MAIN FUNCTION
def main():
    playSound(1)
    shooter = pygame.Rect(SHOOTER_STARTING_X, SHOOTER_STARTING_Y, PLAYER_WIDTH, PLAYER_HEIGHT)

    #TICKS - Basically an FPS
    clock = pygame.time.Clock()

    global run
    while run:
        clock.tick(FPS)

        #EXIT CONDITION
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        shooterMovement(keys, shooter)

        if event.type == pygame.KEYDOWN:
            if ((event.key == pygame.K_RETURN) or (event.key == pygame.K_SPACE)) and (len(bullets) < MAX_BULLETS):
                bullet = pygame.Rect(shooter.x + shooter.width//2, shooter.y - 10, 2, 4)
                bullets.append(bullet)

        fireMovement(bullets, shooter)
        
        #DRAW THE DISPLAY
        draw(shooter, bullets)
        

if __name__ == "__main__":
    main()
