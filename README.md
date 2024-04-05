Inspired by Joma's favorite interview question [Can you solve my favorite interview question? (math + cs)](https://www.youtube.com/watch?v=pvimAM_SLic), this project further visualizes the dots within the circle and those out of the circle.\
\
This question uses random to generate number from 0 to 1 and ask the number pi.\
\
The trick behind this question is that we have to imagine a circle with radius 1 and a square with a side length of 1.\
$$\frac{\pi r^2}{(2r)^2} = \frac{\text{Number of points inside the circle}}{\text{Number of total points}}$$
Calculate the distance between each point and see if they are within the radius 1.\
The 4 times of the radius between the number of point within the circle and the total number of point is pi!\
\
For more, we can look up [Monte Carlo](https://www.geeksforgeeks.org/estimating-value-pi-using-monte-carlo/), using abundant random number to obtain a targeted result.
