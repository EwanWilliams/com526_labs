# Week 4 Task

This week we looked at intelligent agents. Now you are tasked with building a system based of the scenario from the 
lecture

You can find a very simple demo [here](https://github.com/darrened/526/tree/main/Week4/demo)

This is a large programming task, it is highly likely you will need to revisit it over the week

In this task you are given a number of classes.  
These classes make up a system in which a 'fire fighting' robot will explore an environment, attempting to put out 
'flames'. 

I have broken this system up in to different levels, thus you can decide how far you wish to go - frankly, a system like 
this can be endlessly expanded with more and more advanced functionality.

First, lets look at the classes:
* [Environment](https://github.com/darrened/526/tree/main/Week4/environment.py) - The heart of the system. Contains the
map and facilites all data requests and interactions with said map
* [Agent](https://github.com/darrened/526/tree/main/Week4/agent.py) - An abstract class providing the base functionality 
for all agents. Any agents should inherit from this class!
* [WaterStation](https://github.com/darrened/526/tree/main/Week4/water_station.py) - A concrete implementation of the 
agent class - representing the water station. You will need to complete much of this functionality
* [Robot](https://github.com/darrened/526/tree/main/Week4/robot.py) - Also a concrete implementation of the Agent class. 
Most of your coding work will likely be done in this class (along with environment)
* [Flame](https://github.com/darrened/526/tree/main/Week4/flame.py) - Not currently an agent. just allows the flames to 
be displayed when printing the map

Other files included:
* [utils.py](https://github.com/darrened/526/tree/main/Week4/utils.py) - Useful functions and imports
* [map.txt](https://github.com/darrened/526/tree/main/Week4/map.txt) - Is used by environment.py - you can reconfigure 
the map by modifying this file (x = obsticle, * = flame, s = water station, r = robot)

## Tasks

### Stage 1
Modify the above program so that the water station will:
* Sense if a robot is next to it
  * If there is a robot then the water station should call a provided method on that robot that refills its water tank
  * If there is no robot - the water station should simply idle

Modify the above program so that the robot will:
* Move randomly around the map
  * It should only enter a free space on the map. If the space is occupied by any other thing, then the robot should not 
  see that as a viable space to move in to.

### Stage 2
Modify the above program so that the robot will:
* Sense any flames that are next to it.
  * If a flame is next to it, then it should put said flame out losing 5% of its water in the process.
  * If there are multiple flames next to it, it should pick one at random to tackle first. It will then tackle the other 
  on the next sense -> decide -> act cycle.

### Stage 3
Modify the above program so that the robot will:
* Sense if it is next to the water station.
  * If it is, then it should record the location.
  * The provided system only had 1 water station, if you have modified this then you will need to 
  account for that.
* Factor its water level in to decision-making. If it does not have enough water to tackle flames then it should start 
heading directly to the water station (using A*). However, it should only do this if it knows the location of the water 
station. If it doesn't, then it should roam around hoping to happen across it.

### Stage 4
Modify the above program so that the robot:
* Now has its own map.
  * This map will just be all question marks
  * As the robot moves around sensing, it should uncover/update more of the map 

### Stage 5
Modify the above program so that the robot:
* Uses its map to move directly to any known locations of flames. It should use A* to do this
* Uses its own map when using the A* to find its way back to the water station

### Stage 6
Modify the above program so that:
* Flames are now agents
  * These flames will sense the surrounding cells.
    * If there are no free cells, then the flame will idle
    * If there is a free cell then the flame will count up how many other flames are around it:  
    each neighbouring flame will stack a 10% change that the flame will spread to a randomly selected neighbouring free 
    space.  
    However, if there are no other flames nearby, then it will not spread.  
  
With this, the robot may need help!
Thus, you will need to add a couple of more robots to the map!
Update the robot class so:
* If two robots encounter one another, they will share information about where any flames are located.
* They will update their individual maps accordingly