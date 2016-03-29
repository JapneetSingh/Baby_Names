import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import mode
import os
import warnings
# Ignore any warnings in Output
warnings.filterwarnings("ignore")


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import mode
import os
import warnings
#Ignore warnings in Output
warnings.filterwarnings("ignore")
######################### Download , Extarct and Load Data

def download_extract_load(data_path,web_url):
    '''
    Downloads and extracts data and then calls read_in_babynames() function to load the data to a dataframe
    INPUT:
    data_path - path where data needs to be downlaoded. By default works in the current working directory
    web_url - url path to the babynames zipfile
    
    OUTPUT:
    
    data -  data frame with data loaded
    '''
    # creates path if it does not exist
    if not os.path.isdir(data_path): 
        os.makedirs(data_path)
    
    #Change directory to data path
    os.chdir(data_path)
    
    #Download Data if not already downloaded
    if not os.path.isfile("names.zip"):
        print "Downloading."
        import urllib
        urllib.urlretrieve(ssa_url, 'names.zip')
    
    else: print "Data already downloaded."
    print"Downloading complete."    
    
    if not os.path.isfile("AL.txt") or not os.path.isfile("WY.txt"):
        print "Extracting."
        import zipfile
        with zipfile.ZipFile('names.zip') as zf:
            #for member in zf.infolist():#Alternate method
                #zf.extract(member)
            zf.extractall() 
        
    else: print "Data already extracted."
    print"Extraction complete!!"
    
    data = read_in_babynames()
    return data



def read_in_babynames():
    """
    Reads in data from a given location
    INPUT:
    None
    
    OUTPUT:
    data- dataframe containing the contents of all the files
    
    """
    
    
    
    # List of all state(+DC = 51 in total) names to be used for reading in the files
    states = ['AL','AK','AZ','AR','CA','CO','CT','DC','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA',
    'ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA',
    'RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
    
    
    # Change working directory to the location of the files
    #os.chdir(path_to_files)
    
    # Initializing an empty dataframe to read in the data
    data = pd.DataFrame()
    counter = 0
    
    for state in states:
        counter+=1
        filename =  state +'.txt'
        #print filename as a check
        print "%d)%s loaded"%(counter,state)
        # The files dont have headers
        temp_data =  pd.read_csv(filename,sep = ",",header=None)
        data = data.append(temp_data)
    
    # Set column names
    data.columns = ["state","gender","year","name","state_frequency"]
    print "Data load is now complete. Do your thing!!"
    return data
    

############Insights
##################################### Impact of US International and National Policy on Birthrates in America



def insight1(data):



	# Total births by year
	q0 = data.groupby(['year']).sum().reset_index()


	plt.figure(figsize = (14,10))
	plt.plot(q0['year'], q0['state_frequency'])
	plt.title("Change in birthrates across the US over the last century")
	plt.xlabel("years")
	plt.ylabel("population")
	#plt.legend()
	plt.show()



	# Total births by year by gender

	q1 = data.groupby(['year','gender']).sum().reset_index()

	## getting male and female populations
	mpop = q1[q1['gender']== 'M']
	fpop= q1[q1['gender']== 'F']

	plt.figure(figsize = (14,10))
	plt.plot(mpop['year'], mpop['state_frequency'], label = "Male Population")
	plt.plot(mpop['year'], fpop['state_frequency'], label = "Female Population")
	plt.title("Change in birthrates across the US over the last centuary by Gender")
	plt.axvspan(1933,1936 , facecolor = 'y', alpha=0.5, label = " Male rates overtake female rates")
	plt.xlabel("years")
	plt.ylabel("population")
	plt.legend()
	plt.show()





	# Plotting World events

	plt.figure(figsize = (18,10)).add_axes([0.1, 0.1, 0.6, 0.75])
	plt.plot(mpop['year'], mpop['state_frequency'], label = "Male Population", c ="red")
	plt.plot(mpop['year'], fpop['state_frequency'], label = "Female Population", c ="black")
	plt.title("Possible Impact of US Foreign policy on birth rates in America ")
	plt.xlabel("years")
	plt.ylabel("Number of births")

	plt.axvspan(1917, 1919, facecolor='b', alpha=0.5, label ="WW1(1917-1919)")
	plt.axvspan(1929, 1939, facecolor='g', alpha=0.5, label ="Great Depression(1929-1939)")
	plt.axvspan(1941, 1945, facecolor='y', alpha=0.5, label ="WW2(1941-1945)")
	plt.axvspan(1950, 1953, facecolor='r', alpha=0.5, label ="Korean War(1950-1953)")
	plt.axvspan(1959, 1979, facecolor='brown', alpha=0.5, label ="Vietnam War(1959-1979)")
	plt.axvspan(1987, 1988, facecolor='teal', alpha=0.5, label ="Tanker War(1987-1988)")
	plt.axvspan(1989, 1990, facecolor='orchid', alpha=0.5, label ="Panama Invasion(1989-1990)")
	plt.axvspan(1990, 1991, facecolor='cyan', alpha=0.5, label ="Persian Gulf War(1990-1991)")
	#plt.axvspan(1997, 1999, facecolor='lime', alpha=0.5, label ="Global market crash(1997-1999)")
	plt.axvspan(2001, 2014, facecolor='gray', alpha=0.5, label ="Afganistan War(2001-)")
	plt.axvspan(2000, 2003, facecolor='black', alpha=0.5, label ="Dotcom Bubble")
	plt.axvspan(2003, 2011, facecolor='m', alpha=0.5, label ="Iraq War(2003-2011)")

	plt.axvspan(2007, 2012, facecolor='yellow', alpha=0.5, label ="The Great Recession(2007-2012)")

	plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0. )

	
	plt.show()




