import pygame
from sys import exit

def dis_score():
  cur_time =  int(pygame.time.get_ticks()/1000) - start_time
  score_surf = Tfont.render(f'Score: {cur_time}',False,(64,64,64))
  score_rect = score_surf.get_rect(center=(400,50))
  screen.blit(score_surf,score_rect)
  return cur_time
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
game_state = True
start_time = 0
score = 0

#Creating a basic surface to display on the main screen
#Plain Colour
# test_surface = pygame.Surface((100,200))
# test_surface.fill('Red') # Can use hex code

#Image 
sky_surface = pygame.image.load('Graphics/Sky.png').convert_alpha() #Converts the image into something that pygame can work with easily 
ground_surface = pygame.image.load('Graphics/ground.png').convert_alpha()

#Text
# text_surface  = Tfont.render('Score',False,(64,64,64)) #(<Text to display>,anti aliasing ,colour)
#Anti aliasing smooths the text (not for pixel arts)
# text_rect = text_surface.get_rect(center=(400,50))


#Animation and other things
snail_surface = pygame.image.load('Graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600,300))
#Rectangle (Helps positioning stuff precisely also help in detect collision)
player_sruf = pygame.image.load('Graphics/Player/player_walk_1.png').convert_alpha()
player_rec = player_sruf.get_rect(midbottom=(100,300)) #takes the surface and creates it into a rectangle Syntax: (<place> =(x,y))
player_grav = 0
player_end = pygame.image.load('Graphics/Player/player_stand.png').convert_alpha()
player_end = pygame.transform.rotozoom(player_end,0,2) #(surface,angle,size)
playend_rect = player_end.get_rect(center=(400,200))
Game_over = Tfont.render("Game Over",False,(111,196,196))
game_over_rect = Game_over.get_rect(center=(400,80))
play_again = Tfont.render("Press Space to Start",False,(111,196,196))
play_again_rect = play_again.get_rect(center=(400,350))






while True:
  #Check if the close button is clicked to close the game and console
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: #QUIT is a constant
      pygame.QUIT #you cannot use pygame.quit() because it quites pygame and dosent allow update statement to run
      exit()
    # Gravity  eff
    if game_state == True:
      if event.type == pygame.MOUSEBUTTONDOWN and player_rec.bottom == 300:
        if player_rec.collidepoint(event.pos): 
          player_grav = -20
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE and player_rec.bottom == 300:
          player_grav = -20
    else:
      if event.type == pygame.KEYDOWN and  event.key == pygame.K_SPACE:
        game_state = True
        snail_rect.left = 800
        start_time = int(pygame.time.get_ticks()/1000)

            
    #Check for mouse button press
    # if event.type == pygame.MOUSEMOTION: #Can also use MOUSEBUTTONDOWN == True == When clicked , MOUSEBUTTONUP == True == When released
    #   if player_rec.collidepoint(event.pos):
    #     print('Perfect Collision')

  #Displays regular surface in main screen
  if game_state == True:
    screen.blit(sky_surface,(0,0)) #Block image transform (puts one surface on the other) Syntax : <screen_name>.blit(<sub_screen>,position)
    screen.blit(ground_surface,(0,300)) #blit screen placing is ordered 
    score = dis_score()
    #Drawing images on the screen using rectangles
    #Pygame.draw (Can be used to draw rect , circle , polygons etc)
    #pygame.draw.rect(screen,'#c0e8ec',text_rect) #Syntax : (surface to display on,Colour,rect that should be drawn,optional margin or border only)
    #pygame.draw.rect(screen,'#c0e8ec',text_rect,10)
    #screen.blit(text_surface,text_rect)

    #Drawing a line across the screen 
    #pygame.draw.line(screen,'Gold',(0,0),pygame.mouse.get_pos(),10)

    # Drawing a rect with a different border and fill colour

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
    player_grav += 1
    player_rec.y += player_grav 
    if player_rec.bottom >= 300:
      player_rec.bottom = 300
    #player_rec.left += 1 #Moves the rectangle 
    #print(<rect_name>.<pos>) prints the coords of the pos
    screen.blit(player_sruf,player_rec)
    dis_score()

    if snail_rect.colliderect(player_rec):
      game_state = False 

  else:
    screen.fill((94,129,162))
    screen.blit(player_end,playend_rect)
    
    score_msg=Tfont.render(f'Your Score: {score}',False,(111,196,196))
    score_msg_rect = score_msg.get_rect(center=(400,330))
    if score == 0:
      screen.blit(play_again,play_again_rect)
    else:
      screen.blit(score_msg,score_msg_rect)

    screen.blit(Game_over,game_over_rect)

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

  
#Player
#1) Keyboard inputs
  # Using pygame.key.get_pressed
  # keys = pygame.key.get_pressed() #shows a list of keys press 0 == false , 1 == true
  # if keys[pygame.K_SPACE]:
  #   print("Jump")
  # using event loop
  # if event.type == pygame.KEYUP:
  #   if event.key == pygame.K_SPACE:
  #     print('Jump')
  # elif event.type == pygame.KEYDOWN:
  #   print('Key Down')
#2) Jump
#3) Floor

#Game Over Mechanics
#Score 
#Transforming a surface 
  #Draw all elements
  #Updates everything
  pygame.display.update() #Update statement
  clock.tick(60) #Tells that the while loop shouldn't run more than 60x a second
