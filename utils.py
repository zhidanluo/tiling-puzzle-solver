import numpy as np
import copy

# Connected Components Algorithm
import cv2


"""Loading puzzle setting."""
def loadPuzzle(path, puzzleName):
    printName = copy.copy(puzzleName)
    puzzleDataSetsDirectoryFullPath = path
    puzzleName = puzzleDataSetsDirectoryFullPath + puzzleName
    with open(puzzleName, 'r') as f:
        puzzleRaw = f.read()
    
    puzzleUnique = list(set(puzzleRaw))
    puzzleUnique = [i for i in puzzleUnique if i != ' ']
    puzzleUnique = [i for i in puzzleUnique if i != '\n']

    count = 0    
    for puzzleElement in puzzleUnique:
        count += 1
        countStr = str(count)
        puzzle = puzzleRaw.replace(puzzleElement,countStr)
    puzzle = puzzle.replace(' ', '0')
    
    
    lines = puzzle.splitlines()
    maxNum = 0
    for line in lines:
        num = len(line)
        if num >maxNum:
            maxNum = num
    
    puzzleArray = np.zeros(maxNum)
    for line in lines:
        if line == '':
            lineArray = np.zeros(maxNum)           
        else:
            lineList = []
            for i in range(len(line)):
                lineList.append(int(line[i]))       
            
            lineArray = np.array(lineList)
            zeros = np.zeros(maxNum - len(lineList))
            lineArray = np.append(lineArray, zeros)
            
        puzzleArray = np.vstack((puzzleArray, lineArray))
    puzzleArray = puzzleArray.astype(int)
    print("successfully loaded puzzle setting: '%s'" % printName)
        
    return puzzleArray
    
  
def findConnectedComponents(data):
    data = np.array(data, dtype=np.uint8)    
    img = cv2.threshold(data, 0, 255, cv2.THRESH_BINARY)[1]
    nComponents, labels = cv2.connectedComponents(img, connectivity=4)   

    return nComponents, labels


def createTile(index):
    row = index[0]
    col = index[1]
    row -= min(row)
    col -= min(col)
    
    tile = np.zeros((max(row)+1, max(col)+1)).astype(int)
    for i in range(len(row)):
        tile[row[i], col[i]] =1
    
    return tile
    

def loadTileBoard(path, puzzleName):
    puzzleArray = loadPuzzle(path, puzzleName)
    
    nComponents, labels = findConnectedComponents(puzzleArray)
    
    tiles = []
    tilesLength = []
    for i in range(nComponents-1):        
        index = np.where(labels==i+1)
        tile = createTile(index)
        tiles.append(tile)
        tilesLength.append(np.sum(tile))
    
    boardIndex = tilesLength.index(max(tilesLength))
    board = tiles[boardIndex]
    board += -1
    board = np.abs(board)
    tiles.pop(boardIndex)
    
    if not puzzleName.find('test') == -1:
        tilesLength.pop(boardIndex)
        boardIndex = tilesLength.index(max(tilesLength))
        board = tiles[boardIndex]
        tiles.pop(boardIndex)
        
    return tiles, board