
from replit import clear, db
from functions import affirm
import board
from getkey import getkey, keys
import random
from encounter import Pencounter

global localY
global localX
def clamp(n, smallest, largest): return max(smallest, min(n, largest)) 

brd = []
boardX = 20
boardY = 20				
localY = boardY/2
localX = boardX/2
targets = [[0,0]]
board.playerCharacter = "@"
board.boardCharacter = "+"
board.init['targetMarkers'] = False

def func(x, y, chara): 
	return

def update():
	clear()
	brd = []	
	targets = [[0,0]]
	board.drawBoard(brd, localX, localY, boardX, boardY, targets, func)
	board.boardPrint(brd)
print("Loading")
clear()
def Pokemon():
  global localX
  global localY
  while True:
    if db['EeveeHP'] > 0:
      update()
      print('')
      if db['Perfume'] > 0:
        print(f'Your Shiny Perfume will wear off in {db["Perfume"]} encounters..  ')
      print('')
      print("Use arrow keys or WASD to move ")
      print('')
      print("Click 'e' to go back to main page. ")
      key = getkey()
      if key == keys.LEFT or key == keys.A:
        localX -= 1
        localX = clamp(localX, 0, boardX - 1)
        z = random.randint(1, 5)
        if z == 4:
          pass
          print('')
          print('You found a Pokemon!')
          affirm()
          clear()
          Pencounter()
        
      elif key == keys.RIGHT or key == keys.D:
        localX += 1
        localX = clamp(localX, 0, boardX - 1)
        z = random.randint(1, 5)
        if z == 4:
          pass
          print('')
          print('You found a Pokemon!')
          affirm()
          clear()
          Pencounter()
      elif key == keys.UP or key == keys.W:
        localY -= 1
        localY = clamp(localY, 0, boardY - 1)
        z = random.randint(1, 5)
        if z == 4:
          pass
          print('')
          print('You found a Pokemon!')
          affirm()
          clear()
          Pencounter()
      elif key == keys.DOWN or key == keys.S:
        localY += 1
        localY = clamp(localY, 0, boardY - 1)
        z = random.randint(1, 5)
        if z == 4:
          pass
          print('')
          print('You found a Pokemon!')
          affirm()
          clear()
          Pencounter()
      elif key == keys.E:
        clear()
        return ''
    else:
      return ''