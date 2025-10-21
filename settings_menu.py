import pygame

#Need to decide how each menu will be structured
#Graphics: resolution, fullscreen/windowed
#Sound: volume, mute/unmute
#Controls: key bindings
#Restart game: restart from level one(or perhaps restart current level)
#Back: return to current game(if settings is used during game) or main menu(if already on main menu)


class SettingsMenu:
    def __init__(self, screen): # A layer is created for settings menu
        self.screen = screen
        self.font = pygame.font.Font(None, 50) #sets the font in menu
        self.options = ["Graphics", "Sound", "Controls", "Restart","Back", "Exit Game"] #menu options
        self.selected_option = 0 #defaults to first option

    def draw(self):
        self.screen.fill((0, 0, 0)) #fill the screen with black
        for index, option in enumerate(self.options):
            color = (255, 255, 255) if index == self.selected_option else (100, 100, 100) #selected option is white otherwise grey
            text_surface = self.font.render(option, True, color) #renders the text with the self.font, turns on anti-aliasing and sets the color with above line
            self.screen.blit(text_surface, (100, 100 + index * 40)) #draws the text at the specified position
        pygame.display.flip()

    def keyboard_option_selector(self, event):  #menu navigation via keyboard (up/down then press enter to select)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif event.key == pygame.K_DOWN: 
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                return self.options[self.selected_option]
        return None
    
    def mouse_option_selector(self, event):  #menu navigation via mouse (hover then click to select)
        if event.type == pygame.MOUSEMOTION:
            mouse_y = event.pos[1]
            for index in range(len(self.options)):
                option_y = 100 + index * 40
                if option_y <= mouse_y <= option_y + 30:  #30 is approx height of text
                    self.selected_option = index
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  #left mouse button
                return self.options[self.selected_option]
        return None