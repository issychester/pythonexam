**Original code**
As the number of iterations increase, the time it takes increases exponentially from a point. It starts to increase when the number of branches reaches about 10, and before this point each iteration takes a very small (about 0s) amount of time. 18 branches/iterations takes about 0.4s. 

**Numpy code**
The same trend can be seen in the numpy and original code however, the exponential increase is sharper and starts at about iteration 15. 18 branches/iterations takes about 200s.

**Comparison**
From comparing numpy with the original code, the numpy version takes longer to run for the larger iterations because with numpy, a new array is created with each array that is appended. The original code allows arrays to be added, without creating and copying the original array each time. 
Until about iteration 15, when the numpy code increases exponentially, the time between the 2 versions is about the same (about 0s). Although the orignal code does take longer with more iterations/branches, this change is minute compared to the numpy version.