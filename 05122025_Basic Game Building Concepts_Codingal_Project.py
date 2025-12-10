import pygame
pygame.init()
display_surface = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game screen")
WHITE = (255, 255, 255)
display_surface.fill(WHITE)
text = pygame.font.Font(None, 36).render("Hello, World!", True,
                                         pygame.Color("black"))
text_rect = text.get_rect(center=(320, 350))
pygame.draw.rect(display_surface, (0, 125, 255), pygame.Rect(280, 200, 90, 40))
def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display_surface.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__ == "__main__":
    game_loop()