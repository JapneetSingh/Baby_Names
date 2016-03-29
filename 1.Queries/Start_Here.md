
I would recommend looking at the source code in ipython notebook where it details every step taken
A python file has also been provided for you to execute.


### 1.  Please describe the format of the data files. Can you identify any limitations or distortions of the data?

The data is stored in tall format in ***comma seperated text files***, one for each state.
Each row has five values:
* **state**: the 2-letter code of the state.
* **gender**: one letter, M|F.
* **year**: the year of birth for this record, in 4-digit format.
* **name**: the name.
* **state_frequency**: an integer for the number of times this name occurred in that state in that year.


In the description provided by SSA, it is mentioned that only names which occur 5 or more times in an year are included
which introduces bias into the data. Hence this data is not a comprehensive representation of all baby names in America.
This bias also limits our ability to get an idea of population since we have no idea how many babies with names that
occur less than 5 times exist in each state. I would therefore be careful about any generalizations from this data.





### 2.  What is the most popular name of all time? (Of either gender.)

##### The most popular name by itself is ***James***
We can see here that the most popular name for :

Women is **Mary**

Men is **James**


### 3.  What is the most gender ambiguous name in 2013? 1945?

#### Define Gender ambiguity:
At this point we need to devise a metric to measure gender-ambiguity
We look at it as the *name that has the similar percent as males as females asssociated with it:
* per_f = percentage of times the name appears as female
* per_m = percentage of times the name appears as male

**diff = per_f-per_m ~ 0**

Since per_f = 1- per_m  so **difference** can be reworked as ***abs(2*perf_m-1)***.

We do the reworking because it prevents us from having to use and extra self join in the future
when we need to calculate the difference


**Maxie** is the most gender ambiguous name for 1945 while
for 2013 we have a tie between **Nikita, Devine, Cree, Sonam and Arlin**




### 4.  Of the names represented in the data, find the name that has had the largest percentage increase in popularity since 1980. Largest decrease?

### 5.  Can you identify names that may have had an even larger increase or decrease in popularity?


* Biggest increase considering only the names that existed in 1980 ***Colton***

* Biggest decrease for both considering only the names that existed in 1980 and considering all is  ***Tonya***
* Biggest increasein popularity considering all the names ***Jayden***

* Biggest increase/decrease in popularity considering all the names ***Jayden***
