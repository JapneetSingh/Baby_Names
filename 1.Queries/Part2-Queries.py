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
    
###########################################Queries


########################Query 3 
def find_common_names(year, data):
    
    '''
    Returns common names for males and females for a given year
    
    INPUT:
    year - year for which this needs doing
    data - data
    
    OUTPUT:
    names -  set with unisex names
    '''
    df = data[data['year'] == year]
    m_names = set(df[df['gender']=='M']['name'])
    f_names = set(df[df['gender']=='F']['name'])
    
    common_names =  m_names.intersection(f_names)
    return common_names


def gender_ambi(data, year):
    '''
    function to give the most data ambiguous names
    
    INPUT:
    data -  your data
    year -  year for which this operation names to be performed
    OUTPUT:
     
    list_of_ga_names - list of most gender ambiguous names
    
     
    '''
    
    # Get the set of gender ambiguous names
    ga_names = find_common_names(year,data)
    
    # Subset data to get a dataframe with gender ambiguous names for that year.
    df = data[data['year'] == year]
    df_ga = df[(df['name'].isin(ga_names))]
    
    # Calculating the groupby and sum. Reset index ensures we can use the groupby indexes as columns 
    #and access them easily for future funtions. It does the following 3 things
    #1) groups by given columns and removes years as a possible column by choosing stat_frequency 
    #2) then sums the groupby values
    #3) Resets index 
    df = df_ga.groupby(['name','gender'])['state_frequency'].sum().reset_index()
    
    # We calculate a second dataframe to count the total number of occurances for each name. Will be used to calculate
    # the percent male/female for each name
    tot_names = df_ga.groupby(['name']).sum().reset_index()
    
    
    # Merging the two using left join so I have the values aligned to calcuate the percent
    df_vals = pd.merge(df,tot_names,on='name',how='left')
    
    # Removing all the rows with gender = "F" as not needed going forward based on gender ambiguity formula
    df_final = df_vals[df_vals['gender'] == "M"]
    
    # Calculating the percent of male names and then the final difference using the formulae described above
    df_final['per_m'] = df_final['state_frequency_x']/df_final['state_frequency_y']
    df_final['diff'] = abs(2*df_final['per_m']-1)
    
    # Sort the final data frame by 
    ga = df_final.sort_values(by = ["diff"]).reset_index(True)
    min_diff = ga['diff'].min()
    
    # deriving the final list of names by finding the minimum difference
    solns = ga[ga['diff'] == min_diff]
    list_of_ga_names = solns['name']
    
    return list_of_ga_names



########################################### Query 4 and Query 5

def inc_dec(year1,year2,data, inc = True, consider_all=True):
    '''
    In this case we consider also the names that did not exist in 1980,2014
    
    INPUT:
    
    year1,year2 - Years we wish to compare. 
    data -  your data
    inc - Boolen to decide whether to calculate increase or decrease. By default we calculate the increase
    consider_all- boolean consider all the names including the ones that didnt exist in 1980
    
    OUTPUT:
    
    soln - dataframe containing with max inc/dec and the value of inc/dec
    
    '''
    # Subset the database for specified years
    df1 = data[data['year'] == year1].reset_index(True)
    df2 = data[data['year'] == year2].reset_index(True)
    
    # Calculating the total appearances of each name for both the years
    names_y1 = df1.groupby(['name']).sum()['state_frequency'].reset_index(True)
    names_y2 = df2.groupby(['name']).sum()['state_frequency'].reset_index(True)

    # COmbining the two to form a master dataframe with 3 columns:
    #1) name
    #2) y1_freq 
    #3) y2_freq

    df = pd.merge(names_y1,names_y2,how = 'outer',on= 'name')
    df.columns = ['name','y1_freq','y2_freq']
    

    
    # Fill any null values with 0
    df.fillna(0,inplace = True)
    
    # Adding Laplacian smooting. Because if the increase is from 0 we get inf percent. So increasing all occurances by 1
    df['y1_freq'] +=1
    df['y2_freq'] +=1
    
    #Subsetting the data based on whether we're calculating increase
    if inc:
        # Get a subset where y2_freq (2014)>y1_freq(1980)
        
        dfinc = df[df['y2_freq']>df['y1_freq']]
        dfinc['diff'] = (dfinc['y2_freq'] - dfinc['y1_freq'])
        dfinc['perc'] = dfinc['diff'] /  dfinc['y1_freq']
        print 
        # Sort the final data frame by 
        dfinc = dfinc.sort_values(by = ["perc"] , ascending = False).reset_index(True)
        
        if not consider_all:
        # If we only wish to consider the names that existed in 1980. Since their value has been set to 1
            dfinc =  dfinc[dfinc['y1_freq'] > 1]
        
        max_inc = dfinc['perc'].max()
        
        soln =dfinc[dfinc["perc"] == max_inc][["name","perc"]]        
      
    #Subsetting the data based on whether we're calculating decrease
    else:     
        # Get a subset where y1_freq (1980)>y2_freq(2014)
        dfdec = df[df['y1_freq']>df['y2_freq']]
        dfdec['diff'] = (dfdec['y1_freq'] - dfdec['y2_freq'])
        dfdec['perc'] = dfdec['diff'] /  dfdec['y1_freq']
        
        # Sort the final data frame by 
        dfdec = dfdec.sort_values(by = ["perc"] , ascending = False).reset_index(True)
        max_dec = dfdec['perc'].max()
        soln =dfdec[dfdec["perc"] == max_dec][["name","perc"]]
        
    
    return soln





##############################################Execute the code
def main(data_path,ssa_url):
		
	# Get the data:
	data = download_extract_load(data_path,ssa_url)   

	#Query 2:
	print " Result to Query 2: The 10 most common name in America are \n: \
	%s"	%(data.groupby(['gender','name']).sum().sort_values(by = ["state_frequency"],\
	ascending = False))[:10]

	print "The most common name here is James"


	# Query 3
	ga_2013 = gender_ambi(data,2013)
	ga_1945 = gender_ambi(data,1945)
	
	print "The most gender ambiguous name in 2013 are:>>>>>>>>>>>>>>>>\n", ga_2013
	print "The most gender ambiguous name in 1945 are:>>>>>>>>>>>>>>>>\n", ga_1945

	#Query 4 
	
	biggest_dec = inc_dec(1980,2014,data, inc= False, consider_all=False)
	biggest_inc = inc_dec(1980,2014,data, inc = True, consider_all=False)	
	
	biggest_dec_all = inc_dec(1980,2014,data, inc= False, consider_all=True)
	biggest_inc_all = inc_dec(1980,2014,data, inc = True, consider_all= True)



	print "Largest decrease not considering all (only the names that existed in 1980)", biggest_dec

	print "Largest increase not considering all (only the names that existed in 1980)", biggest_inc

	print "Largest decrease considering all (including the names that did not exist in 1980)", biggest_dec_all

	print "Largest increase considering all (including the names that did not exist in 1980)", biggest_inc_all



if __name__ == "__main__":
  	
	# Path on your computer where the process should happen. 
	# Else it occurs in current working directory
  	data_path = "user_data" 
	ssa_url = 'http://www.ssa.gov/oact/babynames/state/namesbystate.zip'
	main(data_path,	ssa_url)