############################################## US Child Naming patterns 

def insight2(data):

	# Creating a column with the first letter 
	data['fletter'] = map(lambda x: x[0],data['name'])

	#################### Finding the total frequecies by given letters and plotting
	letter = data.groupby(['fletter']).sum().reset_index().drop('year',1)
	print " The following is the list of alphabets from most common to least common: \n ",\
						letter.sort_values("state_frequency",ascending = False)


	plt.figure(figsize = (14,10))
	plt.bar(letter.index,letter.iloc[:,1])
	plt.xticks(range(26),letter.iloc[:,0],ha='center', rotation=0)
	plt.xlim((0,26))
	plt.title("Number of names starting with given alphabets over the last century(1910-2014")
	plt.xlabel("Alphabets")
	plt.ylabel("Number of names starting with given alphabet(in ten millions)")
	plt.show()					


	#################Top 5 alphbets for each gender. Plotting them			

	letter = data.groupby(['gender','fletter']).sum().reset_index().drop('year',1)

	males = letter[letter['gender'] == 'M'].reset_index(drop = True)
	females = letter[letter['gender'] == 'F'].reset_index(drop = True)


	plt.figure(figsize = (14,10))
	width =.25
	plt.bar(males.index,males.iloc[:,2],width,label = "Males", facecolor='y')


	plt.bar(females.index+width,females.iloc[:,2],width, facecolor = "g", label = "Females")
	plt.xticks(range(26),males.iloc[:,1],ha='center', rotation=0)
	plt.xlim((0,26))
	plt.title("Number of names starting with given alphabets")
	plt.xlabel("Alphabets")
	plt.ylabel("Number of names starting with given alphabet(in ten millions)")
	plt.legend()
	plt.show()	




    ################### Decade wise analysis of most common letters	

	# Creating a column for decade of the century
	bins = range(1900,2030, 10)
	labels = ["1900's","1910's","1920's","1930's","1940's","1950's","1960's","1970's","1980's","1990's","2000's","2010's"]
	data['decade'] = pd.cut(data['year'],bins,labels=labels)


	decade_wise = data.groupby(['decade','fletter']).sum().reset_index().drop('year',1)
	let_by_dec = pd.DataFrame()
	for label in labels:
		# FOr each decade get the mose common alphabet
		
		df = decade_wise[(decade_wise['decade']==label)]
		
		let_by_dec = let_by_dec.append(df.sort_values('state_frequency',ascending = False)[:1])

	print "The following is the result of decade by decade analysis of the most common letters: \n"	
	print let_by_dec


    ################## Decade wise analysis by gender 

	# Groupby by decade letter and gender and count the number of names by those groups
	temp = data.groupby(['decade','fletter','gender']).sum().reset_index().drop('year',1)

	gender = ['M','F']

	# Empty data frames to record male and female top letters
	dec_m = pd.DataFrame()
	dec_f =pd.DataFrame()


	for label in labels:
	    # Subset by decade
	    df = temp[(temp['decade']==label)]
	    
	    for gen in gender:
	        #Subset by gender on data of above decade and sort the values
	        df = df[(df['gender']==gen)]
	        df.sort_values(['state_frequency'],ascending = False, inplace = True)
	        
	        # Get list of male and female top letter for wach decade
	        if gen  == 'M':
	            dec_m =  dec_m.append(df[:1])
	        else:
	            dec_f = dec_f.append(df[:1])


	print " For females the top names of each decade are \n:", dec_f           

	print " \n For males the top names of each decade are \n:", dec_m   





	########################## Unique name analysis for boys

	# Subseting the data by first letter J and sex as Male
	test_m = data[(data['fletter'] == 'J') & (data['gender'] == 'M')]
	
	#Group the data by name and decade which gives you a table containing 
	#occurances of each name starting with J for every decade
	test_m = test_m.groupby(['name',"decade"]).sum().reset_index()
	
	
	# Now that we have all the names starting with J for each decade we do a groupby for decade to count the number of unique names per decade
	# Some Null values will occur for every decade since not all names occur in all decades. The count will ignore them
	test_m1 = test_m.groupby(['decade']).count().reset_index()
	
	# Plotting number of unique names by decade
	plt.figure(figsize = (14,10))
	plt.bar(range(12),test_m1.state_frequency)
	plt.xticks(range(12),test_m1.decade,rotation =45)
	plt.xlabel('Decades')
	plt.ylabel('Number of unique names starting from J')
	plt.title("Number of unqiue names starting from J over the last century")
	plt.show()




if __name__ =="__main__":


	data_path = "user_data" 
	ssa_url = 'http://www.ssa.gov/oact/babynames/state/namesbystate.zip'


	data = download_extract_load(data_path,ssa_url) 


	# Which insight to execute
	choice = int(raw_input("Enter 1 for Insight 1 \n Enter 2 for Insight2  \n Enter 0 for running both together:\n"))
	print "You chose ",choice
	
	if choice == 1 :
		insight1(data)
	
	elif choice == 2 :
		insight2(data)
	
	elif choice == 0:
		print "Now starting US policy analysis"
		insight1(data)
		print "Now starting Naming Pattern analysis"
		insight2(data)
	
	else:
		print"Invalid choice"	
