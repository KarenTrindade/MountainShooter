import pygame

print('Setup Start')
pygame.init()
window = pygame.display.set_mode(size=(600, 400))  # Cria uma janela
print('Setup End')

print('Loop Start')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Quitting...')
            pygame.quit()  # Close Window
            quit()  # end pygame
