Shooters do not have problems with with vertical deviation, so we can use a simplified model for this mission.
We placed a camera above the shooting range and use 
[Cartesian coordinates](http://en.wikipedia.org/wiki/Cartesian_coordinate_system) to describe states.
We know coordinates of wall (target) ends and shooting point.
And we know the point where is a bullet after a small time.
You should determine the result of the shot.

You are given coordinates for the end-points of the target wall on a grid.
In addition, you have two points describing the shot: A starting point where the bullet was fired,
and a second point indicating the location of the bullet after a specified length of time.
You should calculate the result of the shot, specifically if a bullet hit the wall in the center,
then it's 100 points. Awarded points reduce in relation to the distance from the center.
An impact on the end of the wall is 0 points and a missed shot deducts a point (-1).
The result should be [rounded to the nearest integer](http://en.wikipedia.org/wiki/Rounding#Rounding_to_integer).

![Wall](bullet-wall.svg)
