#Easy - 0 0 4 0 5 0 0 0 0 9 0 0 7 3 4 6 0 0 0 0 3 0 2 1 0 4 9 0 3 5 0 9 0 4 8 0 0 9 0 0 0 0 0 3 0 0 7 6 0 1 0 9 2 0 3 1 0 9 7 0 2 0 0 0 0 9 1 8 2 0 0 3 0 0 0 0 6 0 1 0 0
#Medium - 2 0 0 0 0 0 6 9 0 0 5 0 0 0 3 0 0 0 1 7 0 0 0 9 4 0 5 0 0 3 0 2 5 0 1 8 0 0 0 0 4 0 0 0 0 7 2 0 3 8 0 5 0 0 5 0 2 6 0 0 0 4 1 0 0 0 5 0 0 0 7 0 0 6 7 0 0 0 0 0 3
#Hard - 0 0 0 8 0 0 4 2 0 5 0 0 6 7 0 0 0 0 0 0 0 0 0 9 0 0 5 7 4 0 1 0 0 0 0 0 0 0 9 0 3 0 7 0 0 0 0 0 0 0 7 0 4 8 8 0 0 4 0 0 0 0 0 0 0 0 0 9 8 0 0 3 0 9 5 0 0 3 0 0 0

import copy
def coordinate(row,column):  # Function used to create keys for possibilites dictionary
    return str(row)+","+str(column)

def checkRowSolved(puzzleIn):  #  Checking rows of for solved puzzles
    for a in range(9):
      puzzleIn[a].sort()
      if [1,2,3,4,5,6,7,8,9]!=puzzleIn[a]:  # Compares the row (sorted) to a complete sorted list. Every row of the puzzle must have numbers 1-9 in the row only once
        return False      
    return True

def checkRow(possibilitiesIn,puzzleIn,rowIn,columnIn):  #  Checking row of provided empty space
    for a in range(9):  # Going through all columns of row being checked
        if puzzleIn[rowIn][a]!=0:  # If current number is not 0
            for i in range(len(possibilitiesIn[coordinate(rowIn,columnIn)])):  # Go through all number of dictionary possiblities list
                if puzzleIn[rowIn][a]==possibilitiesIn[coordinate(rowIn,columnIn)][i]:  # If the current number is in the possibilites list
                    possibilitiesIn[coordinate(rowIn,columnIn)].pop(i)  # Take current number out of the possibilites list for specific empty space
                    break
    return possibilitiesIn

def checkColumnSolved(puzzleIn):  #  Checking columns for solved puzzles
    for b in range(9):
      checking=[1,2,3,4,5,6,7,8,9]  # This list is used for comparisons to each section of the solved puzzle. Every puzzle must have numbers 1=9 in the column only once
      for a in range(9):
        for i in range(len(checking)):
          if checking[i]==puzzleIn[a][b]:
            checking.pop(i)
            break 
      if len(checking)!=0:
        return False      
    return True
    
def checkColumn(possibilitiesIn,puzzleIn,rowIn,columnIn):
    for a in range(9):  # Going through all columns of row being checked
        if puzzleIn[a][columnIn]!=0:  # If current number is not 0
            for i in range(len(possibilitiesIn[coordinate(rowIn,columnIn)])):  # Go through all number of dictionary possiblities list
                if puzzleIn[a][columnIn]==possibilitiesIn[coordinate(rowIn,columnIn)][i]:  # If the current number is in the possibilites list
                    possibilitiesIn[coordinate(rowIn,columnIn)].pop(i)  # Take current number out of the possibilites list for specific empty space
                    break
    return possibilitiesIn     

