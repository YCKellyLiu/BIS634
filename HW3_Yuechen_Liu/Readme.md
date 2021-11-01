### Question 4 
#### Describe in words how you would parallelize this algorithm to work with two processes.
Answer:
Original data: 14, 1, 18, 2, 16, 4, 7, 21
STEP1: Assign to two processors P0 and P1:
P0: 14, 1, 18, 2 P1: 16, 4, 7, 21
Step2: P0 and P1 quickly sort the two sets of data:
P0: 1, 2, 14, 18 P1: 4,7,16,21
Step3: Compare the smallest number in P0 with the smallest number in P1, 1 in P0 is smaller than 4 in P1, and then proceed to the next step, continue to compare the second number,2, in P0 with 4 in P1, and set the smallest number in P1 using insertion sort in P0, and P1 is inserted between 2 and 14 of P0. At this time, there are:
P0: 1,2,4,14,18 P1: 7,16,21
Step4: Insert the 7 of P1 from the 4 of P0 to the back to sort, recursively, and finally we have: 
P0: 1, 2, 4, 7, 14, 16, 18, 21
After sorting, P1 is empty.

Original link: https://blog.csdn.net/xudong_98/article/details/51622219

#### How you would validate the results and the speedup?
Answer: For validate the result, we can use both merge sort and parallel merging sort to process one group of data, to test if they can have the same result. For the speedup, we can import time module in python, to get the working time of both algorithms. Normally, parallel merging sort will be faster. Parallel merging algorithm is very effective in processing large amounts of data, but the performance of traditional merging algorithm is very poor, because each time the merging process, the processor will be reduced by half, aggravating the data length processed by each processor. When merging to the end, only one processor processes all the data, which is very slow. As a result, the merge sort algorithm must be parallelize to achieve the maximum advantages.

