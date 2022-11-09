import pandas as pd
import numpy as np
import random
import itertools 

class Die():
    """
    A class to set the characteristics of a Die to be used in a Monte Carlo simulation.
    ...

    Attributes
    ----------
    faces : str or int
        an array of faces
    weights : float
        the weight of a given side of the die

    Methods
    -------
    changeweight:
        changes the weight of a single side of the die
    roll:
        rolls the die one or more times
    reveal:
        shows the user the die's current set of faces and weights
    """

    def __init__(self, faces: list = []):
        self.faces = faces
        
        #convert list to numpy array
        x = np.array(self.faces)
    
        # test for unique values
        uniqueFaces = np.unique(x)

        #initialize array of faces into data frame that sets weight to 1.0 as default
        self.myDie = pd.DataFrame({'Face': uniqueFaces,
                               'Weight': 1.0})
        
    def changeweight(self, changeFace, newWeight):
        
        self.changeFace = changeFace
        self.newWeight = newWeight
        
        #check to see if the face passed is valid and in die array                     
        if not np.isin(self.changeFace, self.myDie):
            print("This is not a valid face value")

       # if face is valid, check if weight is a float (or can be converted to one)
        if isinstance(self.newWeight, str):
            print("This is not a valid face value.")
            
        else:            
            if isinstance(self.newWeight, int):
                self.newWeight = float(self.newWeight)
            
        #change weight in die array
        self.myDie.loc[self.myDie['Face'].eq(str(self.changeFace)), 'Weight'] = self.newWeight

    def roll(self, roll_num=1):
        self.roll_num = int(roll_num)
        
        #roll the die
        self.result = random.choices(self.myDie['Face'], weights=self.myDie['Weight'],k=self.roll_num)
            
        return self.result
    
    def reveal(self):
        return self.myDie

    
class Game():
    """
    A class to create a game that rolls one or more die of the same kind one or more times
    ...

    Attributes
    ----------
    dieList : list
        a list of already instantiated similar die objects

    frame : str
        "narrow" or "wide" to determine format of displayed dataframe

    Methods
    -------
    play:
        plays the game by rolling the die and then saves the results of the play

    showResult:
        shows the user the results of the most recent play
    """

    def __init__(self, dieList: list = []):
        self.dieList = dieList

    def play(self, rollDie = int):
        
        #parameter specifying how many times the die should be rolled
        self.rollDie = int(rollDie) + 1
        
        #define list A to capture the results of the iterations
        self.listA = []
        
        #loop through number of rolls
        for i in range(1, self.rollDie):
            
            #define list B to capture the results of the die rolls
            self.listB = []
            
            #loop through the dice
            for die in self.dieList:
                
                #roll the die
                self.result = die.roll()
                
                #append the results to B
                self.listB.append(self.result[0])
            
            #append B to A
            self.listA.append(self.listB)
            
        #convert B to a data frame
        self.playResults = pd.DataFrame(self.listA)
        
        #add index/columns names to dataframe of results
        self.playResults.index.name = 'roll_num'
        self.playResults.columns.name = 'die_num'
        
    
    def showResult(self, frame="wide"):
        self.frame = frame
        print(self.frame)
        
        if self.frame != "wide" and self.frame != "narrow":
            print("Please select 'narrow' or 'wide' as your choice of display")
        else:
            if self.frame == "wide":
                return self.playResults
            else:
                self.narrowResult = self.playResults
                self.narrowResult = self.narrowResult.melt(ignore_index=False)
                self.narrowResult = self.narrowResult.reset_index().set_index(['roll_num', 'die_num'])
                self.narrowResult.rename(columns={'value':'die_face'}, inplace=True)
                return self.narrowResult


class Analyzer():
    """
    A class to take the results of a single game and compute various descriptive statistical properties about it
    ...

    Attributes
    ----------
    face counts per roll    : int
        the number of times a given face appeared in each roll

    jacokpot : int
        the number of times a roll resulted in all faces being the same

    combo   :   dataframe
        the number of combination types of faces were rolled and their counts

    permutation :   dataframe
        the number of sequence types were rolled and their counts

    Methods
    -------
    face counts per roll:
        computes how many times a given face is rolled in each event

    jackpot:
        computes how many times the game resulted in all faces being identical

    combo:
        computes the distinct combinations of faces rolled, along with their counts
    """

    def __init__(self, game):
        self.game = game
        self.facetype = [type(i) for i in self.game.showResult('narrow')['die_face']]

    def face_counts_per_roll(self):
        #initialize self.facecounts from game instance & calculate unique values of each face on the die
        self.facecounts = self.game.showResult('wide').apply(lambda s: s.value_counts(), axis=1).fillna(0)

        return self.facecounts

    def jackpot(self):
        #find number of colums (faces rolled) in game
        self.jackpot = self.game.showResult('wide')
        self.list_of_rows = self.jackpot.to_numpy().tolist()
        
        #initialize jackpot count
        self.jackpotcount = 0
        
        #initialize list of jackpots to be appended to dataframe
        self.jackpotList = []
        
        #iterate through each roll and count jackpots
        for i in self.list_of_rows:
            self.row_set = set(i)
            
            if len(self.row_set) == 1:
                self.jackpotcount += 1
                self.jackpotList.append(1)
                
            else:
                self.jackpotList.append(0)
            
        #append list to dataframe as new column of jackpots
        self.jackpot['Jackpot'] = self.jackpotList
        
        return self.jackpotcount


    def combo(self):
        #list of unique combinations
        self.comboList = [list(i) for i in set(tuple(i) for i in self.list_of_rows)]
        
        #initialize combocountList
        self.combocountList = []
        
        #assign each list element to a tuple
        self.comboList2 = [tuple(i) for i in self.comboList]
        self.list_of_rows2 = [tuple(i) for i in self.list_of_rows]
            
        #create dictionary that has each element as a key and count of that element
        self.resultsX = {}
        for i in self.comboList2:
            self.resultsX[i] = self.list_of_rows2.count(i)

        #create dataframe from dictionary
        self.comboResult = pd.DataFrame.from_dict(self.resultsX, orient='index', columns=['number_of_instances'])
        self.comboResult.index.name = 'combination'
        
        return self.comboResult
        
