import pygame
from sys import exit

# Initializes pygame to do different types of works like pictures sound etc
pygame.init() # Should always call it

HEIGHT,WIDTH = 800,400
screen = pygame.display.set_mode((HEIGHT,WIDTH)) #Creats a display screen with (WIDTH,HEIGHT)
#Title
pygame.display.set_caption("Jummpy")
#Create a constant FPS (helps in maintain massive sys based errors)
clock = pygame.time.Clock()
#Font (Creates a font)
Tfont = pygame.font.Font('Font/pixeltype.ttf',50) #(<font_type>,size)


#Creating a basic surface to display on the main screen
#Plain Colour
# test_surface = pygame.Surface((100,200))
# test_surface.fill('Red') # Can use hex code

#Image 
sky_surface = pygame.image.load('Graphics/Sky.png').convert_alpha() #Converts the image into something that pygame can work with easily 
ground_surface = pygame.image.load('Graphics/ground.png').convert_alpha()

#Text
text_surface  = Tfont.render('Jummpy',False,'Black') #(<Text to display>,anti aliasing ,colour)
#Anti aliasing smooths the text (not for pixel arts)
text_rect = text_surface.get_rect(center=(400,100))

#Animation and other things
snail_surface = pygame.image.load('Graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600,300))
#Rectangle (Helps positioning stuff precisely also help in detect collision)
player_sruf = pygame.image.load('Graphics/Player/player_walk_1.png').convert_alpha()
player_rec = player_sruf.get_rect(midbottom=(80,300)) #takes the surface and creates it into a rectangle Syntax: (<place> =(x,y))







while True:
  #Check if the close button is clicked to close the game and console
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: #QUIT is a constant
      pygame.QUIT #you cannot use pygame.quit() because it quites pygame and dosent allow update statement to run
      exit()
    #Check for mouse button press
    # if event.type == pygame.MOUSEMOTION: #Can also use MOUSEBUTTONDOWN == True == When clicked , MOUSEBUTTONUP == True == When released
    #   if player_rec.collidepoint(event.pos):
    #     print('Perfect Collision')

  #Displays regular surface in main screen
  screen.blit(sky_surface,(0,0)) #Block image transform (puts one surface on the other) Syntax : <screen_name>.blit(<sub_screen>,position)
  screen.blit(ground_surface,(0,300)) #blit screen placing is ordered 
  screen.blit(text_surface,text_rect)

  #Increases snail_x_pos constantly
  # snail_x_pos -= 4
  # If snail leaves the screen and to bring it back
  # if snail_x_pos < -50:
  #   snail_x_pos = 800
  snail_rect.left -= 4
  if snail_rect.right <= 0:
    snail_rect.left = 800
    # it dosen't clear the previous frame so always load moving item on a background
  screen.blit(snail_surface,snail_rect)
  player_rec.left += 1 #Moves the rectangle 
  #print(<rect_name>.<pos>) prints the coords of the pos
  screen.blit(player_sruf,player_rec)
  #Collisions
  # if player_rec.colliderect(snail_rect):
  #   print('Collision') # Check every frame if there is collision not for health based games
  #Collide point (For mouse)
  #Check the mouse position

  # mos_pos =pygame.mouse.get_pos()
  # if player_rec.collidepoint(mos_pos):
  #   print(pygame.mouse.get_pressed()) #prints collision everytime the mouse hovers over the player
# Print (False,False,False) for no clicks 
# Right click == (False,False,True)
# Left click == (True,False,False)
# Middle click == (False,True,False)

  #Draw all elements
  #Updates everything
  pygame.display.update() #Update statement
  clock.tick(60) #Tells that the while loop shouldn't run more than 60x a second
