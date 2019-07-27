# trigfunctiongraph
The program can graph basic cosine and sine functions. Currently, the range is from 4 units in the positive and negative 
directions, and the domain is 5pi in the positive and negative direction. The program prompts the user for different 
components of the sine/cosine functions, such as the amplitude, the period length, the phase shift, and the vertical shift. 
The program utilizes a library of graphics for python called graphics.py. The calculation formula goes something like this:
asin((2pi/k)*(x-c)) + d, where x is the angle degree. I will be working towards being able to customize the ranges of possible 
values for each axis beyond its current limit in the near future. Error-trapping for the most part has been included, prompting
the user to re-enter information if they enter invalid information etc. 
