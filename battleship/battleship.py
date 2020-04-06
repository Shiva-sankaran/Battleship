import pygame
import math
import random
pygame.init()
from pygame.locals import (

    QUIT,
    KEYDOWN

)
screen_height = 680
screen_width =680



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.boats = []
        width = (screen_width//2) 
        height = (screen_height//2)
        self.surf = pygame.Surface((width, height))
        self.surf.fill((0,191,255))
        grid_width = 30
        grid_height = 30
        for i in range(20,width-20,grid_width):
        	for j in range(20,height-20,grid_height):
        		rect = pygame.Rect((i,j), (grid_width,grid_height))
        		pygame.draw.rect(self.surf, (0,0,0), rect,1)
        		
        		 
class AI(pygame.sprite.Sprite):
    def __init__(self):
        super(AI, self).__init__()
        self.boats = []
        width = screen_width//2
        height = screen_height//2
        self.surf = pygame.Surface((width, height))
        self.surf.fill((0,191,255))
        grid_width = 30
        grid_height = 30
        for i in range(20,width-20,grid_width):
        	for j in range(20,height-20,grid_height):
        		rect = pygame.Rect((i,j), (grid_width,grid_height))
        		pygame.draw.rect(self.surf, (0,0,0), rect,1)

def binarySearch(arr, l, r, x): 
  
    while l <= r: 
  
        mid = l + (r - l)//2; 
          
        if arr[mid] == x: 
            return True 
  
        elif arr[mid] < x: 
            l = mid + 1
  
        else: 
            r = mid - 1
      
    return False

def calulate_rect(cord,origin):
	column = ((cord[0]-origin[0])//30)
	row = ((cord[1]-origin[1])//30)
	return [row,column]

def text_to_screen(screen, text, x, y,clrscr = (0,0), size = 20,color = (200, 000, 000), font_type = 'battleship/Arial.ttf',):
	rect = pygame.Rect((x,y), clrscr)
	pygame.draw.rect(screen, (255,255,224), rect)
	font = pygame.font.Font(font_type, size)
	text = font.render(text, True, color)
	screen.blit(text, (x, y))
def check_disjoint(list1,list2):
	for i in list1:
		if binarySearch(list2,0,len(list2)-1,i) == True:
		 # element present
		 return False # even one cord is present 
	return True # if disjoint



def in_grid(row,column,align,size):
	if align == 'h':
		if ((column+size+1) <= 10):
			return True
	else:
		if ((row+size+1) <= 10) :
			return True
	return False
	

def AI_boats_loc():
	boats_loc = []
	size = 5
	while size != 0:
		temp_list = []
		align = random.choice(('h','v'))
		row = random.choice(range(10))
		column = random.choice(range(10))
		if ([row,column] in boats_loc) or (in_grid(row,column,align,size) == False):
			continue
		else:
			if align == 'h':
				for i in range(size):
					temp_list.append([row,column+i])
				if check_disjoint(temp_list,boats_loc) == False:
					continue
				else:
					boats_loc.extend(temp_list)
					size-=1
			else:
				for i in range(size):
					temp_list.append([row+i,column])
				if check_disjoint(temp_list,boats_loc) == False:
					continue
				else:
					boats_loc.extend(temp_list)
					size-=1
	ai.boats = boats_loc		
	

def check_if_elements_unique(my_list):
	for i in my_list:
		if my_list.count(i) > 1:
			return False
	return True

def game():
	no_of_player_hits = 0
	no_of_ai_hits = 0
	print("ai boats",ai.boats)
	running = True
	
	
	
	screen = pygame.display.set_mode((screen_width, screen_height))
	screen.fill((255,255,224))
	#pygame.draw.line(screen, (0, 0, 0), (screen_width//2, 0), (screen_width//2, screen_height),3)
	text_to_screen(screen,"HIT is denoted in red colour",40,0)
	text_to_screen(screen,"HINT: ATTACKING A ALREDY ATTACKED PLACE IS A WASTE",40,60)
	text_to_screen(screen,"YOUR BOARD",150,120)
	text_to_screen(screen,"ENEMY BOARD",360,120)
	while running:	
		screen.blit(player.surf,(0,screen_height//4) )
		screen.blit(ai.surf,(screen_width//2,screen_height//4) )
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONUP:

				cord = event.pos
				print(cord)

				if cord[0]>=360 and cord[0]<=660 and cord[1]>=190 and cord[1] <= 490:
					row = random.choice(range(10))
					column = random.choice(range(10))
					ai_rectangle = [row,column]
					print("ai going to attack on",ai_rectangle)
					ai_xco = (ai_rectangle[0]*30) + 190
					ai_yco = (ai_rectangle[1]*30) + 20
					ai_rect = pygame.Rect((ai_yco,ai_xco-20-150), (30,30))
					rectangle = calulate_rect(cord,(360,190))
					xco = (rectangle[0]*30) + 190
					yco = (rectangle[1]*30) + 20
					playerrect = pygame.Rect((yco,xco-20-150), (30,30))
					if rectangle in ai.boats:						
						pygame.draw.rect(ai.surf,(255,0,0), playerrect)
						no_of_player_hits+=1
						print("HIT!!")

					else:
						pygame.draw.rect(ai.surf,(255,255,224), playerrect)
						print("MISSED")
					if ai_rectangle in player.boats:
						
						pygame.draw.rect(player.surf,(255,0,0), ai_rect)
						no_of_ai_hits+=1
						print("AI:HIT!!")

					else:
						pygame.draw.rect(player.surf,(255,255,224), ai_rect)
						print("AI:MISSED")
		if no_of_player_hits == 15:
			Final_scene("You Won!!. Press any key to quit")
			running = False
		if no_of_ai_hits == 15:
			Final_scene("You Lost!!. Press any key to quit")
			running = False
		

		
				
def Final_scene(message):
	screen = pygame.display.set_mode((screen_width, screen_height))
	screen.fill((255,255,224))
	
	text_to_screen(screen,message,0,340,(0,0),30)
	pygame.display.flip()
	running = True
	while running:
		
		for event in pygame.event.get():
			if event.type == QUIT:
				running = False
			if event.type == KEYDOWN:
				running = False


def intialize():
	global flag
	boats_loc = []
	boats = ["aircraft carrier","battleship","submarine","destroyer","patrol boat"]
	colours = ( (118, 0, 163),( 38, 243, 13 ),( 243, 13, 222 ),(144, 118, 12),(  196, 236, 0  ))
	running = True
	t = 0
	count = 0
	screen = pygame.display.set_mode((screen_width, screen_height))
	screen.fill((255,255,224))
	screen.blit(player.surf,(0,screen_height//4) )
	pygame.display.flip()
	
	while running:	
		if t>=5:
			break
		size = 5-t
		colour = colours[t]

		message = "place "+boats[t]+" on the board by clicking "+str(size)+" STRAIGHT squares"
		text_to_screen(screen,message,0,0,(680,50),20,colour)
		
		pygame.display.flip()
		for event in pygame.event.get():
			if count>=size:
				t+=1
				count = 0
				break
			if event.type == QUIT:
				flag = 0
				running = False
				
			if event.type == pygame.MOUSEBUTTONUP  and count<=size:
				rect = pygame.Rect((0,50), (680,50))
				pygame.draw.rect(screen, (255,255,224), rect)
				cord = event.pos
				print(cord)
				
				if cord[0]<=320 and cord[0]>=20 and cord[1]>=190 and cord[1]<=490:
					rectangle = calulate_rect(cord,(20,190))
					if rectangle not in boats_loc:
						count+=1
						print(rectangle)
						boats_loc.append(rectangle)
						xco = (rectangle[0]*30) + 190
						yco = (rectangle[1]*30) + 20
						rect = pygame.Rect((yco,xco), (30,30))
						playerrect = pygame.Rect((yco,xco-20-150), (30,30))
						pygame.draw.rect(player.surf,colour, playerrect)
						pygame.draw.rect(screen, colour, rect)
						pygame.display.flip()
					else:
						print("colliding")
						text_to_screen(screen,"boats should not be overlapping",0,50,(680,50),20,colour)
						pygame.display.flip()
	player.boats = boats_loc
	
	
flag = 1	
player = Player()
ai = AI()
AI_boats_loc()
while check_if_elements_unique(ai.boats) == False:  # While running tests to check if ai.boats were distinct only once postions were repeteded and I could not figure out the fault in the algo so temporarily this part will take care if it happpens again. But most probably this loop wont run
 	print("changing ai boats")
 	AI_boats_loc()

print(ai.boats)
intialize()
if flag == 1:
	game()




			
	      

        

            

    





