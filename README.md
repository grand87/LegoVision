# Lego Recognition Project 2018

## Ideas
* 1. Provide solution to easily locate the required brick in the huge amount of Lego Bricks with Mobile phone camera in real time
* 2. Recognition of Lego bricks on photo or on video in real time with suggestion for which Lego set this brick is aceptable
* 3. Recognition of Lego bricks on photo or on video to generate DB of bricks and suggest suitable Lego Sets to build with availible bricks.
	* Additional point show which bricks are missing for the selcted Lego Sets
* 4. Wow effect: AR in real time to highlight recognized blocks with glow effect & notes about brick on the side:
	* acceptable sets
	* animated brick 3d model (aka in Terminator Vision mode - https://www.youtube.com/watch?v=6uPUhqR6zCo)

### Use cases
* Ideas might be implemented as Mobile apps with offline recognition engine
* Ideas might be implemented as Web Service with\without Mobile App  

### Monetization
* Mobile app & web service might have subscription plan for more robust\precise recognition

### Related projects
https://jacquesmattheij.com/sorting-two-metric-tons-of-lego
http://www.i-programmer.info/news/105-artificial-intelligence/10892-diy-ai-to-sort-2-metric-tons-of-lego.html
https://spectrum.ieee.org/geek-life/hands-on/how-i-built-an-ai-to-sort-2-tons-of-lego-pieces

## Implementation
1. Recognition objects on the photo
2. Based on objects rects from 2D image send these 2D regions to the recognition engine
	2.1 Need to define solution how to distinguish small lego bricks from other big objects and skip reduntand recognition
3. Objects recognition:
	3.1 Develop 2 class recognizer: Lego or not Lego
	3.2 Develop 10 class lego brick recognition model:
		3.1.1 Brick
		3.1.2 Lego Minifigure
		3.1.3 Pimptic ))
		3.1.4 Lego plates
		3.1.5 
		
### Recognition approaches
1. Features based recognition model
2. Convolutional (CNN) recognition model

## Tasks
1. Locate known lego Brick (means we have image with exact Lego Brick) in the huge amount of other bricks - https://docs.opencv.org/2.4/doc/tutorials/features2d/feature_homography/feature_homography.html
2. 	

## Demos
1. AR application which locates lego brick & recognizes it. Highlights the brick on camera and shows pop-up with additional information (name, and glowing animated rotated model)
	1.1 For the POC might pre-select 10 very different lego bricks to simplify recognition task
2. Lego Minifigure face location on image
	2.1 prepare dataset with lego heads
	
## Articles

### 3D generated rendered dataset
I got inspiriation after the article https://shapenet.cs.stanford.edu/projects/RenderForCNN/. My ideas is to use LeoCAD + LDView + POV-Ray to generate set of images wiht real environment but rendered Lego bricks.
These images would contain suplimentary metadata about the brick - exact position, amount of visibel dots, angle, distance, dimensions, etc.
