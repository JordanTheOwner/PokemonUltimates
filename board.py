boardCharacter = "-"
playerCharacter = "#"
markerCharacter = "!"
printSpace = " "
init = {'playerMarker': True, 'targetMarkers':True}

def unimportant(): return
def drawBoard(board, x, y, brdX, brdY, tgets, c):
	for i in range(0, brdY):
		for z in range(0, brdX):
			arr = []
			arr.append(printSpace)
			if i == y and z == x and init['playerMarker'] == True:
				arr.append(playerCharacter)
				c(z, i, "player")
			else:
				marker = 0
				for pair in tgets:
					if pair in tgets:
						if pair[0] == z and pair[1] == i and init['targetMarkers']:
							marker = marker + 1
							arr.append(markerCharacter)
							c(z, i, "marker")
				if marker == 0:
					arr.append(boardCharacter)
					c(z, i, "board")
			board.append(arr)
		board.append("\r\n")
				
def boardPrint(board):
	for row in board:
		for space in row:
			print(space, end="")

    

