import pygame
import math 
import random

pygame.init()

def init_all_words():
    word_list = []
    f = open("words.txt", "r")
    for line in f:
        if len(line.strip()) == 5:
            word_list.append(line.strip())

    return word_list

def draw_keyboard():
    spacing = 4
    font = pygame.font.Font('freesansbold.ttf', 32)
    rows = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

    for i in range(3):
        startx = WIDTH/2 - len(rows[i])*(KEYBOARD_SIZE + spacing)/2
        starty = HEIGHT - (3.2-i)*(KEYBOARD_SIZE+spacing)
        for j in range(len(rows[i])):
            key_colour = UNKNOWN_KEY_COLOUR
            if rows[i][j] in guessed_letters:
                if rows[i][j] in actual_word: key_colour = CORRECT_KEY_COLOUR
                else: key_colour = WRONG_KEY_COLOUR

            pygame.draw.rect(screen, key_colour, pygame.Rect(startx, starty, KEYBOARD_SIZE, KEYBOARD_SIZE))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(startx, starty, KEYBOARD_SIZE, KEYBOARD_SIZE), 2)
            text = font.render(rows[i][j], True, (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (startx + KEYBOARD_SIZE/2, starty+KEYBOARD_SIZE/2)
            screen.blit(text, textRect)

            startx += KEYBOARD_SIZE + spacing

def draw_grid():
    font = pygame.font.Font('freesansbold.ttf', 40)
    spacing = 4
    startx = WIDTH/2 - 2.5*(TILE_SIZE+spacing)
    starty = spacing*3
    for i in range(6):
        for j in range(5):
            key_colour = UNKNOWN_KEY_COLOUR
            if rows_colours[i][j] == "g":
                key_colour = CORRECT_KEY_COLOUR	
            elif rows_colours[i][j] == "o":
                key_colour = NEARLY_KEY_COLOUR	
            elif rows_colours[i][j] == "w":
                key_colour = WRONG_KEY_COLOUR	

            pygame.draw.rect(screen, key_colour, pygame.Rect(startx, starty, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(startx, starty, TILE_SIZE, TILE_SIZE), 2)

            if i == current_pos[1] and current_pos[0] == j:
                pygame.draw.line(screen, (0, 0, 0), (startx+0.1*TILE_SIZE, starty+0.86*TILE_SIZE), (startx+0.9*TILE_SIZE, starty+0.86*TILE_SIZE), 2)

            if rows[i][j] != "":
                text = font.render(rows[i][j], True, (0, 0, 0))
                textRect = text.get_rect()
                textRect.center = (startx + TILE_SIZE/2, starty+TILE_SIZE/2)
                screen.blit(text, textRect)

            startx += TILE_SIZE+spacing
        startx = WIDTH/2 - 2.5*(TILE_SIZE+spacing)
        starty += TILE_SIZE+spacing*2

def enter_guess():
    if current_pos[1] <= 0: return
    y = current_pos[1]-1
    for x in range(5):
        guessed_letters.add(rows[y][x])
    
    for x in range(5):
        if rows[y][x] == actual_word[x]:
            rows_colours[y][x] = "g"
        elif rows[y][x] != actual_word[x] and rows[y][x] not in actual_word:
            rows_colours[y][x] = "w"
        else:
            rows_colours[y][x] = "o"
        


def start_game():
    rows.clear()
    guessed_letters.clear()
    for i in range(6):
        rows.append([""] * 5)
        rows_colours.append([""] * 5)
    current_pos.clear()
    current_pos.append(0)
    current_pos.append(0)
    

WIDTH = 600
HEIGHT = 600
TILE_SIZE = 60
KEYBOARD_SIZE = 50
ALL_WORDS = init_all_words()
UNKNOWN_KEY_COLOUR = (245, 217, 182)
CORRECT_KEY_COLOUR = (142, 242, 114)
NEARLY_KEY_COLOUR = (142, 242, 114)
WRONG_KEY_COLOUR = (242, 137, 114)
LETTERS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
running = True
guessed_letters = set()
rows = []
rows_colours = []
actual_word = "ABCDE"
current_pos = [0, 0]

lost = False
won = False

BACKGROUND_COLOUR = (224, 198, 153)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wordle")

start_game()

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if (event.button == 1):
                pass
        
        if event.type == pygame.KEYUP:
            if pygame.K_a <= event.key <= pygame.K_z: 
                k = event.key - 97
                if current_pos[0] < 5:
                    rows[current_pos[1]][current_pos[0]] = LETTERS[k]
                    current_pos[0] += 1
            elif event.key == pygame.K_BACKSPACE:
                if current_pos[0] > 0:
                    current_pos[0] -= 1
                    rows[current_pos[1]][current_pos[0]] = ""
            elif event.key == pygame.K_RETURN:
                if current_pos[0] < 5: continue
                current_pos[1] += 1
                current_pos[0] = 0
                print(current_pos)
                
        

                                   
    screen.fill(BACKGROUND_COLOUR) 
    draw_grid()
    draw_keyboard()  
        
    pygame.display.flip()

pygame.quit()