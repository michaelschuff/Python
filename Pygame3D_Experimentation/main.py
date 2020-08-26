import pygame

pygame.init()

window = pygame.display
window.set_mode([500, 500])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((255, 255, 255))
    window.flip()

pygame.quit()
