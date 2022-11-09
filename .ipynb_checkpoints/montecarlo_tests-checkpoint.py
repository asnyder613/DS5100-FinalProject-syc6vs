import unittest
from montecarlo import Die
from montecarlo import Game
from montecarlo import Analyzer
import pandas as pd
import numpy as np
import random
import itertools 


class MonteCarloTestSuite(unittest.TestCase):
    
    
    def test_1_createDie(self):
        #create die instance
        faces1 = ['a', 1, 'b', 2, 3]
        die1 = Die(faces1)

        #expected to be in Die instance
        self.assertTrue('a' in die1.myDie['Face'].to_list(), "FAILURE: the die face was not added correctly")
    
    def test_2_createDie2(self):
        #create die instance with non-unique values
        faces2 = ['a', 'a', 2, 3, 4]
        die2 = Die(faces2)
        
        #Die instance should only have 4 faces
        self.assertTrue(len(die2.myDie['Face'].to_list()) == 4, "FAILURE: the die face should only have 4 faces")
    
    def test_3_changeFace(self):
        #create die instance
        faces1 = ['a', 1, 'b', 2, 3]
        die1 = Die(faces1)
        
        #change face on die1
        die1.changeweight('a', 3.0)

        #expected to be in Die instance
        self.assertTrue(3.0 in die1.myDie['Weight'].to_list(), "FAILURE: the die weight was not changed")
    
    def test_4_changeFace(self):
        #create die instance
        faces1 = ['a', 1, 'b', 2, 3]
        die1 = Die(faces1)
        
        #change face on die1 with incorrect input
        die1.changeweight('c', 5.0)

        #expected to be in Die instance
        self.assertFalse('5.0' in die1.myDie['Weight'].to_list(), "FAILURE: the die weight should not have been changed")
            
    def test_5_changeFace(self):
        #create die instance
        faces1 = ['a', 1, 'b', 2, 3]
        die1 = Die(faces1)
        
        #change face on die1 with non-float input
        die1.changeweight(1, 5)
               
        #expected to be in Die instance
        self.assertTrue(5.0 in die1.myDie['Weight'].to_list(), "FAILURE: the die weight was not changed")
            

    def test_6_rollDie1(self):
        #create die instance
        faces1 = ['a', 1, 'b', 2, 3]
        die1 = Die(faces1)
        
        #test roll on die1
        die1.roll(5)
    
        #roll should return 5 values
        self.assertTrue(len(die1.result) == 5, "FAILURE: the roll should have 5 results")
 

    def test_7_reveal(self):
        #create die instance
        faces1 = ['a', 1, 'b', 2, 3]
        die1 = Die(faces1)
            
        die1.reveal()
            
        self.assertTrue(len(die1.myDie['Weight'])==5, "FAILURE: the die display is incorrect")
        
        
    def test_8_play(self):
        #create die instance
        faces1 = ['a', 1, 'b', 2, 3]
        die1 = Die(faces1)

        #create additional die instance
        faces3 = ['a', 1, 'b', 2, 3]
        die3 = Die(faces3)

        #initialize dielist to use with Game class testing
        dielist1 = []

        #append instances of die to list
        dielist1.append(die1)
        dielist1.append(die3)
       
        #create instance of game
        game1 = Game(dielist1)
        
        #test play method
        game1.play(8)
              
        self.assertTrue(len(game1.playResults.index)==8, "FAILURE: the die was not rolled the correct number of times")
 

    def test_9_results(self):
        #create die instance
        faces1 = ['a', 1, 'b', 2, 3]
        die1 = Die(faces1)

        #create additional die instance
        faces3 = ['a', 1, 'b', 2, 3]
        die3 = Die(faces3)

        #initialize dielist to use with Game class testing
        dielist1 = []

        #append instances of die to list
        dielist1.append(die1)
        dielist1.append(die3)
       
        #create instance of game
        game1 = Game(dielist1)
        
        #execute play method
        game1.play(8)
        
        #test showResult method with narrow
        game1.showResult('narrow')
        
        self.assertTrue(len(game1.narrowResult.index)==16, "FAILURE: the result did not return a narrow dataframe")
            
 
    def test_10_facecount(self):
        #create die instance
        faces1 = ['a', 1, 'b', 2, 3]
        die1 = Die(faces1)

        #create additional die instance
        faces3 = ['a', 1, 'b', 2, 3]
        die3 = Die(faces3)

        #initialize dielist to use with Game class testing
        dielist1 = []

        #append instances of die to list
        dielist1.append(die1)
        dielist1.append(die3)
       
        #create instance of game
        game1 = Game(dielist1)
        
        #execute play and getresult methods
        game1.play(8)
        game1.showResult()
                
        #create instance for Analyzer class
        analyze1 = Analyzer(game1)
        
        #test face counts per roll method
        analyze1.face_counts_per_roll()

        self.assertTrue(len(analyze1.facecounts.index)==8, "FAILURE: the dataframe is not returned correctly")
        

    def test_11_jackpot(self):
        #create die instance
        faces1 = ['a', 1, 'b', 2, 3]
        die1 = Die(faces1)

        #create additional die instance
        faces3 = ['a', 1, 'b', 2, 3]
        die3 = Die(faces3)

        #initialize dielist to use with Game class testing
        dielist1 = []

        #append instances of die to list
        dielist1.append(die1)
        dielist1.append(die3)
       
        #create instance of game
        game1 = Game(dielist1)
        
        #execute play and getresult methods
        game1.play(8)
        game1.showResult()
                
        #create instance for Analyzer class
        analyze1 = Analyzer(game1)
        
        #test jackpot method
        analyze1.jackpot()

        self.assertTrue(type(analyze1.jackpotcount)==int, "FAILURE: jackpot does not return a count")
        
        
    def test_12_analyzecombo(self):
        #create die instance
        faces1 = ['a', 1, 'b', 2, 3]
        die1 = Die(faces1)

        #create additional die instance
        faces3 = ['a', 1, 'b', 2, 3]
        die3 = Die(faces3)

        #initialize dielist to use with Game class testing
        dielist1 = []

        #append instances of die to list
        dielist1.append(die1)
        dielist1.append(die3)
       
        #create instance of game
        game1 = Game(dielist1)
                
        #execute play method
        game1.play(8)

        #create instance for Analyzer class
        analyze1 = Analyzer(game1)
        
        #run jackpot method
        analyze1.jackpot()
        
        #test jackpot method
        analyze1.combo()

        self.assertTrue(len(analyze1.comboResult.columns)==1, "FAILURE: count method does not return correct dataframe")
        
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)