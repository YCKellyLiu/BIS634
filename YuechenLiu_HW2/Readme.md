# BIS634 Yuechen Liu HW2

## Exercise 1 (30 points)

### 1) Examine the contents of hw2-patients.xml  Download hw2-patients.xmlin a text-editor to see its structure, but in brief, there are a handful of fields you can ignore for this exercise and then several <patient> entries, all contained inside <patients>. Each <patient> has several attributes that we will want, namely name, age, and gender. Some patients have other associated data (e.g. diagnoses), but we won't need that here.
#### Load the data. Plot a histogram showing the distribution of ages (2 points).
Answer:

![](https://github.com/YCKellyLiu/BIS634/blob/main/YuechenLiu_HW2/1.png )

The distribution of ages: most patients are around 20~60 years old.

#### Do any of the patients share the same exact age? (2 points) 
Answer:
No.
#### How do you know? (2 points).
Answer:
Use set() to eliminate duplicated elements, because a set cannot have duplicated elements. If it returns TRUE, it means that there is no duplicate in the age list,which means no patients share the same age. 

### 2) For an extra 2 points: explain how the answer to the question about multiple patients having the same age affects the solution to the rest of the problem.
Answer: If there are multiple patients having the same age, we can still use binary search, but the search time will be different. For example, if multiple patients are 41.5 years old, using binary search can find one 41.5, and then traverse left or right to find the boundary of all "41.5" numbers. The total time will be O(n); even in the worst situation that all numbers are the same, it will cost n/2 time, still the O(n)time.

### 3）Plot the distribution of genders. (2 points).
Answer:
![](https://github.com/YCKellyLiu/BIS634/blob/main/YuechenLiu_HW2/2.png)
 #### In particular, how did this provider encode gender? 
 Answer: 
 The provider uses string to encode gender.
 #### What categories did they use? (2 points)
 Answer: 
Three categories: 'female','male', and 'unknown'.

### 4) Sort the patients by age and store the result in a list (use the "sorted" function with the appropriate key, or implement sort yourself by modifying one of the algorithms from the slides or in some other way). (2 points)
Answer:
Sort the patients by age and store the result in a list. Zip age and name as tuples store in a list, then locate the last one in age, which will give the name of the oldest person. The oldest patient is 'Monica Caponera'. 

### 5）Identifying the oldest person from a list sorted by age should be an O(1) task... but sorting is an O(n log n) process (assuming we're using an efficient algorithm), so the total time for the above is O(n log n). Describe how (you don't need to implement this, unless that's easier than writing it out) you could find the second oldest person's name in O(n) time. (2 points). 
Answer:
To draw the secondary oldest patient, we need find the oldest patient first, which needs O(n) time, and then remove this patient(tuple) from the zip_list(age and name), which is O(1) time; and now use the function to find the oldest patient in the new zip_list,which needs O(n) time. The total time consums will be O(n)+O(1)+O(n)=O(n)

#### Discuss when it might be advantageous to sort and when it is better to just use the O(n) solution. (2 points).
Answer:
Advantage
Sort: O(n log n) time: when you have to find different elements in a list for many times, you only cost nlogn + n time; sort the list first will be great.
Not sort: O(n) solution, when you just want to find the element once or a few times. 

### 6）Recall from our discussion of the motivating problem for September 9th that we can search within a sorted list in O(log n) time via bisection. Use bisection on your sorted list (implement this yourself; don't trivialize the problem by using Python's bisect module) to identify the patient who is 41.5 years old. (2 points)
Answer:
Citation:https://towardsdatascience.com/understanding-time-complexity-with-python-examples-2bda6e8158a7
Use binary search, I find the position of the patient who is 41.5 years old is No.173886 in sorted age list. Then I locate the number in the zip list(age, name), and find the patient name:'John Braswell'
 
### 7) Once you have identified the above, use arithmetic to find the number of patients who are at least 41.5 years old. (2 points)
Answer:
len(sorted_patient)-173886 = 150471
There are 150,471 patients who are at least 41.5 years old.

### 8) Generalizing the above, write a function that in O(log n) time returns the number of patients who are at least low_age years old but are strictly less than high_age years old. (2 points) 
Firstly I use bineray search, but because the question asks "strictly less than high_age years old", I change "while left <= right" to "while left < right". Then I write another function to calculate how many patients in the age range. 

#### Test this function (show your tests) and convince me that this function works. (2 points). (A suggestion: sometimes when you're writing high efficiency algorithms, it helps to make a slower, more obviously correct implementation to compare with for your tests. Be sure your function works both for ages that are and are not in the dataset.)
Answer:
I use 22 years old and 66 years old to test the function, and I get 184,198 patients in this age range.
To prove this function works, I use for loop to count how many patients in the age range; if the bisection function works, the result will be the same. The for loop function gives the same answer, 184,198 patients. Besides, I also check the time of using these two functions seperately. The time of using bisection is 0.0031239986419677734 seconds, and the time of using for loop is 0.5042462348937988 seconds. Clearly, bisection is much faster. 

### 9) Modify the above, including possibly the data structure you're using, to provide a function that returns both the total number of patients in an age range AND the number of males in the age range, all in O(log n) time as measured after any initial data setup. (2 points).
Answer:
Firstly, I zip age list and sex list to get patient2, which is a list of tuples. Then I change my bisection function a little bit, since I create a list of tuples for male this time. The new bisection function is called bisection2. Finally, I create the function to get both numbers of males and total patients in a age range by using bisection and bisection2.

#### Test it (show your tests) and justify that your algorithm works. (2 points)
Answer:
I use age range 22~66 years old to test the function, and the result is: The total number of patients betweeen 22 years old and 66 years old is 184,198 AND the number of males in the age range is 90,378. Since "the total number of patients betweeen 22 years old and 66 years old is 184,198" has been proved from 8) question, I only test the number of males by using for loop. I use for loop to count how many males in the age range; if the bisection function works, the result will be the same. I create a list that stores all the male patients.
By using the for loop function (same function for_loop_test), I get the same result as using bisection, 90,378 males.

## Exercise 2 (25 points)
### Download and uncompress the latest Human Reference Genome(GRCh38.p13) from https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/001/405/GCA_000001405.28_GRCh38.p13/GCA_000001405.28_GRCh38.p13_genomic.fna.gz (Links to an external site.)The above should create the file GCA_000001405.28_GRCh38.p13_genomic.fna. This is a FASTA file a little over 3 GB in size, representing the about 3 billion bases in the human genome.(The Human Reference Genome is a product of the Genome Reference Consortium. It is a composite sequence representing no individual human but primarily derived from 11 individual humans. Other projects are trying to characterize the diversity possible across the species.)

### 1) Write code to loop through all 15-mers, subsequences of 15 bases within chromosome 2 (CM000664.2).  (5 points)
Answer:





## Exercise 3 (20 points)
### 1) Your friend says to you, "you have to help me! I'm supposed to present in lab meeting in less than an hour, and I haven't been able to get the simplest thing to work!" After you help them calm down, they explain: through a collaboration with a fitness app, they have a 4GB file of high-precision weights of exactly 500 million people throughout the world. Even with 8GB of RAM, they get a MemoryError when trying to load the file in and find the average weight. They show you their code which worked fine when they tested it on a small number of weights:

with open('weights.txt') as f:
    weights = []
    for line in f:
        weights.append(float(line))
print("average =", sum(weights) / len(weights))
Aha! You exclaim.
Explain what went wrong (6 points)
Remember, your friend has to present soon, so keep your answers concise but thorough.

#### Answer: 
Python is different with other language when using memory.
In the following pitcure, we can see that Python store 100 int numbers using 904 Bytes, but C language only uses 400 Bytes.
![](https://github.com/YCKellyLiu/BIS634/blob/main/YuechenLiu_HW2/3.png)
When looping the 500 million float numbers in the file, it will need 4 GB (since the data is high-precision in this file, one float needs 8 Bytes; 8 Bytes* 500million = 4 GB). Besides, Python has a fair amount of per-object overhead (object header, allocation alignment, etc.)，so Python needs extra memory to describe the data structure. 
Hence, the total memory using is excess. 

### 2) Suggest a way of storing all the data in memory that would work (7 points)：
Using Numpy to store all the data in memory may save some extra memory; if still not work, use a lower-precision numeric type other than 8-Byte float to save each weight.
Besides, my friend can also use computational method (math)/function to solve this problem, so every number can be calculated instead of using huge memory to store. For example, the human weights may have normal distribution. However, we do not know how the data is distributed in the data set, so this method may not be useful. 

### 3) Suggest a strategy for calculating the average that would not require storing all the data in memory (7 points).
Use Welford’s method: This is an online algorithm that computes both the mean and the variance by looking at each datapoint once and using O(1) memory. Or do not create the list. Set count=0, weight = 0. When count+=1, the count updates, and weight adds float(line), but only need the memory of two numbers: one number is the sum result, the other number is the len(weights).


## Exercise 4 (25 points)
### 1) Identify a data set online (10 points) that you find interesting that could potentially be used for the final project; the main requirements is that there needs to be many (hundreds or more) data items with several identifiable variables, at least one of which could be viewed as an output variable that you could predict from the others.
Answer:
Data set name: Foodborne Disease Outbreaks, 1998-2015
https://www.kaggle.com/cdc/foodborne-diseases
Using the dataset from January 1998 to December 2015 to analyze what contaminant has been the major factor responsible for most illnesses.
The original data set is consisted of 19119 rows and 12 columns(variables).
The output variable can be the mortality rate, morbidity rate and so on. 

### 2)Describe the dataset (10 points) Your answer should address (but not be limited to): how many variables?
Answer:
The total variable is 12. 
Data fields description(columns description)
Year: Year when the disease outbreak occurred
Month: Month when the disease outbreak occurred
State: U.S States where the disease outbreak occurred
Location: Location where the food was prepared 
Food: The food which was contaminated
Ingredient: Contaminated Ingredient
Species: Pathogen/Toxic Substance causing the incontamination
Serotype/Genotype: The type of Pathogen
Status: Status whether the pathogen was cofirmed or not
Illnesses: Number of illnesses 
Hospitalizations: Number of Hospitalizations
Fatalities: Number of fatalities

### 3)Are the key variables explicitly specified or are they things you would have to derive (e.g. by inferring from text)?
Answer:
Yes. The key variables(Illness,hospitalizations, fatalities,etc.)are clearly specified, but the researcher has to do statistically 
analysis based on those.

### 4) Are any of the variables exactly derivable from other variables? (i.e. are any of them redundant?)
Answer:
The original data set has no redundant. 

### 5)Are there any variables that could in principle be statistically predicted from other variables? 
Answer:
Mortality rate, Morbidity rate and so on.

### 6)How many rows/data points are there? 
Answer:
The original data set is consisted of 19119 rows and 12 columns(variables).
After cleaning, there are 5202 rows and 10 variables in the new data set (The data cleaning process is in Jupyter Notebook named Q4).

### 7)Is the data in a standard format? 
Answer:
After cleaning, the current data set is in a standard format.

### 8)Describe the terms of use and identify any key restrictions (e.g. do you have to officially apply to get access to the data? Are there certain types of analyses you can't do?) 
Answer:
This is a public dataset owned by CDC. The researcher can access to the data set without asking permission. 
For now, there are no certain types of analyses the researcher cannot do. 