def checkSolvedSection(puzzleIn):  # Checking sections for solved puzzles
  for counter in range(9):
    checking=[1,2,3,4,5,6,7,8,9]  # This list is used for comparisons to each section of the solved puzzle. Each section of the puzzle must only have numbers 1-9 only once in each section
    if counter==0:  
      for a in range(3):
        for b in range(3):
          for i in range(len(checking)):
            if puzzleIn[a][b]==checking[i]:
              checking.pop(i)
              break
    if counter==1:
      for a in range(3):
        for b in range(3):
          for i in range(len(checking)):
            if puzzleIn[a][b+3]==checking[i]:
              checking.pop(i)
              break
    if counter==2:
      for a in range(3):
        for b in range(3):
          for i in range(len(checking)):
            if puzzleIn[a][b+6]==checking[i]:
              checking.pop(i)
              break
    if counter==3:
      for a in range(3):
        for b in range(3):
          for i in range(len(checking)):
            if puzzleIn[a+3][b]==checking[i]:
              checking.pop(i)
              break
    if counter==4:
      for a in range(3):
        for b in range(3):
          for i in range(len(checking)):
            if puzzleIn[a+3][b+3]==checking[i]:
              checking.pop(i)
              break
    if counter==5:
      for a in range(3):
        for b in range(3):
          for i in range(len(checking)):
            if puzzleIn[a+3][b+6]==checking[i]:
              checking.pop(i)
              break
    if counter==6:
      for a in range(3):
        for b in range(3):
          for i in range(len(checking)):
            if puzzleIn[a+6][b]==checking[i]:
              checking.pop(i)
              break
    if counter==7:
      for a in range(3):
        for b in range(3):
          for i in range(len(checking)):
            if puzzleIn[a+6][b+3]==checking[i]:
              checking.pop(i)
              break
    if counter==8:
      for a in range(3):
        for b in range(3):
          for i in range(len(checking)):
            if puzzleIn[a+6][b+6]==checking[i]:
              checking.pop(i)
              break
    if len(checking)!=0:
      return False
  return True    

def checkSection(possibilitiesIn,puzzleIn,rowIn,columnIn):  # Checks section of empty space provided
    if rowIn<3 and columnIn<3:  # Switch/case-similar method for finding which section the empty space is located in
      for a in range(3):
        for b in range(3):
          if puzzleIn[a][b]!=0:
            for i in range(len(possibilitiesIn[coordinate(rowIn,columnIn)])):
              if puzzleIn[a][b]==possibilitiesIn[coordinate(rowIn,columnIn)][i]:
                possibilitiesIn[coordinate(rowIn,columnIn)].pop(i)
                break
    elif rowIn<3 and (columnIn>=3 and columnIn<=5):
      for a in range(3):
        for b in range(3):
          if puzzleIn[a][b+3]!=0:
            for i in range(len(possibilitiesIn[coordinate(rowIn,columnIn)])):
              if puzzleIn[a][b+3]==possibilitiesIn[coordinate(rowIn,columnIn)][i]:
                possibilitiesIn[coordinate(rowIn,columnIn)].pop(i)
                break
    elif rowIn<3 and (columnIn>=6 and columnIn<=8):
      for a in range(3):
        for b in range(3):
          if puzzleIn[a][b+6]!=0:
            for i in range(len(possibilitiesIn[coordinate(rowIn,columnIn)])):
              if puzzleIn[a][b+6]==possibilitiesIn[coordinate(rowIn,columnIn)][i]:
                possibilitiesIn[coordinate(rowIn,columnIn)].pop(i)
                break
    elif (rowIn>=3 and rowIn<=5) and columnIn<3:
      for a in range(3):
        for b in range(3):
          if puzzleIn[a+3][b]!=0:
            for i in range(len(possibilitiesIn[coordinate(rowIn,columnIn)])):
              if puzzleIn[a+3][b]==possibilitiesIn[coordinate(rowIn,columnIn)][i]:
                possibilitiesIn[coordinate(rowIn,columnIn)].pop(i)
                break
    elif (rowIn>=3 and rowIn<=5) and (columnIn>=3 and columnIn<=5):
      for a in range(3):
        for b in range(3):
          if puzzleIn[a+3][b+3]!=0:
            for i in range(len(possibilitiesIn[coordinate(rowIn,columnIn)])):
              if puzzleIn[a+3][b+3]==possibilitiesIn[coordinate(rowIn,columnIn)][i]:
                possibilitiesIn[coordinate(rowIn,columnIn)].pop(i)
                break
    elif (rowIn>=3 and rowIn<=5) and (columnIn>=6 and columnIn<=8):
      for a in range(3):
        for b in range(3):
          if puzzleIn[a+3][b+6]!=0:
            for i in range(len(possibilitiesIn[coordinate(rowIn,columnIn)])):
              if puzzleIn[a+3][b+6]==possibilitiesIn[coordinate(rowIn,columnIn)][i]:
                possibilitiesIn[coordinate(rowIn,columnIn)].pop(i)
                break
    elif (rowIn>=6 and rowIn<=8) and columnIn<3:
      for a in range(3):
        for b in range(3):
          if puzzleIn[a+6][b]!=0:
            for i in range(len(possibilitiesIn[coordinate(rowIn,columnIn)])):
              if puzzleIn[a+6][b]==possibilitiesIn[coordinate(rowIn,columnIn)][i]:
                possibilitiesIn[coordinate(rowIn,columnIn)].pop(i)
                break
    elif (rowIn>=6 and rowIn<=8) and (columnIn>=3 and columnIn<=5):
      for a in range(3):
        for b in range(3):
          if puzzleIn[a+6][b+3]!=0:
            for i in range(len(possibilitiesIn[coordinate(rowIn,columnIn)])):
              if puzzleIn[a+6][b+3]==possibilitiesIn[coordinate(rowIn,columnIn)][i]:
                possibilitiesIn[coordinate(rowIn,columnIn)].pop(i)
                break
    elif (rowIn>=6 and rowIn<=8) and (columnIn>=6 and columnIn<=8):
      for a in range(3):
        for b in range(3):
          if puzzleIn[a+6][b+6]!=0:
            for i in range(len(possibilitiesIn[coordinate(rowIn,columnIn)])):
              if puzzleIn[a+6][b+6]==possibilitiesIn[coordinate(rowIn,columnIn)][i]:
                possibilitiesIn[coordinate(rowIn,columnIn)].pop(i)
                break
    return possibilitiesIn          
          
