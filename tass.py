import pygame
import speech_recognition as sr
import os
import webbrowser as wb
pygame.init()

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

display_width = 1366
display_height = 768

black = (0, 0, 0)
alpha = (0, 88, 255)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (100, 55, 80)
cyan = (146,229,255)
dullorange = (255,169,82)
dullyellow = (214,233,91)
grey = (150,150,150)
maroon = (209,77,77)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('TASS')

gameDisplay.fill(white)
image = pygame.image.load('img.jpg')
image = pygame.transform.scale(image, (1366, 768))
gameDisplay.blit(image, (0,0))

def search():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print ('Say Something!')
        audio = r.listen(source)
        print ('Done!')

    try:
        text = r.recognize_google(audio)

        f_text = 'https://www.google.co.in/search?q=' + text
        wb.get(chrome_path).open(f_text)

    except:
        message_display("OOPS! Could not recognize your voice")


def s2t():
    gameDisplay.blit(image, (0, 0))
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print ('Say Something!')
        audio = r.listen(source)
        print ('Done!')
        try:
            text = r.recognize_google(audio)
            message_display(text.upper())
            print (text.upper())
            with open('new.txt', 'w') as data_file:

             data_file.write(text)
            os.startfile('new.txt')

        except:
            message_display("OOPS! Could not recognize your voice")




def close():
    pygame.quit()
    quit()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 1.5), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("Times New Roman", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()



        button("Speak", 100, 400, 100, 50, cyan, alpha, s2t)
        button("Search", 100, 500, 100, 50, dullyellow, dullorange, search)
        button("Quit", 100, 600, 100, 50, maroon, bright_red, close)
        pygame.display.update()


if __name__ == '__main__':
    main()
