# BIS634 Yuechen Liu HW2

## Exercise 1 

### Use the requests module (or urllib) to use the Entrez API (see slides8) to identify the PubMed IDs for 1000 Alzheimers papers from 2019 and for 1000 cancer papers from 2019. 
Answer:
Citation: https://stackoverflow.com/questions/317413/get-element-value-with-minidom-with-python
I create a function called get_id(disease); when input the disease name, say, Cancer, the funciton will grab the id of Cancer paper, and add it to a list by for loop. For test whether the function works, I get the length of the two lists, and the answer is 2000. 

### There are of course many more papers of each category, but is there any overlap in the two sets of papers that you identified? 
Answer:
I create a function called overlap(disease1,disease2); when input the two disease names, we can check if the two disease papers have overlap by checking if they have duplicate ids. I use 'set' to check it, and get the result is '32501203'.

### Use the Entrez API via requests/urllib to pull the metadata for each such paper found above (both cancer and Alzheimers) (and save a JSON file storing each paper's title, abstract, MeSH terms (DescriptorName inside of MeshHeading), and the query that found it that is of the general form
Answer:
Citation: https://www.geeksforgeeks.org/python-ways-to-create-a-dictionary-of-lists/  https://docs.python.org/3/tutorial/errors.html
I create a function called get_info(disease1,disease2) in order to combine two dictionaries into one for better use in the future. I met problems when adding paper information into the json file, such as there is missing value in title, so I use if & else to catch the issue to make sure that the json file can be finished. Finally, I save the json file called pmbi2000.json.

### Some papers like 32008517 (Links to an external site.) have multiple AbstractText fields (e.g. when the abstract is structured). Be sure to store all parts. You could do this in many ways, from using a dictionary or a list or simply concatenating with a space in between. Discuss any pros or cons of your choice in your readme 
Answer: 
I use for loop to go through all child nodes, and if the child is None, the function will print"someone is missing abstract"; if it is not null, the function will add it to the "abstract". i think the advantage may be in this way, the function can avoid possible attribute errors, so the function can process smoothly regardless the format of the abstract; the potential disadvantage may be it will cost more time to check if there is missing abstract. 

## Exercise 2 
### Q2.1What fraction of the Alzheimer's papers have no MeSH terms? 
Answer: 
I create a function called mesh_fraction(disease) to calculate the fraction of the disease's papers having no MeSH terms. The function firstly conut the number of empty MeSH papers, and divided it by the total number of papers. When the disease is ALZHEIMERS, the result is 0.165, which means that there are 16.5% of Alzheimer's papers without MeSH terms. 

### Q2.2 What fraction of the cancer papers have no MeSH terms? 
Answer:
The answer is 0.759, which means that there are 75.9% of Cancer's papers without MeSH terms.

### Comment on how the fractions compare. (1 point; i.e. if they're essentially the same, do you think that's a coincidence? If they're different, do you have any theories why?)
Answer:
The two results are totally different. I think the one potential reason is that because cancer is a really broad term, which it has many subterms such as breast cancer, stomach cancer, etc.. Compared with cancer, Alzheimer is a more narrow term, which maybe the missing MeSH terms percentage is fewer than Cancer. #https://www.definitivehc.com/resources/glossary/medical-subject-headings-mesh

### What are the 10 most common MeSH terms for the Alzheimer's papers whose metadata you found in Exercise 1? 
Answer:
Citation: #https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
I create function called mesh_count(disease) to count how many MeSH headings(terms) in each disease, and for Alzheimer, the function returns a list of MeSH terms with the count of each term. Then I create a function called first_ten_items(disease) to get the first ten common MeSH terms for Alzheimer papers. The top ten are: Humans, Alzheimer Disease, Male, Female, Aged, Animals, Amyloid beta-Peptides, Brain, Aged, 80 and over and Cognitive Dysfunction.

### Provide a graphic illustrating their relative frequency. 
Answer: 
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW3_Yuechen_Liu/top10_A.png)

### What are the 10 most common MeSH terms for the cancer papers whose metadata you found in Exercise 1? 
Answer:
I use mesh_count(disease) and first_ten_items(disease) to get the first ten common MeSH terms for Cancer papers. The top ten are Humans, Female, Male, Middle Aged, Aged, Adult, Animals, Retrospective Studies, Neoplasms, Treatment Outcome.

### Provide a graphic illustrating their relative frequency.
Answer:
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW3_Yuechen_Liu/top10_C.png)

