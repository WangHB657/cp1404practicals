"""
Random integers between 5 and 20.
The smallest number seen would be 5, and the largest would be 20.

Random odd numbers between 3 and 9.
The smallest number seen would be 3, and the largest would be 9.
No, line 2 could not have produced a 4 since the step size (third parameter) is 2, starting at 3.

Random floating-point numbers between 2.5 and 5.5.
The smallest number seen would be 2.5, and the largest would be 5.5.
"""

import random
random_number = random.randint(1, 100)
print(random_number)