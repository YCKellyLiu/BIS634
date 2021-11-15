# BIS634 Yuechen Liu HW4

## Exercise 1 (25 points):

### 1) Implement a two-dimensional version of the gradient descent algorithm to find optimal choices of a and b. (7 points)
Answer:
Let the error function be L (loss function) and parameter θ:[a, b]
The goal is to find an optimal set of θ parameters to minimize L, as follows:  θ^*=arg(min)L(θ)
In this task, we do not need to care about the input and output. We can directly obtain loss through Request, so we only need to adjust the parameter gradient. Let the initial parameter be θ(0):[a(0), b(0)]. As a result, I implemented the gradient descent funtion. It takes the f function, gradf funtion, and our inital guess of t, the step size alpha, and the EPS (Epsilon is a very small number to prevent any division by zero in the implementation.

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




