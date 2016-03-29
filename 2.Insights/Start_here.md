#Part 2: Insights

When you proceed by running the python file you will be asked for input
to decide which insight code to run. Please follow the instructions
to get the appropriate choice

# Insight 1 :Impact of US International and National Policy on Birthrates in America

When given a data set my approach is always to see what questions can I ask that
the dataset may answer.While we have a distorted dataset(only the names with
frequency greater than 5 in a state ) , it seemed like a  good place to start
to get an idea of the birth rates

I decided to start by asking the following 2 questions:
* How have the US number of birthrates changed over the last century
from 1910 onwards
*  Is there a difference in the birth rates of males and females
over the century


I started by plotting out the **total births per year(Image1)** and followed it up
with **total births per year by gender(Image2)**

The non linear trend of the birth rates came as a huge surprise to me since
one would believe that with advancements in technology and medicine
the birthrates over the years would go up. Yet we had 2 big troughs
in the birthrates , one in the 30's and the other in the 60's and 70's.
Interestingly these trends were echoed in the total births by gender graph
almost identically.
The one interesting observation in the birthrates by gender was in the 1930's
which was the first time that the male births exceeded the female births.
The male births have continued to higher than their counterparts since the
1930's


As someone who was unfamiliar with American history, I decided to research further.
The two major important events in US history seemed to be coincided with
the the mentioned periods :
 1. Great Depression for 1930's:
 The decline of births during the great depression made sense since with majority
 of people struggling to feed their families would have decided to postpone
 the family life.
 This may also explain the male births overtaking the female births. With males
 considered the primary breadwinners in the society at the given time, it can
 be argued that families had a disposition towards the male child.

 It would be interesting if we could get data about infanticides(if any) rates
 during the great depression which would add another layer to this discussion



 2. US- Vietnam War for the 1960's and 1970's
With over 500,000 American troops deployed to Vietnam at the peak of the war,
the second trough actually coincided with this event in US history.[1]


These  interesting discoveries got me thinking that can I find events in US
history which could coincide with the other minor troughs in the birthrates.
I started researching major events in US history and surely enough I found
major world National and International events that coincided with falling birth
rates:

1. World War 1(1917-1919)
2. Great Depression(1929-1939)
3. World War 2(1941-1945)
4. Korean War(1950-1953)
5. Vietnam War(1959-1979)
6. Tanker War(1987-1988)
7. Panama Invasion(1989-1990)
8. Persian Gulf Wars(1990-1991)
9. Dot com bubble(2000-2003)
9. Afghanistan War(2001-present)
10. Iraq War(2003-2011)
11. The Great Recession(2007-2013)

**See Image 3**


The years 2000-2015 have been some of the  most turbulent years in recent history
with a variety of events, from 2000's Dotcom Boom, to The Iraq and Afghanistan
wars and the Great Recession. So it is no wonder to learn than that as of 2003-2011
the US birth rates are the lowest they have been since 1920's( the earliest years
with reliable data available)  with a decline of almost 8%[3]


There seems to be a definite correlation between the US National and International
policy on birth rates. But since the data is distorted I would refrain from making any
generalizations at this point.



### Future Work
1. As mentioned above , I would like to explore the cause for the drop in female
births during the recession. It would be really interesting to find a reliable
datasource about abortions, and female infanticide if any from the 1930's.

2. I could not find any particular events in mid to late 1990's that would relate
to a small drop in the birth rates. There was a recession in Asian in mid 1990's
but I could not find any data/articles to support sufficient relation between
the two events.




# References
[1]http://www.digitalhistory.uh.edu/active_learning/explorations/vietnam/escalate_graph1.cfm
[2]https://en.wikipedia.org/wiki/List_of_the_lengths_of_American_participation_in_major_wars
[3]http://business.time.com/2012/12/04/birth-rate-plunges-during-recession/



# Insight 2: US child naming pattern

After dealing with the count I decided to explore the names by themselves.
In Asian cultures the the letters that names begin with are
derived on religious grounds and vary from day to day. Your name may essentially
be different depending on which day your parents decide to perform the
naming rituals.

In contrast names in America are decided based on the parent's wishes which allows
for the possibility of predisposition towards certain alphabets in the English
Language. Therefor I was curious to observe if there was any sort of preference
for certain letters in American names.
Therefore I started out by asking:

*  Which letters do majority of US names start with?

The numbers suggested a clear pattern. There was 1 clear winners:
**J** was the most most common alphabet which beat M the second most common by
nearly 12 million entries. The following are the top 5 naming letters
over the last century:
```
# Most common alphabets
J	    40,437,220
M	    28,267,690
A	    23,817,686
C 	  22,045,102
D	    21,527,509
```
The following were the least common:
```
X	    170,509
Q	    158,147
U	    80,897
```

