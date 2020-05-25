import sys

from pygame.constants import *
import game
import utils
import data_collector
import saves_manager



# Stats_listing : Create the best scores list window
def stats_listing(pygame, font, screen, screen_rect, userName):
    print("Stats list incoming")
    color = (255, 255, 255)
    active = False
    done = False
    #data = data_collector.get_file('src/scoreboard.json')

    savedGames = saves_manager.getBestScores()

### init every needed icons for the stats windows 
    #winner trophy
    trophy_first = pygame.image.load("img/medals/trophy_1.png").convert_alpha()
    trophy_first_s = pygame.transform.scale(trophy_first, (60, 60))
    
    #second trophy
    trophy_second = pygame.image.load("img/medals/trophy_2.png").convert_alpha()
    trophy_second_s = pygame.transform.scale(trophy_second, (60, 60))
    
    #third trophy
    trophy_third = pygame.image.load("img/medals/trophy_3.png").convert_alpha()
    trophy_third_s = pygame.transform.scale(trophy_third, (60, 60))


    ######################################### start : graphic layout for the scoreboard
    list_line_pos = [200, 290, 380, 470, 560]
 
    while not done:
        mx, my = pygame.mouse.get_pos() 
        utils.init_game_background(pygame, screen)              # Start the init_game_background function
        utils.draw_text('Scoreboard', font, (255, 255, 255), screen, 300, 50, True)                  # Draw the text menu

        top_rectangle = 200
        top_text_pos = 215

        #draw the medals cards
        for i in list_line_pos:
            pygame.draw.rect(screen, color, pygame.Rect(63, i, 80, 80))
            top_rectangle += 90
        
        # draw the user cards
        for i in list_line_pos:
            pygame.draw.rect(screen, color, pygame.Rect(145, i, 650, 80))
            top_rectangle += 90

        
        screen.blit(trophy_first_s, (73, 210))
        screen.blit(trophy_second_s, (73, 300))
        screen.blit(trophy_third_s, (73, 390))

        # Max 5 lines displayed
        currIndex = 0
        for savedGame in savedGames:
            if currIndex < 5:
                user_stat = savedGame[0] + " - " + savedGame[1]
                utils.draw_text(user_stat, font, (0, 0, 0), screen, 150, top_text_pos, False)
                top_text_pos += 90
            currIndex += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print("enter")
                if event.key == K_ESCAPE:
                    print("Escape has been pushed")
                    done = True

        pygame.display.flip()
