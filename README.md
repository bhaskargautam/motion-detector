# Motion Detector Interface for Touch Screen

The screen has 6 touch points (A to E) arranged as  below:

DAE

DBE

DCE

FFF 

## Features
* The class is capable of detecting the Right and Left Swipes based on pre-defined order of touches.
* MotionDetector class provides a method *update* for feeding in the six touch inputs as int (0 tp 4095).
* It keeps tracks of inputs provided in last 1 second and converts them to order list of touch points.
* Easy to add more gestures by providing ordered list of expected touches.
* Unit Test Cases for MotoonDetector Class.

## Todo:
* UP/Down Swipes
* Tapping and Double Tapping
* Hitting and Slapping ??
* Flicking
* Rubbing ??
* Simiplify Ordered List of motions.