def runChecks(possibilitiesIn, puzzleIn):  # Function to allow multiple calls of checking empty spaces
  for a in range(9):
    for b in range(9):
      if puzzleIn[a][b]==0:  # Going through puzzle to find empty spaces and running check functions for each
          possibilitiesIn=checkRow(possibilitiesIn,puzzleIn,a,b)
          possibilitiesIn=checkColumn(possibilitiesIn,puzzleIn,a,b)
          possibilitiesIn=checkSection(possibilitiesIn,puzzleIn,a,b)
  return possibilitiesIn

def insert(possibilitesIn,puzzleIn):  # Function to allow multiple calls to insert one-long possibilites from dictionary of possibilities
  for key in possibilitesIn:
    if len(possibilitesIn[key])==1:
      coordinate=key.split(",")
      puzzleIn[int(coordinate[0])][int(coordinate[1])]=possibilitesIn[key][0]
      possibilitesIn[key].pop(0)
  return possibilitesIn,puzzleIn

def checkSolved(puzzleIn):  # Method used for checking if the puzzle is completely solved
  for a in range(9):
    for b in range(9):
      if puzzleIn[a][b]==0:
        return False
  return True

def guessOne(possibilitiesIn,puzzleIn,coordinate):  # Guessing second possibility from list of two possibilities
  possibilitiesIn[coordinate].pop(0)  # Taking out first possibility
  for i in range(30):  # For-loop used to solve puzzle
    possibilitiesIn,puzzleIn=insert(possibilitiesIn,puzzleIn)
    possibilitiesIn=runChecks(possibilitiesIn,puzzleIn)
  return possibilitiesIn,puzzleIn

def guessTwo(possibilitiesIn,puzzleIn,coordinate):  # Guessing first possibility from list of two possibilities
  possibilitiesIn[coordinate].pop(1)  # Taking out second possibility
  for i in range(30):  # For-loop used to solve puzzle
    possibilitiesIn,puzzleIn=insert(possibilitiesIn,puzzleIn)
    possibilitiesIn=runChecks(possibilitiesIn,puzzleIn)
  return possibilitiesIn,puzzleIn

def guessThree(possibilitiesIn,puzzleIn,coordinate):  # Guessing second possibility from list of three possibilities
  possibilitiesIn[coordinate].pop(0)  # Taking out first possibility
  possibilitiesIn[coordinate].pop(1)  # Taking out last possiblity (last one is moved after previous line of code executes)
  for i in range(30):  # For-loop used to solve puzzle
    possibilitiesIn,puzzleIn=insert(possibilitiesIn,puzzleIn)
    possibilitiesIn=runChecks(possibilitiesIn,puzzleIn)
  return possibilitiesIn,puzzleIn

def guessFour(possibilitiesIn,puzzleIn,coordinate):  # Guessing first possibility from list of three possibilities
  possibilitiesIn[coordinate].pop(1)  # Taking out second possibility
  possibilitiesIn[coordinate].pop(1)  # Taking out third possibility (last one is moved after previous line of code executes)
  for i in range(30):  # For-loop used to solve puzzle
    possibilitiesIn,puzzleIn=insert(possibilitiesIn,puzzleIn)
    possibilitiesIn=runChecks(possibilitiesIn,puzzleIn)
  return possibilitiesIn,puzzleIn