So Americans clearly have a predisposition towards letter 'J'.
This did not surprise me because we had earlier seen three names in 10 most
common American names in top 10 in the queries portion of this exercise.
**See plot 2.1**
So now onto an obvious follow up questions:


**1) But was this true for both Genders ?**
**2) Was J really the most common alphabet for every year?**


1. But was this true for both Genders ?

On further research we got the folloing top 5 alphabets for male and female

```
gender firstletter  state_frequency
M       J           27,239,116
M       R           15,208,120
M       D           13,068,742
M       M           11,584,336
M       C           11,245,004

gender firstletter  state_frequency
F       M           16,683,354
F       A           13,744,632
F       J           13,198,104
F       S           11,758,497
F       C           10,800,098
```

So the most popular letter for naming males in the past century was *J*
and for females was *M*
Another interseting observation here was while J is the clear winner for boys,
girl's names are more evenly divided over a variety of different alphabets(M,A,J etc.)
**See plot 2.2**


2. Was J really the most common alphabet for every year?

To address the first question I proceeded to do a **decade by decade analysis.**
I broke the years starting from 1910 into 12 bins:
```
labels = ["1900's","1910's","1920's","1930's","1940's","1950's","1960's",/
"1970's","1980's","1990's","2000's","2010's"]
```        
Upon running my query I got the following results        

```
1900's	M
1910's	M
1920's	J
1930's	J
1940's	J
1950's	J
1960's	J
1970's	J
1980's	J
1990's	J
2000's	A
2010's	A
```
So it seems letter 'M' was the most popular until the early 1920's. Its popularity
was soon replaced by "J" which was dominant until early 2000's
followed by 'A' becoming the most popular since 2 early 2000's

This brought me to the next question:

#### * **Would the pattern be different for Males and females over these decades?**

So I went back into the data to dig this up. No we are looking to
find for every decade for both the genders which is the most used alphabet
The results were most interesting.

Here are the results:
```
Males:
decade	fletter
1900's	    J
1910's    	J
1920's    	J
1930's    	J
1940's    	J
1950's    	J
1960's    	J
1970's	    J
1980's    	J
1990's    	J
2000's    	J
2010's    	J



Females:
decade	fletter
1900's	   M
1910's	   M
1920's	   M
1930's	   M
1940's	   J
1950's	   D
1960's	   S
1970's	   J
1980's	   A
1990's	   A
2000's	   A
2010's	   A
```
While females see different names dominate in different decades with M until 1930's
and A since the 1980's,male names over the last 12 decades have been dominated by
letter J.

Letter J it seems is really popular for boys

This brings me to my final follow up question:
#### * **Although J has been the dominant letter over the decades has the number
of unique names starting from J changed over this time**

This time we find a very interesting trend. The number of unique names starting
with J have been increasing over the century and peaking in the 80's ,90's and early
2000's as shown below and in the **Image 2.3**


```
decade	 No_Of_Unique_names
1900's	   45
1910's	   113
1920's	   131
1930's	   131
1940's	   145
1950's	   145
1960's	   183
1970's	   318
1980's     523
1990's     706
2000's	   843
2010's  	 609

```

The only possible reason in my  mind for name increases could possibly
be immigration. People from different cultures bring along their names
which I believe may have added to the name diversity in the USA over the
last few years.

I went out to look for immigration patterns and found this figure
http://www.trivisonno.com/wp-content/uploads/Immigration-Annual-USA.jpgIt show
which seems to coincide with the maximum distinct names starting with letter J.
**See figure 2.3 and 2.4[1] together.**


A this point it would be really interesting to get our hands on the missing
data(names with < 5 occurances per state). It might be interesting to
see how these unique names now are different from the unique names in
early half of 20th century. They may also carry hints about where the immigrants
are coming from.




# Conclusions and Summary
1. It seems very likely that American naming conventions have a disposition
towards certain letters for naming the children.

J has been the most popular letter over the course of last century when
combined data for boys and girls is looked over.

When split into a decade by decade analysis we find that the letter A has
had the most names since the turn of 21st century, although J was dominant
from 1920's to 1990's



For every decade over the last 105 years, names starting from letter J have been
preferred for boys, with J having maximum names in every decade.

There is more variety in girl names with letter M dominating until 1940's
while letter A dominating since the 1980's


2. We looked at the number of unique names starting from top letter J over
the course of past century and we discover a significant increase in the 80's and
90's this seems consistent with the immigration patterns  



# Future Work and additional insights
I could not complete the work due to time limitations but I did come across
some more insights that seem worth exploring further

* Even though A is the third most used alphabet including both genders, of the
top 50 names we only have 2 entires for A, Anthony at 21 and at Andrew at 23.
I would like to further explore the distribution of each of the top 10 letters
over the top 1000 names

* I would further like to explore the number of unique names per girls for every
decade for the dominant alphabet.

# References
[1] http://www.trivisonno.com/wp-content/uploads/Immigration-Annual-USA.jpg
