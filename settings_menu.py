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
        self.options = ["Graphics", "Sound", "Controls","Restart", "Back", "Exit Game", 
                        "Resolution", "Fullscreen/Windowed", "Back",
                        "Master Volume", "Music Volume", "Sound Effects Volume", "Mute/Unmute", "Back",
                        "Rebind Keys", "Back"] # Number of things in each section (6,3,5,2)
        self.selected_option = 0 #defaults to first option

    def draw(self, res, settings_state=0):
        self.screen.fill((0, 0, 0)) # Clear screen with black
        if settings_state == 0:
            for index, option in enumerate(self.options[0:6], start=0): # Graphics, Sound, Controls, Back, Exit Game
                color = (255, 255, 255) if index == self.selected_option else (100, 100, 100)# Highlight selected option
                text = self.font.render(option, True, color) # Render text
                self.screen.blit(text, (100, 100 + index * 40)) # Draw text
            pygame.display.flip()
        elif settings_state == 1:
            for index, option in enumerate(self.options[6:9], start=6): # Resolution, Fullscreen/Windowed, Back
                color = (255, 255, 255) if index == self.selected_option else (100, 100, 100)
                text = self.font.render(option, True, color)
                self.screen.blit(text, (100, 100 + index * 40))
            pygame.display.flip()
        elif settings_state == 2:
            for index, option in enumerate(self.options[9:14], start=9): # Master Volume, Music Volume, Sound Effects Volume, Mute/Unmute, Back
                color = (255, 255, 255) if index == self.selected_option else (100, 100, 100)
                text = self.font.render(option, True, color)
                self.screen.blit(text, (100, 100 + (index - 8) * 40))
            pygame.display.flip()
        elif settings_state == 3:
            for index, option in enumerate(self.options[14:15], start=14): # Rebind Keys, Back
                color = (255, 255, 255) if index == self.selected_option else (100, 100, 100)
                text = self.font.render(option, True, color)
                self.screen.blit(text, (100, 100 + (index - 13) * 40))
        pygame.display.flip()



    #volume control (call between 0.0 and 1.0)
    def adjust_volume(self, level, channel=0): #in main be sure to have a variable to apply master volume as a percent of the other two. for example, music volume = master volume * music volume setting
        if channel == 0:  # Master volume
            pygame.mixer.music.set_volume(level)
            pygame.mixer.Sound.set_volume(level)
        elif channel == 1:  # Music volume
            pygame.mixer.music.set_volume(level)
        elif channel == 2:  # Sound effects volume
            pygame.mixer.Sound.set_volume(level)
    
    #mute/unmute control
    def mute_unmute(self, level, mute=True, channel=0):
        if mute:
            if channel == 0:  # Master mute
                pygame.mixer.music.set_volume(0)
                pygame.mixer.Sound.set_volume(0)
            elif channel == 1:  # Music mute
                pygame.mixer.music.set_volume(0)
            elif channel == 2:  # Sound effects mute
                pygame.mixer.Sound.set_volume(0)
        else:
            if channel == 0:  # Master unmute
                pygame.mixer.music.set_volume(level)
                pygame.mixer.Sound.set_volume(level)
            elif channel == 1:  # Music unmute
                pygame.mixer.music.set_volume(level)
            elif channel == 2:  # Sound effects unmute
                pygame.mixer.Sound.set_volume(level)
    



    #restart game
    def restart_game(self): # placeholder
        pass


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
            mouse_x = event.pos[0]
            for index in range(len(self.options)):
                option_y = 100 + index * 40
                # determine the rendered text width so we can check horizontal proximity
                text = self.options[index]
                text_width, text_height = self.font.size("Exit Game") # use the largest option to get consistent width
                text_x = 100  # x position used in draw()

                # vertical check (approx height of text)
                if option_y <= mouse_y <= option_y + text_height:
                    # horizontal proximity: within 30 pixels of text bounds
                    if (mouse_x >= text_x - 30) and (mouse_x <= text_x + text_width + 30):
                        self.selected_option = index
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  #left mouse button
                return self.options[self.selected_option]
        return None
    def selector(self,event):
        return self.mouse_option_selector(event) or self.keyboard_option_selector(event)