def guessFive(possibilitiesIn,puzzleIn,coordinate):  # Guessing third possibility from list of three possibilities
  possibilitiesIn[coordinate].pop(0)  # Taking out first possibility
  possibilitiesIn[coordinate].pop(0)  # Taking out second possibility (second possibility is moved after previous line of code executes)
  for i in range(30):  # For-loop used to solve puzzle
    possibilitiesIn,puzzleIn=insert(possibilitiesIn,puzzleIn)
    possibilitiesIn=runChecks(possibilitiesIn,puzzleIn)
  return possibilitiesIn,puzzleIn
    
def hardPuzzles(possibilitiesIn,puzzleIn):  # Hard puzzle code for solving hard puzzles. Uses methods of guessing possibilities from dictionary of possibles
  for key in possibilitiesIn:  # Method for guessing first possibilities from lists of 2 possibilites from original possibilities dictionary
    if len(possibilitiesIn[key])==2:
      possTest=copy.deepcopy(possibilitiesIn)
      puzzTest=copy.deepcopy(puzzleIn)
      possTest,puzzTest=guessOne(possTest,puzzTest,key)
      if checkSolved(copy.deepcopy(puzzTest)) and checkSolvedSection(copy.deepcopy(puzzTest)) and checkColumnSolved(copy.deepcopy(puzzTest)) and checkRowSolved(copy.deepcopy(puzzTest)):  # If solved completely
        return puzzTest
      else: 
        for key in possTest:  # Method for guessing first possibilities from lists of 2 possibilities from next over (newly created) possibilities dictionary, created from previously guessed possibilities
          if len(possTest[key])==2:
            possTest2=copy.deepcopy(possTest)
            puzzTest2=copy.deepcopy(puzzTest)
            possTest2,puzzTest2=guessOne(possTest2,puzzTest2,key)
            if checkSolved(copy.deepcopy(puzzTest2)) and checkSolvedSection(copy.deepcopy(puzzTest2)) and checkColumnSolved(copy.deepcopy(puzzTest2)) and checkRowSolved(copy.deepcopy(puzzTest2)):  # If solved completely
              return puzzTest2
            else:
              for key in possTest2:  # Method for guessing first possibilities from lists of 2 possibilities from next NEXT over (newly created) possibilities dictionary, created from previously PREVIOUSLY guessed possibilities
                if len(possTest2[key])==2:
                  possTest3=copy.deepcopy(possTest2)
                  puzzTest3=copy.deepcopy(puzzTest2)
                  possTest3,puzzTest3=guessOne(possTest3,puzzTest3,key)
                  if checkSolved(copy.deepcopy(puzzTest3)) and checkSolvedSection(copy.deepcopy(puzzTest3)) and checkColumnSolved(copy.deepcopy(puzzTest3)) and checkRowSolved(copy.deepcopy(puzzTest3)):  # If solved completely
                    return puzzTest3
              
  for key in possibilitiesIn:  # Method for guessing second possibilities from lists of 2 possibilities from original possibilities dictionary
    if len(possibilitiesIn[key])==2:
      possTest=copy.deepcopy(possibilitiesIn)
      puzzTest=copy.deepcopy(puzzleIn)
      possTest,puzzTest=guessTwo(possTest,puzzTest,key)
      if checkSolved(copy.deepcopy(puzzTest)) and checkSolvedSection(copy.deepcopy(puzzTest)) and checkColumnSolved(copy.deepcopy(puzzTest)) and checkRowSolved(copy.deepcopy(puzzTest)):  # If solved completely
        return puzzTest
      else:
        for key in possTest:  # Method for guessing first possibilities from lists of 2 possibilities from next over (newly created) possibilities dictionary, created from previously guessed possibilities
          if len(possTest[key])==2:
            possTest2=copy.deepcopy(possTest)
            puzzTest2=copy.deepcopy(puzzTest)
            possTest2,puzzTest2=guessTwo(possTest2,puzzTest2,key)
            if checkSolved(copy.deepcopy(puzzTest2)) and checkSolvedSection(copy.deepcopy(puzzTest2)) and checkColumnSolved(copy.deepcopy(puzzTest2)) and checkRowSolved(copy.deepcopy(puzzTest2)):  # If solved completely
              return puzzTest2
            else:
              for key in possTest2:  # Method for guessing first possibilities from lists of 2 possibilities from next NEXT over (newly created) possibilities dictionary, created from previously PREVIOUSLY guessed possibilities
                if len(possTest2[key])==2:
                  possTest3=copy.deepcopy(possTest2)
                  puzzTest3=copy.deepcopy(puzzTest2)
                  possTest3,puzzTest3=guessTwo(possTest3,puzzTest3,key)
                  if checkSolved(copy.deepcopy(puzzTest3)) and checkSolvedSection(copy.deepcopy(puzzTest3)) and checkColumnSolved(copy.deepcopy(puzzTest3)) and checkRowSolved(copy.deepcopy(puzzTest3)):  # If solved completely
                    return puzzTest3           
                  

  for key in possibilitiesIn:  # Method for guessing second possibilities from lists of 3 possibilities from original possibilities dictionary
    if len(possibilitiesIn[key])==3:
      possTest=copy.deepcopy(possibilitiesIn)
      puzzTest=copy.deepcopy(puzzleIn)
      possTest,puzzTest=guessThree(possTest,puzzTest,key)
      if checkSolved(copy.deepcopy(puzzTest)) and checkSolvedSection(copy.deepcopy(puzzTest)) and checkColumnSolved(copy.deepcopy(puzzTest)) and checkRowSolved(copy.deepcopy(puzzTest)):  # If solved completely
        return puzzTest
      else:
        for key in possTest:
          if len(possTest[key])==3:  # Method for guessing second possibilities from lists of 3 possibilities from next over (newly created) possibilities dictionary, created from previously guessed possibilities
            possTest2=copy.deepcopy(possTest)
            puzzTest2=copy.deepcopy(puzzTest)
            possTest2,puzzTest2=guessThree(possTest2,puzzTest2,key)
            if checkSolved(copy.deepcopy(puzzTest2)) and checkSolvedSection(copy.deepcopy(puzzTest2)) and checkColumnSolved(copy.deepcopy(puzzTest2)) and checkRowSolved(copy.deepcopy(puzzTest2)):  # If solved completely
              return puzzTest2
            else:
              for key in possTest2:  # Method for guessing second possibilities from lists of 3 possibilities from next NEXT over (newly created) possibilities dictionary, created from previously PREVIOUSLY guessed possibilities
                if len(possTest2[key])==3:
                  possTest3=copy.deepcopy(possTest2)
                  puzzTest3=copy.deepcopy(puzzTest2)
                  possTest3,puzzTest3=guessThree(possTest3,puzzTest3,key)
                  if checkSolved(copy.deepcopy(puzzTest3)) and checkSolvedSection(copy.deepcopy(puzzTest3)) and checkColumnSolved(copy.deepcopy(puzzTest3)) and checkRowSolved(copy.deepcopy(puzzTest3)):  # If solved completely
                    return puzzTest3         

  for key in possibilitiesIn:  # Method for guessing first possibilities from lists of 3 possibilities from original possibilities dictionary
    if len(possibilitiesIn[key])==3:
      possTest=copy.deepcopy(possibilitiesIn)
      puzzTest=copy.deepcopy(puzzleIn)
      possTest,puzzTest=guessFour(possTest,puzzTest,key)
      if checkSolved(copy.deepcopy(puzzTest)) and checkSolvedSection(copy.deepcopy(puzzTest)) and checkColumnSolved(copy.deepcopy(puzzTest)) and checkRowSolved(copy.deepcopy(puzzTest)):  # If solved completely
        return puzzTest
      else:
        for key in possTest:
          if len(possTest[key])==3:  # Method for guessing first possibilities from lists of 3 possibilities from next over (newly created) possibilities dictionary, created from previously guessed possibilities
            possTest2=copy.deepcopy(possTest)
            puzzTest2=copy.deepcopy(puzzTest)
            possTest2,puzzTest2=guessFour(possTest2,puzzTest2,key)
            if checkSolved(copy.deepcopy(puzzTest2)) and checkSolvedSection(copy.deepcopy(puzzTest2)) and checkColumnSolved(copy.deepcopy(puzzTest2)) and checkRowSolved(copy.deepcopy(puzzTest2)):  # If solved completely
              return puzzTest2
            else:
              for key in possTest2:
                if len(possTest2[key])==3:  # Method for guessing first possibilities from lists of 3 possibilities from next NEXT over (newly created) possibilities dictionary, created from previously PREVIOUSLY guessed possibilities
                  possTest3=copy.deepcopy(possTest2)
                  puzzTest3=copy.deepcopy(puzzTest2)
                  possTest3,puzzTest3=guessFour(possTest3,puzzTest3,key)
                  if checkSolved(copy.deepcopy(puzzTest3)) and checkSolvedSection(copy.deepcopy(puzzTest3)) and checkColumnSolved(copy.deepcopy(puzzTest3)) and checkRowSolved(copy.deepcopy(puzzTest3)):  # If solved completely
                    return puzzTest3        

  for key in possibilitiesIn:  # Method for guessing third possibilities from lists of 3 possibilities from original possibilities dictionary
    if len(possibilitiesIn[key])==3:
      possTest=copy.deepcopy(possibilitiesIn)
      puzzTest=copy.deepcopy(puzzleIn)
      possTest,puzzTest=guessFive(possTest,puzzTest,key)
      if checkSolved(copy.deepcopy(puzzTest)) and checkSolvedSection(copy.deepcopy(puzzTest)) and checkColumnSolved(copy.deepcopy(puzzTest)) and checkRowSolved(copy.deepcopy(puzzTest)):
        return puzzTest
      else:
        for key in possTest:
          if len(possTest[key])==3:  # Method for guessing third possibilities from lists of 3 possibilities from next over (newly created) possibilities dictionary, created from previously guessed possibilities
            possTest2=copy.deepcopy(possTest)
            puzzTest2=copy.deepcopy(puzzTest)
            possTest2,puzzTest2=guessFive(possTest2,puzzTest2,key)
            if checkSolved(copy.deepcopy(puzzTest2)) and checkSolvedSection(copy.deepcopy(puzzTest2)) and checkColumnSolved(copy.deepcopy(puzzTest2)) and checkRowSolved(copy.deepcopy(puzzTest2)):
              return puzzTest2
            else:
              for key in possTest2:  # Method for guessing third possibilities from lists of 3 possibilities from next NEXT over (newly created) possibilities dictionary, created from previously PREVIOUSLY guessed possibilities
                if len(possTest2[key])==3:
                  possTest3=copy.deepcopy(possTest2)
                  puzzTest3=copy.deepcopy(puzzTest2)
                  possTest3,puzzTest3=guessFive(possTest3,puzzTest3,key)
                  if checkSolved(copy.deepcopy(puzzTest3)) and checkSolvedSection(copy.deepcopy(puzzTest3)) and checkColumnSolved(copy.deepcopy(puzzTest3)) and checkRowSolved(copy.deepcopy(puzzTest3)):
                    return puzzTest3
  return puzzle  # Return original puzzle if could not be solved                    


