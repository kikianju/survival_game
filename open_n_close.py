import pygame
import random

# 1 -게임 변수 초기화
# 2 - 게임 변수 초기화
    # 2-1 게임 화면
pygame.init()
screen = pygame.display.set_mode((480, 640))

# 2-1 시간 관련 변수
FPS = 60
fpsClock = pygame.time.Clock()

try:
    # 3 이미지 및 효과음 삽입
        # 3-1 그림삽입
    spaceship_img = pygame.image.load("./img/johnny.png")
    asteroid0 = pygame.image.load("./img/asteroid0.png")
    asteroid1 = pygame.image.load("./img/asteroid1.png")
    asteroid2 = pygame.image.load("./img/asteroid2.png")
    asteroid_img = (asteroid0, asteroid1, asteroid2)
    game_over = pygame.image.load("./img/gameover.jpg")
        # 3-2 효과음
    take_off_sound = pygame.mixer.Sound("./sound/30lee_shin_iku")
    landing_sound = pygame.mixer.Sound("./sound/46shako_you_wanna_show_magic")
    take_off_sound.play()
except Exception as err:
    print('그림 또는 효과음 삽임에 문제가 있습니다. :', err)
    pygame.quit()
    exit(0)

# 게임 루프
running = True
while running:
    # 시작화면 흰색으로 채우기
    screen.fill((255, 255, 255))

    # 7 - 키보드 / 마우스 이벤트
    for event in pygame.event.get():
        # x버튼 클릭 시 게임 종료
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # 9 - 게임 상태 변경
            # 9-1 우주선 위치 / 그리기
        screen.blit(spaceship_img, (240, 600))
        landing_sound.play()
            # 9-2 asteroids 추가
        screen.blit(asteroid_img[0], (240, 320))

        # 10 - 게임속도
        fpsClock.tick(FPS)

        # 11 - 화면 전체 업데이트
        pygame.display.flip()
# 게임 종료
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        pygame.display.flip()
