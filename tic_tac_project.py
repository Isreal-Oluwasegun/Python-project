from random import randrange 

def display_board(board):
	print("+-------"*3,"+",sep="")
	for row in range(3):
		print("|       "*3,"|",sep="")
		for col in range(3):
			print("|   "+ str(board[row][col]) + "   ", end="")
		print("|")
		print("|       "*3,"|",sep="")
		print("+-------"*3,"+",sep="")


def enter_move(board):
	ok = False
	while not ok:
		move = input("Select a number to move in: ")
		ok = len(move) == 1 and move >= '1' and move <= '9'
		if not ok:
			print("bad move! Try again")
			continue
		move = int(move) - 1
		row = move // 3
		col = move % 3
		sign = board[row][col]
		ok = sign not in ['X','O']
		if not ok:
			print("Field already occupied")
			continue
		board[row][col] = 'O'

def make_list_of_free_fields(board):
	free = []
	for row in range(3):
		for col in range(3):
			if board[row][col] not in ['X','O']:
				free.append((row,col))
	return free

def victory_for(board, sgn):
	if sgn == "X":
		who = "Me"
	if sgn == "O":
		who = "You"
	cross1 = cross2 = True
	for rc in range(3):
		if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:
			return who
		if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:
			return who
		if board[rc][rc] != sgn:
			cross1 = False
		if board[2-rc][2-rc]:
			cross2 = False
	if cross1 or cross2:
		return who
	return None

def compu_move(board):
	free = make_list_of_free_fields(board)
	cnt = len(free)
	if cnt > 0:
		this = randrange(cnt)
		row, col = free[this]
		board[row][col] = 'X'


board = [[3*j+i+1 for i in range(3)] for j in range(3)]	
board[1][1]="X"
Human_turn = True
free = make_list_of_free_fields(board)
while len(free):
	display_board(board)
	if Human_turn:
		enter_move(board)
		victor = victory_for(board, 'O')
	else:
		compu_move(board)
		victor = victory_for(board, 'X')
	if victor != None:
		break
	Human_turn = not Human_turn
	free = make_list_of_free_fields(board)

display_board(board)
if victor == "You":
	print("You won!")
elif victor == "Me":
	print("I won!")
else:
	print("Tie!")
