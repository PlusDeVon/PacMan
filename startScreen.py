import pygame
import settings_menu

pygame.init()

# Screen resolution
res = (800, 600)     
screen = pygame.display.set_mode(res)
pygame.display.set_caption("PacMan")

# "Pacman" text at the top
font = pygame.font.SysFont("Arial", 80)
text2 = font.render("Pac-man", True, (255, 165, 0))  # Orange color
text2_rect = text2.get_rect(center=(res[0] // 2, 180))  # Adjust Y to be at the top

# "Start" button in the center
font = pygame.font.SysFont("Arial", 80)
text = font.render("Start", True, (255, 255, 255))  
text_rect = text.get_rect(center=(res[0] // 2, res[1] // 2))  # Center of the screen
start_button_rect = text.get_rect(topright=(res[0] -40,res[1] -580))

button_padding = 20  # Padding around the text
button_color = (255, 165, 0)  # Orange color
button_rect = text_rect.inflate(button_padding * 2, button_padding * 2)  # Inflate to add padding


# Settings button at the top right corner
small_font = pygame.font.SysFont("Arial", 30)
settings_button = small_font.render("Settings", True, (0, 0, 0)) # settings button
settings_button_rect = settings_button.get_rect(topright=(res[0] -40,res[1] -580)) # position settings button at top right corner

running = True
while running:
    screen.fill((0, 0, 0))  # Fill the screen with black

    # Draw the text
    screen.blit(text2, text2_rect)  # Draw "Pacman" at the top
    screen.blit(text, text_rect)  # Draw "Start" button

    rect = pygame.Rect(res[0]-140, 20, 110, 40) #(X position, Y position, width, height)
    pygame.draw.rect(screen, (255, 255, 255), rect) # Draw white rectangle for settings button background
    screen.blit(settings_button, settings_button_rect)  # Draw settings button

    

    # Check for mouse events
    mouse_pos = pygame.mouse.get_pos()  # Get the current mouse position
    mouse_click = pygame.mouse.get_pressed()  # Check if the mouse is clicked

    if pygame.event.get(pygame.MOUSEBUTTONDOWN): #checks if mouse button is clicked
        if rect.collidepoint(mouse_pos): # checks if mouse is over settings button
            settings_menu_instance = settings_menu.SettingsMenu(screen) # Create an instance of SettingsMenu
            in_settings = True
            while in_settings:
                for event in pygame.event.get():
                    selected_option = settings_menu_instance.keyboard_option_selector(event) or settings_menu_instance.mouse_option_selector(event)

                    if selected_option == "Graphics":
                        pass

                    elif selected_option == "Sound":
                        pass

                    elif selected_option == "Controls":
                        pass

                    elif selected_option == "Restart": # Restart the game/level (undecided)
                        settings_menu_instance.restart_game()
                    elif selected_option == "Back": # Go back to main menu or current game
                        in_settings = False
                    elif selected_option == "Exit Game" or event.type == pygame.QUIT: # Exit the game
                        running = False
                        in_settings = False
                settings_menu_instance.draw(res)
        elif button_rect.collidepoint(mouse_pos): # checks if mouse is over start button
            print("Start button clicked!")
            # Here you can add code to transition to the game screen

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()  # Update the screen

pygame.quit()