# BIS634 Yuechen Liu HW4

## Exercise 1 (25 points):

### 1) Implement a two-dimensional version of the gradient descent algorithm to find optimal choices of a and b. (7 points)
Answer:
Let the error function be L (loss function) and parameter θ:[a, b]
The goal is to find an optimal set of θ parameters to minimize L, as follows:  θ^*=arg(min)L(θ)
In this task, we do not need to care about the input and output. We can directly obtain loss through Request, so we only need to adjust the parameter gradient. Let the initial parameter be θ(0):[a(0), b(0)]. As a result, I implemented the gradient descent funtion. It takes the f function, gradf funtion, and our inital guess of t, the step size alpha, and the EPS (Epsilon is a very small number to prevent any division by zero in the implementation.
Citation: https://www.cs.toronto.edu/~guerzhoy/411/lec/W02/python/graddescent2d.html

### 2)  Explain how you estimate the gradient given that you cannot directly compute the derivative (3 points)
Answer:
Without knowing the exact function, we know the changing trend between parameters and loss, and we can calculate the gradient by calculating the derivative of loss and parameters (a, b). Loss decreases faster in the opposite direction of the gradient.

### 3) Identify any numerical choices -- including but not limited to stopping criteria -- you made (3 points), and justify why you think they were reasonable choices (3 points).
Answer:
In this task, when the number of iterations is less than the maximum 1000, the training is stopped. Another option is to check if the loss continues to decrease or the gradient changes near 0. The reasons for choosing these two methods are as follows: When the number of iterations is enough, the probability of obtaining the local or global minimum value of loss function by gradient descent method is increased and stops when the number of max iterations is reached. In the case of unfixed iteration steps, when iteration reaches the global or local minimum value, the gradient continues to fluctuate near the minimum value due to the existence of learning rate, and loss does not continue to decrease, so it stops.

### 4) It so happens that this error function has a local minimum and a global minimum. Find both locations (i.e. a, b values) querying the API as needed (5 points) and identify which corresponds to which (2 point).
Answer:
After training, we can find that the local minimum is 1.10000049995 when a = 0.2155, b = 0.6885; the global minimum is 1.00000149999 when a =0.7115, b = 0.1685.

### 5) Briefly discuss how you would have tested for local vs global minima if you had not known how many minima there were. (2 points)
Answer:
 1. If I had not known how many minima there were, I would try different corners and center, just like I did; I chose (0.99,0.01),(0.01,0.99)(0.01,0.01),(0.99,0.99), and (0.5,0.5) to test. Initializing multiple models with multiple different parameters is to starting the search from multiple different initial points, which may fall into different local minima, from which selection may obtain a result closer to the global minimum. 
 2. Simulated annealing accepts worse results than the current solution with some probability at each step, thus contributing to the jump out of the local minimum. In the iterative process of each step, the probability of accepting the "suboptimal solution" should gradually decrease with the passage of time, so as to ensure the stability of the algorithm. 
 3. Use random gradient descent. Different from the standard gradient descent method, the stochastic factor is added into the gradient calculation. Thus, even if it falls into the local minimum, its calculated gradient may not be zero, giving it a chance to jump out of the local minimum and continue the search.

## Exercise 2 (25 points):

### 1) Modify the k-means code (or write your own) from slides13 to use the Haversine metric and work with our dataset (5 points). 
Answer: 
I modified k-means code by removing all normalization since we need the accurate numbers; besides, I added the Haversine function from https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points

### 2,3,4)  Visualize your results with a color-coded scatter plot (5 points); be sure to use an appropriate map projection (i.e. do not simply make x=longitude and y=latitude; 5 points). Use this algorithm to cluster the cities data for k=5, 7, and 15. Run it several times to get a sense of the variation of clusters for each k (share your plots) (5 points)
Answer:
I run k =5, k =7, and k=15, each for 3 times to see the difference, and I use Basemap projection. Citation: https://matplotlib.org/basemap/users/robin.html

When k =5 
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW4_YuechenLiu/k5-1.png)
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW4_YuechenLiu/k5-2.png)
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW4_YuechenLiu/k5-3.png)

When k = 7
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW4_YuechenLiu/k7-1.png)
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW4_YuechenLiu/k7-2.png)
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW4_YuechenLiu/k7-3.png)

When k = 15
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW4_YuechenLiu/k15-1.png)
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW4_YuechenLiu/k15-2.png)
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW4_YuechenLiu/k15-3.png)

