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
        self.options = ["Graphics", "Sound", "Controls", "Restart","Back", "Exit Game"] # menu options
        self.graphics_options = ["Resolution", "Fullscreen/Windowed", "Back"] # sub options for graphics
        self.sound_options = ["Master Volume", "Music Volume", "Sound Effects Volume", "Mute/Unmute", "Back"] # sub options for sound
        self.controls_options = ["Rebind Keys", "Back"] # sub options for controls
        self.selected_option = 0 #defaults to first option

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
    


    def draw(self, res):
        self.screen.fill((0, 0, 0)) #fill the screen with black
        for index, option in enumerate(self.options):
            color = (255, 255, 255) if index == self.selected_option else (100, 100, 100) #selected option is white otherwise grey
            main_text_surface = self.font.render(option, True, color) #renders the text with the self.font, turns on anti-aliasing and sets the color with above line
            self.screen.blit(main_text_surface, (50, 100 + index * 40)) #draws the text at the specified position
        pygame.display.flip()

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
    

class SubSettingsMenu():
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 50) #sets the font in menu
        self.graphics_options = ["Resolution", "Fullscreen/Windowed", "Back"] # sub options for graphics
        self.sound_options = ["Master Volume", "Music Volume", "Sound Effects Volume", "Mute/Unmute", "Back"] # sub options for sound
        self.controls_options = ["Rebind Keys", "Back"] # sub options for controls
        self.selected_option = 0 #defaults to first option

    def mouse_option_selector(self, event):  #menu navigation via mouse (hover then click to select)
        if event.type == pygame.MOUSEMOTION:
            mouse_y = event.pos[1]
            mouse_x = event.pos[0]
            for index in range(len(self.sound_options)):
                option_y = 100 + index * 40
                # determine the rendered text width so we can check horizontal proximity
                text = self.graphics_options[index]
                text_width, text_height = self.font.size("Fullscreen/Windowed") # use the largest option to get consistent width
                text_x = 100  # x position used in draw()

                # vertical check (approx height of text)
                if option_y <= mouse_y <= option_y + text_height:
                    # horizontal proximity: within 30 pixels of text bounds
                    if (mouse_x >= text_x - 30) and (mouse_x <= text_x + text_width + 30):
                        self.selected_option = index
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  #left mouse button
                return self.graphics_options[self.selected_option]
        return None



    def draw_graphics_submenu(self, res):
        self.screen.fill((0, 0, 0)) #fill the screen with black
        sub_text_surface = None
        for sub_index, sub_option in enumerate(self.graphics_options):
            color = (255, 255, 255) if sub_index == self.selected_option else (150, 150, 150)
            sub_text_surface = self.font.render(sub_option, True, color)
            self.screen.blit(sub_text_surface, (60, 100 + sub_index * 40))
        pygame.display.flip()


    def draw_sound_submenu(self, res, option):
        self.screen.fill((0, 0, 0)) #fill the screen with black
        sub_text_surface = None
        for sub_index, sub_option in enumerate(self.sound_options):
            color = (255, 255, 255) if sub_index == self.selected_option else (150, 150, 150)
            sub_text_surface = self.font.render(sub_option, True, color)
            self.screen.blit(sub_text_surface, (60, 70 + sub_index * 40))
        pygame.display.flip()

    def draw_controls_submenu(self, res, option):
        self.screen.fill((0, 0, 0)) #fill the screen with black
        sub_text_surface = None
        for sub_index, sub_option in enumerate(self.controls_options):
            color = (255, 255, 255) if sub_index == self.selected_option else (150, 150, 150)
            sub_text_surface = self.font.render(sub_option, True, color)
            self.screen.blit(sub_text_surface, (60, 70 + sub_index * 40))
        pygame.display.flip()


    #fullscreen/windowed
    def toggle_fullscreen(self):
        pygame.display.toggle_fullscreen()
    
    #resolution change
    def change_resolution(self, ratio):
        res = [[3840,2160],[2560,1440],[1920,1080],[1280,780],[1080,480],[800,600]] #Resolution options
        pygame.display.set_mode((res[ratio][1], res[ratio][0]))
    
    #key bindings
    def rebind_key(self, action, new_key): # placeholder
        pass
    


        