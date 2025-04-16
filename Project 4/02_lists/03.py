import pygame
import sys

pygame.init()

WINDOW_SIZE = 800
GRID_SIZE = 20
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
ERASER_SIZE = 40

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Canvas Eraser")

grid = [[BLUE for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

eraser_pos = [0, 0]
dragging = False

def draw_grid():
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, grid[y][x], rect)
            pygame.draw.rect(screen, BLACK, rect, 1) 

def draw_eraser():
    eraser_rect = pygame.Rect(eraser_pos[0] - ERASER_SIZE//2, 
                            eraser_pos[1] - ERASER_SIZE//2, 
                            ERASER_SIZE, ERASER_SIZE)
    pygame.draw.rect(screen, GRAY, eraser_rect)
    pygame.draw.rect(screen, BLACK, eraser_rect, 2)

def erase_cells():
    eraser_rect = pygame.Rect(eraser_pos[0] - ERASER_SIZE//2, 
                            eraser_pos[1] - ERASER_SIZE//2, 
                            ERASER_SIZE, ERASER_SIZE)
    
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            cell_rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if eraser_rect.colliderect(cell_rect):
                grid[y][x] = WHITE

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                dragging = True
                eraser_pos = list(event.pos)
                erase_cells()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: 
                dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                eraser_pos = list(event.pos)
                erase_cells()
    
    screen.fill(WHITE)
    draw_grid()
    draw_eraser()
    pygame.display.flip()

pygame.quit()
sys.exit()