### 5) Comment briefly on the diversity of results for each k. (5 points)
Answer:
1. I run k = 5 three times. As showing in the map, the division of cities in Asia and Europe change a lot(map 1 has four divisions in this two areas; map 2 and 3 has three divisions). Besides, South America and North America are separated in the map 2&3. 
2. I run k =7 three times. As showing in the map, the clusters changing is focusing on the divisions of Europe and North America(map4 has different divisions of Europed with map5&6; the division of North America is different in all three maps).
3. I run k = 15 three times. As showing in the map, the diversity of centers is varied in the three maps. For map7, there are divisions in North America, whereas in map 8&9, the separation in North America decreased, similarly to South America and Africa; Oceania and South Asia have more separation of cities. 

## Exercise 3 (25 points):
### 1) Implement both (yes, I know, I gave you implementations on the slides, but try to do this exercise from scratch as much as possible)
Answer: 
I modified the original function by taking out the time.time function, so it won't need to rewrite and can be directly used. 

### 2,3,4,5)  Time them as functions of n (5 points), and display this in the way you think is best (5 points). Discuss your choices (e.g. why those n and why you're displaying it that way; 5 points) and your results (5 points).
Answer:
This is how I display the two functions. 
![](https://github.com/YCKellyLiu/BIS634/blob/main/q3-1.png)
![](https://github.com/YCKellyLiu/BIS634/blob/main/q3-2.png)

I display the functions by setting x axis as n, y axis as time, to better displaying the time consumption. I use time.time to calculate the time consuming for each function. In the first function, I set n = 40, and we can see in the first graph, the time consuming is increasing. The time consuming is 2.25s/it in the first function. When I use lru_cache in the second function, according to the graph, we can see that the time consuming is approximate to 0(some outliers, but they are to small to ignore), and the time consuming is 192899.78it/s. As a result, we can conclude that using lru_cache is much more efficient. The reason that using lru_cache more efficient is that there are generally memory items that are added once and never used again, and there are items that are added and used frequently. LRU is much more likely to keep the frequently-used items in memory. Citation: https://stackoverflow.com/questions/2058403/why-is-lru-better-than-fifo

## Exercise 4 (25 points)

### Implement a function that takes two strings and returns an optimal local alignment (6 points) and score (6 points) using the Smith-Waterman algorithm; insert "-" as needed to indicate a gap (this is part of the alignment points). Your function should also take and correctly use three keyword arguments with defaults as follows: match=1, gap_penalty=1, mismatch_penalty=1 (6 points). Here, that is a penalty of one will be applied to match scores for each missing or changed letter.Test it, and explain how your tests show that your function works. Be sure to test other values of match, gap_penalty, and mismatch_penalty (7 points).
Answer: 
I first create a function called 'best_matrix' to create the matrix based on the two sequences. The function includes the matrix with the max score, max score position, and the matrix with socre. Citation: https://tiefenauer.github.io/blog/smith-waterman/ 
Next, I create a function called 'go', to actually show how to move in the matrix by recording the position in the matrix. If "diagonal", means match; if "up", means a gap in sequence b; if "left", means a gap in sequence a. Citation: https://stackoverflow.com/questions/23400317/smith-waterman-algorithm-to-generate-matrix-in-python
Besides, I create a function called 'traceback' to decide which way to traceback in the matrix. It has three conditions, which are left, up, and diagonal. Align is inserted "-" as needed to indicate a gap. Citation: https://stackoverflow.com/questions/12666494/how-do-i-decide-which-way-to-backtrack-in-the-smith-waterman-algorithm

Finally, I create a function called 'align' to combine the three functions and get the final align. 

To test if functions are correct, I compared with the official website: http://rna.informatik.uni-freiburg.de/Teaching/index.jsp?toolName=Smith-Waterman
and the answer is the same. 
Say, when  match=1, gap_penalty=1, mismatch_penalty=1 
Mine: 
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW4_YuechenLiu/gap1-1.png)

Website(cannot see the complete matrix in the screenshot, but can see the result):
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW4_YuechenLiu/gap1-3.png)
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW4_YuechenLiu/gap1-2.png)

When  match=1, gap_penalty=2, mismatch_penalty=1 
Mine:
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW4_YuechenLiu/gap2-1.png)

Website:
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW4_YuechenLiu/gap2-2.png)
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW4_YuechenLiu/gap2-3.png)

I also used other two sequences to test the function.
sequece 1: 'agcccagcgat'
sequence 2: 'ttcaagctag'

When  match=2, gap_penalty=2, mismatch_penalty=1 
Mine:
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW4_YuechenLiu/4-1.png)

Website:
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW4_YuechenLiu/4-2.png)












