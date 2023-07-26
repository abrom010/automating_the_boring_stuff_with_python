def isValidChessBoard(board):
	whiteKing = False
	blackKing = False

	whitePieceCount = 16
	blackPieceCount = 16

	whitePawnCount = 8
	blackPawnCount = 8

	for k, v in board.items():
		if not checkKey(k) and checkValue(v):
			return False
		if v[0] == w:
			whitePieceCount -= 1
			if 'pawn' in v:
				whitePawnCount -= 1
			if 'king' in v:
				if whiteKing:
					return False
				else:
					whiteKing = False
		if v[0] == b:
			blackPieceCount -= 1
			if 'pawn' in v:
				blackPawnCount -= 1
			if 'king' in v:
				if blackKing:
					return False
				else:
					blackKing = False
		if whitePieceCount < 0 or blackPieceCount < 0 or whitePawnCount < 0 or blackPawnCount < 0:
			return False
	return True

def checkKey(k):
	validLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
	validNumbers = ['1', '2', '3', '4', '5', '6', '7', '8']
	if len(k) > 2:
		return False
	if k[0] not in validNumbers or k[1] not in validLetters:
		return False
	return True

def checkValue(v):
	validPieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'pawn']
	if v[0] != 'w' or v[0] != 'b':
		return False
	if v[1:] not in validPieces:
		return False
	return True