# BIS634
## Question1 
In this question, I use Python closures to create nested functions. The outter function defines the normal temperature, and the inner function return if the test temperature is normal. Test results show that the function is successful.

## Question 2
Columns: name, age, weight, eyecolor
Total 152,361 rows

The role of number of bins: I divide ages into 50 groups(bins),one bin means two years, to better see the pattern. The pattern of the distribution of ages is right skew.

Relationship: When age <20, the relationship between age and weight is proportional increaseing, which with the increasing of age, the weight also increases. When age>20, the relationship between age and weight is steady, with few increases or decreases. 

Name of the outlier: Anthony Freeman. I got this result by filtering age between 40 and 45, weight between 20 and 25, and obviously based on the graph, there is only one person in this range. 

## Question 3
Citation: Track Coronavirus Cases in Places Important to You
Track Coronavirus Cases in Places Important to You. (2020). Nytimes.com. Retrieved 14 September 2021, from https://www.nytimes.com/interactive/2021/us/covid-cases-deaths-tracker.html

Download date: 09/08/2021

For the first function, case_date, I make the plot of the running total. I use three states, called my_state, to test the function. 

For the function, highest_new_cases, I use "Washington" to test. The result is '2021-09-07'.

For the function, highest_number_cases_first, I use "Washington" and "Illinois" to test the function. Washington had its highest number of cases about 298 days before Illinois.

## Question 4
4a
Function: define_groups(10,8)
Result: [True, True, True, True, True, True, True, True, False, False]

4b
In the function sample, I define 1 = Head, 2 = Tail, num1= The first flip, num2 = The second flip
Function: sample(10,3,8)
Result: [True, True, False, True, False, False, False, False]

4c
In function population_estimated_users, I first calculate p, and use p to measure the estimated drug users in the population.
Function:population_estimated_users(1000,100,20)
Result:1100.0

4d
Function: population_estimated_users(1000,100,50)
Result: 820.0000000000001, which means 820

4e
I run 1000 times. because it is not huge enough to crush my computer, but also I can get enough data to get the sense of distribution. 
The overall result is an approximately normal distribution. 

4f
The overall result is normal distribution, the bars are more compact, compared to "1000 people, 100 of whom are drug users and we do a survey using this protocol that samples 50 people from the total population."

4g
The overall result is normal distribution, but the bars are more loosing and fewer compared with "1000 people, 100 of whom are drug users and we do a survey using this protocol that samples 50 people from the total population."



