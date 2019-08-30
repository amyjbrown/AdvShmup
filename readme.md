# AdvShmup
Scrolling shoot-em-up (shmup) game built in Python 3 and Pygame 1.9.  
By *Amy Brown*  
This was created as a challenge to built a fast, efficient, and modular game framework/engine in Python that can be re-used for future projects with no dependencies aside SDL.

![](https://github.com/jonathanabrown/AdvShmup/blob/master/AdvShmupscreenshot.png)

## Design Features
  * *Fully modular Scene system*  
  Interaction modes are reified as fully seperate Scene objects, which hold their states and methods for handling input, allows for easily adding or removing Scenes and testing them in isolation.  
  `Scenehandler` is a Statemachine serves as an abstraction interface allowing for scenes to arbitrarily load each other. 
  * *User Input Abstraction*
  The `inputhandler` module serves as a standalone user-input abstraction layer, which allows for arbitrary logical inputs to be added and mapped to real system-inputs
  * *Resource loading interface*  
  A system for loading and caching visual assets with paramters (size, resolution, loading items as a spritesheet) that can be then be accessed with no additional lookup time allows for less of a headache in managing assets
  * *Fast Speed*  
  The game currently runs at 60 FPS by design, but will run at whatever the refresh rate of your monitor is
  * *No depdencies*  
  All assets and code are original, and rely on no-external library

## Game and Controls
The goal of this game is to fight off endless waves of asteroids and gain a highscore. Health can be gained via the green medpack items.   
**W,A,S,D**  
Move Ship  
**SPACE**  
Shoot cannons  
**ESCAPE**  
Quit the game  