### Make a labeled table with rows for each of the top 5 MeSH terms from the Alzheimer's query and columns for each of the top 5 MeSH terms from the cancer query. For the values in the table, provide the count of papers (combined, from both sets) having both the matching MeSH terms.
Answer:
Citation: #https://towardsdatascience.com/how-to-easily-create-tables-in-python-2eaea447d8fd
In order to get top 5 MeSH terms, I change the above function a little bit to create a new one called first_5(disease). Then, for the table, I first create a matrix, and for loop the count of top five Mesh Terms paper in to the matrix. Finally, I create a table based on the matrix. 
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW3_Yuechen_Liu/table.png)

### Comment on any findings or limitations from the table and any ways you see to get a better understanding of how the various MeSH terms relate to each other.
Answer:
I think the table has limitations to see the relationship among MeSH terms. The table only shows the numbers, which is not straightforward to actually see the relation; while other ways, such as graphs, may be much more easier for researchers to understand how the various MeSH terms relate to each other.

## Exercise 3
### In particular, for each paper identified from exercise 1, compute the SPECTER embedding (a 768-dimensional vector). Keep track of which papers came from searching for Alzheimers, which came from searching for cancer. 
Answer:







## Exercise 4 
### Describe in words how you would parallelize this algorithm to work with two processes.
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

### How you would validate the results and the speedup?
Answer: For validate the result, we can use both merge sort and parallel merging sort to process one group of data, to test if they can have the same result. For the speedup, we can import time module in python, to get the working time of both algorithms. Normally, parallel merging sort will be faster. Parallel merging algorithm is very effective in processing large amounts of data, but the performance of traditional merging algorithm is very poor, because each time the merging process, the processor will be reduced by half, aggravating the data length processed by each processor. When merging to the end, only one processor processes all the data, which is very slow. As a result, the merge sort algorithm must be parallelize to achieve the maximum advantages.

## Exercise 5
### Do data exploration on the dataset you identified in exercise 4 in the last homework, and present a representative set of figures that gives insight into the data. Comment on the insights gained.
Answer:
#### 1. Which month does foodborne tend to occur the most? 
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW3_Yuechen_Liu/month.png)
As the graph showing, foodborne tends to occur most in May,June,and December.

#### 2. Has foodborne disease outbreaks gotten worse over the years? 
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW3_Yuechen_Liu/year_b.png)
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW3_Yuechen_Liu/year_l.png)
As the graph showing, the trend of foodborne illnesses has decreased overall since 1998. There are some significant drops, one is from 2004 - 2005, the other is from 2008-2009, but now seems to be steady around 800 - 900 cases per year. The data can be concluded that foodborne diseases are occurring less frequently by years.  

#### 3. Which state of the US do they appear the most frequently?
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW3_Yuechen_Liu/state.png)
Clearly, California and Florida have extreamly high rate of foodborne illnesses. The possible reasons could be related to their population rate during the years of 1998-2015. An exceptional circumstance would be the outbreak of Salmonella Infections linked to Peanut Butter: at least 36 people across 17 states have been affected by a salmonella outbreak between May 9 and July 27, 2008 - 2009. Majority of peanut butter was sent to California and Ohio, according to 
https://www.healthline.com/health-news/salmonella-outbreak-in-17-states-linked-to-italian-meats-what-to-know#:~:text=At%20least%2036%20people%20across,abdominal%20pain%2C%20and%20usually%20diarrhea.

### Are there any missing values in your data? (Whether the answer is yes or no, include in your answer the code you used to come to this conclusion.) If so, quantify. Do they appear to be MAR/MCAR/MNAR? Explain.
Answer:
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW3_Yuechen_Liu/missing_1.png)
![](https://github.com/YCKellyLiu/BIS634/blob/main/HW3_Yuechen_Liu/missing_2.png)

Clearly, the dataset has missing values. The data missing can be MNAR, for example, the restaruant is unwilling to report the location, food, ingredient and species; or the customers are not able to recall what food or ingredient caused the outbreaks. Besides, most foodborne infections go undiagnosed and unreported, because the those people don't see the doctors, or the doctor doesn’t made a specific diagnoses according to the CDC. The missing data also can be MAR, for example, the missing data of ingredient and species can be related to missing data of food; the missing data of fatalities can be related to missing data of hospitalizations. 

### Identify any data cleaning needs and write code to perform them. If the data does not need to be cleaned, explain how you reached this conclusion.
Answer:
Filter the dataset, drop the columns that are not related to the topic. Since the ratio of null fields in the column'Serotype/Genotype' and 'Ingredient' to the total number of rows exceeds 60%,which are proved not useful for the data anlysis. Therefore I choose to drop those two columns from my table.
Then, drop all null values.

![](https://github.com/YCKellyLiu/BIS634/blob/main/HW3_Yuechen_Liu/cleaning.png)
The data cleansing is finish, and the data does need to be cleaned, because the null values and excessive null columns are dropped.