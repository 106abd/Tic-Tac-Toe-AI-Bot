import random


def clearTTTBoard():
    for tile in tttBoard:
        tttBoard[tile] = " "


def computeMiniMaxScore(treeDepth: int, isMaximizing: bool, turnNumber: int, alpha: int, beta: int) -> int:
    letterPiece = getLetterPiece(turnNumber)

    if treeDepth > 2 or (" " not in tttBoard and updateGameState(turnNumber - 1) == "Draw"):
        totalScore = 0
        for startTile in range(1, 8, 3):
            stringPattern = tttBoard[startTile] + tttBoard[startTile + 1] + tttBoard[startTile + 2]
            totalScore = totalScore + computePatternScore(stringPattern, letterPiece)

        for startTile in range(1, 4):
            stringPattern = tttBoard[startTile] + tttBoard[startTile + 3] + tttBoard[startTile + 6]
            totalScore = totalScore + computePatternScore(stringPattern, letterPiece)

        stringPattern = tttBoard[1] + tttBoard[5] + tttBoard[9]
        totalScore = totalScore + computePatternScore(stringPattern, letterPiece)

        stringPattern = tttBoard[3] + tttBoard[5] + tttBoard[7]
        totalScore = totalScore + computePatternScore(stringPattern, letterPiece)

        return totalScore

    elif isMaximizing:
        bestScore = -100000
        for tile in tttBoard:
            if tttBoard[tile] == " ":
                tttBoard[tile] = letterPiece
                mockBoardScore = computeMiniMaxScore(treeDepth + 1, False, turnNumber + treeDepth + 1, alpha, beta)
                tttBoard[tile] = " "

                bestScore = max(mockBoardScore, bestScore)

                alpha = max(alpha, mockBoardScore)
                if beta <= alpha:
                    break

        return bestScore

    elif not isMaximizing:
        worstScore = 100000

        for tile in tttBoard:
            if tttBoard[tile] == " ":
                tttBoard[tile] = letterPiece
                mockBoardScore = computeMiniMaxScore(treeDepth + 1, True, turnNumber + treeDepth + 1, alpha, beta)
                tttBoard[tile] = " "

                worstScore = min(mockBoardScore, worstScore)

                beta = min(beta, mockBoardScore)
                if beta <= alpha:
                    break

        return worstScore


def computePatternScore(pattern: str, letterPiece) -> int:
    patternScore = 0

    if letterPiece == "X":
        opponentLetterPiece = "O"
    else:
        opponentLetterPiece = "X"

    if (letterPiece + letterPiece + letterPiece) in pattern:
        patternScore = patternScore + 100

        return patternScore

    elif (letterPiece + letterPiece) in pattern:
        patternScore = patternScore + 9

        return patternScore

    elif (opponentLetterPiece + opponentLetterPiece + opponentLetterPiece) in pattern:
        patternScore = patternScore - 100

        return patternScore

    elif (opponentLetterPiece + opponentLetterPiece) in pattern:
        patternScore = patternScore - 9

        return patternScore

    else:
        for letter in pattern:
            if letter == letterPiece:
                patternScore = patternScore + 1
            elif letter == opponentLetterPiece:
                patternScore = patternScore - 1

        return patternScore


def createTTTBoard():
    global tttBoard
    tttBoard = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}


def decideFirstTurn() -> int:
    rngNumber = random.randint(1, 2)
    return rngNumber


def getComputerInput(turnNumber: int) -> int:
    letterPiece = getLetterPiece(turnNumber)
    bestMove = 0
    bestScore = -100000

    for tile in tttBoard:
        if tttBoard[tile] == " ":

            tttBoard[tile] = letterPiece
            mockBoardScore = computeMiniMaxScore(0, False, turnNumber, -100000, 100000)
            tttBoard[tile] = " "

            if mockBoardScore > bestScore:
                bestScore = mockBoardScore
                bestMove = tile

    return bestMove


def getLetterPiece(turnNumber: int) -> str:
    if (turnNumber % 2) == 1:
        letterPiece = "X"
    else:
        letterPiece = "O"

    return letterPiece


def getPlayerInput() -> int:
    playerInput = int(input("Tile number to place letter on: "))
    return playerInput


def updateGameState(turnNumber: int) -> str:
    gameState = "Unresolved"

    letterPiece = getLetterPiece(turnNumber)

    winConditions = [{1: letterPiece, 2: letterPiece, 3: letterPiece}, {4: letterPiece, 5: letterPiece, 6: letterPiece},
                     {7: letterPiece, 8: letterPiece, 9: letterPiece}, {1: letterPiece, 4: letterPiece, 7: letterPiece},
                     {2: letterPiece, 5: letterPiece, 8: letterPiece}, {3: letterPiece, 6: letterPiece, 9: letterPiece},
                     {1: letterPiece, 5: letterPiece, 9: letterPiece}, {3: letterPiece, 5: letterPiece, 7: letterPiece}]

    for condition in winConditions:
        for index, tile in enumerate(condition):
            if condition[tile] != tttBoard[tile]:
                break
            elif index == 2 and condition[tile] == list(condition.values())[-1]:
                gameState = "Victory"
                break

    if " " not in tttBoard.values() and gameState != "Victory":
        gameState = "Draw"

    return gameState


def placeLetter(piecePlacement: int, turnNumber: int) -> bool:
    letterPiece = getLetterPiece(turnNumber)

    if tttBoard[piecePlacement] != " ":
        print("Error")
        return False
    else:
        tttBoard[piecePlacement] = letterPiece
        return True


def printTTTBoard():
    print(" " + tttBoard[1], "| " + tttBoard[2] + " |", tttBoard[3])
    print("---|---|---")
    print(" " + tttBoard[4], "| " + tttBoard[5] + " |", tttBoard[6])
    print("---|---|---")
    print(" " + tttBoard[7], "| " + tttBoard[8] + " |", tttBoard[9])
    print()


def randomizeScore(difficultyMode: str) -> int:

    if difficultyMode == "Insane":
        return 0
    elif difficultyMode == "Hard":
        return 0
    elif difficultyMode == "Medium":
        return 0
    elif difficultyMode == "Easy":
        return 0
    elif difficultyMode == "Beginner":
        return 0


def startGame():
    firstTurn = decideFirstTurn()
    turnNumber = 1

    if firstTurn == 1:
        currentTurn = "Player"
    else:
        currentTurn = "Computer"

    createTTTBoard()
    printTTTBoard()

    while updateGameState(turnNumber) == "Unresolved":

        print("Turn", currentTurn)

        if currentTurn == "Player":
            selectedTile = getPlayerInput()
        else:
            selectedTile = getComputerInput(turnNumber)

        placeLetter(selectedTile, turnNumber)

        printTTTBoard()
        turnResult = updateGameState(turnNumber)

        if turnResult == "Victory":
            print(currentTurn, "Wins!")
            break
        elif turnResult == "Draw":
            print("Draw!")
            break
        else:
            turnNumber = turnNumber + 1

            if currentTurn == "Player":
                currentTurn = "Computer"
            else:
                currentTurn = "Player"


startGame()
