# BIS634 Yuechen Liu HW5

## Exercise 1 (25 points):

### Perform any necessary data cleaning (e.g. you'll probably want to get rid of the numbers in e.g. "Connecticut(7)" which refer to data source information as well as remove lines that aren't part of the table). Include the cleaned CSV file in your homework submission, and make sure your readme includes a citation of where the original data came from and how you changed the csv file. (5 points)
Answer: 
I select the rows with over 10 elements using csv lib.
Citation: The original data came from "https://statecancerprofiles.cancer.gov/incidencerates/index.php?stateFIPS=00&areatype=state&cancer=001&race=00&sex=0&age=001&stage=999&year=0&type=incd&sortVariableName=name&sortOrder=asc#results" 
1)download the data from above address 
2)create a new .csv file to save the cleaned data: "new_incd.csv" file 
3)set a number 10 to select the rows, because the useful data has over 10 dims 
4)get rid of the numbers in e.g."Connecticut(7)": manually delete numbers, '(', and ')'. 
5)manually organize the names of the columns.

### Using Flask, implement a server that provides three routes (5 points each)You've now completed most of this course, so you're now qualified to choose the next step. Take this exercise one step beyond that which is described above in a way that you think is appropriate, and discuss your extension in your readme. (e.g. you might show maps, or provide more data, or use CSS/JS to make the page prettier or more interactive, or use a database, or...) 
Answer: 
1)include two .html files (homepage.html and errorpage.html)
2)Searching for state names is not case-sensitive and space-insensitive
3)test:
http://localhost:5000/
return {"Age-Adjusted Incidence rate (cases per 100K)":"517.8","State":"Kentucky"}
http://localhost:5000/state/Kentucky
return {"Age-Adjusted Incidence rate (cases per 100K)":"517.8","State":"Kentucky"}
http://localhost:5000/info?state_name=Kentucky
return {"Age-Adjusted Incidence rate (cases per 100K)":"517.8","State":"Kentucky"}
4)use css to decorate, saving to style.css file.

The homepage: 
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW5_YuechenLiu/Q1-1.png)

The info page:
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW5_YuechenLiu/Q1-2.png)

The error page:
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW5_YuechenLiu/Q1-3.png)

## Exercise 2 (25 points):

### Extend the basic binary tree example from slides2 into a binary search tree that is initially empty (5 points).  Provide an add method that inserts a single numeric value at a time according to the rules for a binary search tree (5 points).
Answer: 
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW5_YuechenLiu/Q2-1.png)

### Replace the contains method of the tree with the following contains method. The change in name will allow you to use the in operator; e.g. after this change, 55 in my_tree should be True in the above example, whereas 42 in my_tree would be False. Test this.
Answer:
The test tree is [55, 62, 37, 49, 71, 14, 17]. I test if 55, 42,71, and 4 are in the tree, and the answer is true, false,true, false. 
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW5_YuechenLiu/Q2-2.png)

### Using various sizes n of trees (populated with random data) and sufficiently many calls to in (each individual call should be very fast, so you may have to run many repeated tests), demonstrate that in is executing in O(log n) times; on a log-log plot, for sufficiently large n, the graph of time required for checking if a number is in the tree as a function of n should be almost horizontal. (5 points).

Answer: 
As shown in the below plot, the in is executing in O(log n) times.
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW5_YuechenLiu/Q2-3.png)

### This speed is not free. Provide supporting evidence that the time to setup the tree is O(n log n) by timing it for various sized ns and showing that the runtime lies between a curve that is O(n) and one that is O(n**2). (5 points)
Answer: 
This way is to draw two graphs of extream situation,O(n) and O(n**2), which means that the runtime must lie between those two curves. 
If the input secquence is random enough, the tree is almost balanced and the setup time is O(n), as shown below:
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW5_YuechenLiu/Q2-11.png)
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW5_YuechenLiu/Q2-4.png)

However, if the input is inversely sorted, than the setup time is O(n**2):
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW5_YuechenLiu/Q2-12.png)
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW5_YuechenLiu/Q2-5.png)
If I create a function and put actual time spend, n**2, and n in one graph:
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW5_YuechenLiu/Q2-13.png)
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW5_YuechenLiu/Q2-6.png)
As we can see from the above graph, the actual running time lies between O (n**2) and O (n).

## Exercise 3 (50 points):