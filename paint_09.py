import pygame, sys, math

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

done = False

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Drawing Functions
def drawRect(color, pos, width, height):
    pygame.draw.rect(screen, color, (pos[0], pos[1], width, height), 4)

def drawCircle(color, pos, RAD):
    pygame.draw.circle(screen, color, pos, RAD, 4)

def eraser(pos, RAD):
    pygame.draw.circle(screen, WHITE, pos, RAD)

def drawSquare(color, pos, side_length):
    pygame.draw.rect(screen, color, (pos[0], pos[1], side_length, side_length), 4)

def drawRightTriangle(color, pos, base, height):
    points = [(pos[0], pos[1] + height), (pos[0] + base, pos[1] + height), (pos[0] + base, pos[1])]
    pygame.draw.polygon(screen, color, points, 4)

def drawEquilateralTriangle(color, pos, side_length):
    height = side_length * math.sqrt(3) / 2
    points = [(pos[0], pos[1] + height), (pos[0] + side_length / 2, pos[1]), (pos[0] + side_length, pos[1] + height)]
    pygame.draw.polygon(screen, color, points, 4)

def drawRhombus(color, pos, diagonal_h, diagonal_v):
    half_h = diagonal_h / 2
    half_v = diagonal_v / 2
    points = [
        (pos[0], pos[1] - half_v),  # Top
        (pos[0] + half_h, pos[1]),  # Right
        (pos[0], pos[1] + half_v),  # Bottom
        (pos[0] - half_h, pos[1])   # Left
    ]
    pygame.draw.polygon(screen, color, points, 4)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y + 90)
    pygame.draw.rect(surface, WHITE, (textrect.topleft, (textrect.width + 50, textrect.height + 5)))
    surface.blit(textobj, textrect)

font = pygame.font.SysFont(None, 36)

RAD = 30
drawing = False
color = BLACK

screen.fill(pygame.Color('white'))
rainbow = pygame.image.load('color.jpg')
rainbow = pygame.transform.scale(rainbow, (100, 100))

mode = 0
mode_name = ['rect', 'circle', 'eraser', 'pencil', 'square', 'right tri', 'equil tri', 'rhombus']

while not done:
    clock.tick(FPS)
    pos = pygame.mouse.get_pos()
    screen.blit(rainbow, (0, 0))
    draw_text('Mode: ' + str(mode_name[mode]), font, BLACK, screen, 10, 10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = pos
            if pos[0] > 20 and pos[0] < 100 and pos[1] > 20 and pos[1] < 100:
                color = screen.get_at(pos)
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = pos
            rect_x = abs(start_pos[0] - end_pos[0])
            rect_y = abs(start_pos[1] - end_pos[1])

            if mode == 0:
                drawRect(color, start_pos, rect_x, rect_y)
            elif mode == 1:
                drawCircle(color, start_pos, rect_x)
            elif mode == 4:
                side_length = max(rect_x, rect_y)
                drawSquare(color, start_pos, side_length)
            elif mode == 5:
                drawRightTriangle(color, start_pos, rect_x, rect_y)
            elif mode == 6:
                side_length = min(rect_x, rect_y)
                drawEquilateralTriangle(color, start_pos, side_length)
            elif mode == 7:
                drawRhombus(color, start_pos, min(rect_x, rect_y), 45)

        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == 2:
                eraser(pos, RAD)
            elif mode == 3:
                if start_pos:
                    pygame.draw.line(screen, color, start_pos, pos, 2)
                start_pos = pos

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mode = (mode + 1) % 8
                if mode == 2:
                    color = WHITE
            if event.key == pygame.K_BACKSPACE:
                screen.fill(pygame.Color('white'))

    pygame.display.flip()

pygame.quit()
sys.exit()
