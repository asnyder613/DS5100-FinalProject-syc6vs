# Final Project for DS5100

**Metadata**
Name: Abigail Snyder
UVA id: syc6vs
Project name: Monte Carlo Simulator

**Synopsis**
The first step is to import the module. From the root of this package, run pip install .
Then, following the instructions in the __init__.py file, run the following list of import statements to be prepared to use the module.

Run the following import lines to be ready to use the module:
    import pandas as pd
    import numpy as np
    import random
    import itertools
    
    #If you will be using the montecarlo_demo notebook, also load:
    import string
    
**The module consists of the following classes and methods:**
   
    **class Die:**
    A class to set the characteristics of a Die to be used in a Monte Carlo simulation.

    Methods
    -------
    changeweight:
        changes the weight of a single side of the die
    roll:
        rolls the die one or more times
    reveal:
        shows the user the die's current set of faces and weights
    
    **class Game:**
    A class to create a game that rolls one or more die of the same kind one or more times
    
    Methods
    -------
    play:
        plays the game by rolling the die and then saves the results of the play

    showResult:
        shows the user the results of the most recent play
    
    **class Analyzer:**
    A class to take the results of a single game and compute various descriptive statistical properties about it
    
    Methods
    -------
    face counts per roll:
        computes how many times a given face is rolled in each event

    jackpot:
        computes how many times the game resulted in all faces being identical

    combo:
        computes the distinct combinations of faces rolled, along with their counts
  
  
**How to use the module:**
To create a die game, start by creating an instance of the die. Assume you want a coin with sides 'H' and 'T'

   #create a coin
   diefaces = ['H', 'T']
   firstdie = mc.Die(diefaces)

Then, if you want to change the weight of the die faces, use the changeweights method. 
Here, we make the "T" face of the die weigh 2.0. The default weight is 1.0. 

   #change weight on unfair coin
   firstdie.changeweight('T', 2.0)

Once you have created your die, you can roll that single die by callign the roll method and passing an integer of how many times you would like to roll the die. 

  #roll the die 3 times
  firstdie.roll(3)
  
The Die class also offers a method to view the die object that you created using the reveal method. 

  #see your die
  firstdie.reveal()
  
To play a game, start by creating a list of die objects (that you've created using the Die class) to be "rolled".
Below, we create a game instance using two dientical die, and then roll the die 5 times by passing the desired number of rolls to the play method.

  #create a list of die instances to be used in first game
  game1die = [firstdie, firstdie]
  
  #create instance of game
  game1 = mc.Game(game1die)
  
  #play game with 5 "rolls"
  game1.play(5)

If you would like to see the results of your roll, call the showResult method. The return value will be a dataframe containing the faces rolled during the game.
You may pass either 'wide' or 'narrow' as an argument to determine the format of the returned dataframe.

  #get results of game in narrow table
  game1.showResult('narrow')
  
The Analyzer class gives three methods to analyze the results of your game. 
First, face_counts_per_roll allows you to see how many unique values resulted in each roll. 

  #start by initializing an instance of Analyzer
  analyze1 = mc.Analyzer(game1)
 
  #then call the facecounts method
  analyze1.face_counts_per_roll()
 
The Jackpot method calculates the number of jackpots (where all the faces in a given roll are identical) in your game. 

  #call jackpot method
  analyze1.jackpot()
  
Finally, the combo method returns a dataframe of each unique combination of die faces in the game, as well as a count of how often they occurred. 

  #call the combo method
  analyze1.combo()


**API descriptions**

class Die():

    A class to set the characteristics of a Die to be used in a Monte Carlo simulation.
    ...

    Attributes
    ----------
    faces : str or int
        an array of faces
    weights : float
        the weight of a given side of the die, default is 1.0

    Methods
    -------
    __init__:
        initializes the Die object
        parameters: faces (a list of die faces made up of int or str characters)
        return: none
    
    changeweight:
        changes the weight of a single side of the die
        parameters: face (the face to be changed, int or str), weight (the new weight, float)
        return: none
        
    roll:
        rolls the die one or more times
        parameters: roll_num (how many times to roll the die, int [default=1])
        return: a data frame of the results of each roll
        
    reveal:
        shows the user the die's current set of faces and weights
        parameters: none
        return: a data frame of the die object showing faces and corresponding weights
    


class Game():

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
    __init__:
        initializes the game
        parameters: dieList (a list of Die objects, list)
        return: none
        
    play:
        plays the game by rolling the die and then saves the results of the play
        parameters: rollDie (how many times to roll the die, int)
        return: none

    showResult:
        shows the user the results of the most recent play
        parameters: frame (which format to display the data, 'wide' or 'narrow' [defualt is 'wide'])
        return: a data frame in the format indicated with the results of the game


    
    class Analyzer():

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
    __init__:
        initializes the Analyzer object
        parameters: game object
        return: none
        
    face counts per roll:
        computes how many times a given face is rolled in each event
        parameters: none
        return: a dataframe of how many times each face appeared in a given roll

    jackpot:
        computes how many times the game resulted in all faces being identical
        parameters: none
        return: the number of times a jackpot occurred in the game (int)

    combo:
        computes the distinct combinations of faces rolled, along with their counts
        parameters: none
        return: a data frame of unique combinations of faces rolled and their counts
    