puzzleInput = input("Enter Sudoku Puzzle from left to right for each row, from top to bottom, and put a space between each number. Use 0 for an empty space:\n")
puzzleInput=puzzleInput.split(" ")

if len(puzzleInput)<81:  # Check for invalid input of puzzle
    print("Error. Not enough spaces provided.")
    quit()
elif len(puzzleInput)>81:
    print("Error. Too many spaces.")
    quit()           

puzzle=[]
current=0
for a in range(9):  # Turning the puzzle input into a 9x9 2D array called puzzle
  currentList=[]
  for b in range(9):
    currentList.append(puzzleInput[current])
    current+=1
  puzzle.append(currentList)

# Converting all elements in puzzle from strings to ints
for a in range(9):
    for b in range(9):
        puzzle[a][b]=int(puzzle[a][b])

possibilities={}  # Dictionary to hold all empty coordinate and their possibilities
# Creating dictionary of possiblities for all 0/empty spaces
for a in range(9):
    for b in range(9):
        if puzzle[a][b]==0:
            possibles=[1,2,3,4,5,6,7,8,9]
            possibilities[coordinate(a,b)]=possibles

for i in range(30):  # For-loop used to solve puzzle
  possibilities=runChecks(possibilities,puzzle)
  possibilities,puzzle=insert(possibilities,puzzle)

if checkSolved(copy.deepcopy(puzzle)) and checkSolvedSection(copy.deepcopy(puzzle)) and checkColumnSolved(copy.deepcopy(puzzle)) and checkRowSolved(copy.deepcopy(puzzle)):  # If solved through orinary method of checking rows, columns, and sections
  print("Completely solved puzzle:")
  for i in range(9):  # Printing puzzle
    print(puzzle[i])
else:  # If not solved through basic/ordinary method
  puzzle=hardPuzzles(possibilities,puzzle)
  if checkSolved(copy.deepcopy(puzzle)) and checkSolvedSection(copy.deepcopy(puzzle)) and checkColumnSolved(copy.deepcopy(puzzle)) and checkRowSolved(copy.deepcopy(puzzle)): 
    print("Completely solved puzzle:")
    for i in range(9):  # Printing puzzle
      print(puzzle[i])
  else:  # Could not solve puzzle
    print("Could not solve.")    
