import pygame
from PetriDish import PetriDish
from Constants import Constants

def main():
    pygame.init()

    petriDish = PetriDish()
    petriDish.setup()
 
    # Set the height and width of the screen
    size = [petriDish.getWidth(), petriDish.getHeight()]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("ML Petri Dish")
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    # -------- Main Program Loop -----------
    while not done:
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
 
        # --- Logic
        petriDish.updateDish()
 
        # --- Drawing
        # Set the screen background
        screen.fill(Constants.DISH_COLOR)
 
        for entity in petriDish.getEntities():
            pygame.draw.circle(screen, entity.getColor(), [int(entity.getMyX()), int(entity.getMyY())], entity.getRadius())
        for microbe in petriDish.getMicrobes():
            pygame.draw.circle(screen, microbe.getColor(), [int(microbe.getMyX()), int(microbe.getMyY())], microbe.getRadius())
 
        # --- Wrap-up
        # Limit to 60 frames per second
        clock.tick(5)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()