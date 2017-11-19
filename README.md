# Mario-Kart-8-Blender-Path-XML-Exporter
This is a tool for exporting path data into a usable convertable XML format for yamlconv.


## This tool is in beta! I do not advise using this until I release this in the releases section of this. Many things are not complete or simply not usable yet. 

## Supports:

- Lap Paths
- Gravity Paths
- Glide Paths
- Enemy Paths
- Return Points (normals and tangents too)
- Grouping paths (by blender layers)

**Done but not added yet to addon:**

- GCamera
- Item Paths
- Replay Camera
- Intro Camera

**Not supported YET**

- Object Path (will be done by key frames)
- Pull paths


**Todo**

- Create a good enough object to repesent enemy paths
- UI for path properties
- UI for auto selecting and hiding paths
- UI for converting path types to easily make paths. (Example, duplicate lap paths and convert to enemy paths to instantly make them or use as a base)
- Export object path via key frame data
- Viewable intro camera (possbily export off of keyframes too
- Override ID system with UI (For more than 2 groups to branch out to)



## How to use:


-Open blender. Get the program here if you do not have it. [blender](https://www.blender.org/download/)

Install by going to File - User Preferances - Add ons tab
Click Install Add On by file at the bottom then click the zip. Check the add on to be active and Save User Settings

-In the program use Shift + A to open a menu. This will have the "mesh" option on the top. 
Select it and at the bottom choose your path type.

## Path types:

	Lap Paths determine the boundries from one path to another where Latiku would grab the player. These work identical to how MKWII worked. 

	Enemy Paths are simply points that enemy goes towards. 

	Glider paths pull the player towards. The boxes represent how far you can glide on the side

	Gravity paths are the boundries of anti gravity from one path to another. The first path enables anti gravoty, last one disables it.

	Intro camera works as a path on where to move

	Replay camera are points to view angles of where the player is moving or other things

	Item Paths are simply points items go towards. Generally these can be the same as enemy ones

	
To start you will want to do two paths. A lap path, then an enemy path. Then work your way and do more.

To group paths if they split or if you have multiple glider or gravity sections, press "M" key and add them to the next layer. 

Export with file - export and copy the contents of the XML over to a converted byaml with [yamlconv](https://github.com/Chadderz121/yamlconv)



More details and specifics on this in a video tutorial


## Credits:

KillzXGaming - Worked on code for each path and setup a layout to work with yamklconv

AboodXD  - helped alot with the code

Chadderz - yamlconv 

Wexos - helping me figure out tangent and normal rotation values for return points

Blender Team - Blender api stuff and basic templates to work off of. 

