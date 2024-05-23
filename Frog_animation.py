import pygame, sys

class Player(pygame.sprite.Sprite):
  def __init__(self, pos_x, pos_y):
      super().__init__()
      # Adding sprite images to sprites list
      self.sprites = []
      self.is_animating = False
      self.sprites.append(pygame.image.load('Graphics/attack_1.png'))
      self.sprites.append(pygame.image.load('Graphics/attack_2.png'))
      self.sprites.append(pygame.image.load('Graphics/attack_3.png'))
      self.sprites.append(pygame.image.load('Graphics/attack_4.png'))
      self.sprites.append(pygame.image.load('Graphics/attack_5.png'))
      self.sprites.append(pygame.image.load('Graphics/attack_6.png'))
      self.sprites.append(pygame.image.load('Graphics/attack_7.png'))
      self.sprites.append(pygame.image.load('Graphics/attack_8.png'))
      self.sprites.append(pygame.image.load('Graphics/attack_9.png'))
      self.sprites.append(pygame.image.load('Graphics/attack_10.png'))
      self.current_sprite = 0
      self.image = self.sprites[self.current_sprite]
      # Generating rectangles for images and positioning image/rect
      self.rect = self.image.get_rect()
      self.rect.topleft = [pos_x, pos_y]

  def animate(self):
    self.is_animating = True

  def update(self, speed):
    if self.is_animating == True:
      self.current_sprite +=speed

      if self.current_sprite >= len(self.sprites):
        self.current_sprite = 0
        self.is_animating = False

      self.image = self.sprites[int(self.current_sprite)]


# General setup
pygame.init()
clock = pygame.time.Clock()

# Game screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")

# Create the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(70,100)
moving_sprites.add(player)

# Main game loop --------------------------------------------------
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit

    if event.type == pygame.KEYDOWN:
      player.animate()

  # Drawing ----------
  screen.fill((0,0,0))
  moving_sprites.draw(screen)
  moving_sprites.update(0.2
                        )
  pygame.display.flip()
  clock.tick(60)
  
