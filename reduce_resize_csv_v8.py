# -*- coding: utf-8 -*-

"""
2021.12.02
python script to make reduced-size .csv files:

This requires pandas to be installed in pipenv shell.

This will make fractional-sized reductions in the .csv 
equal to the numbers you set as:
1. number_of_reductions ...e.g. '6' for six files
2. fraction_of_reduction ...e.g. '2' for 1/2
"""

import pandas as pd
import os

# flag
file_ok = False

# check to see if given file name works, if not ask again
while file_ok is False:

    # try the file name
    your_file_name = input("enter your_file_name...deathstarplans.cvs\n")
        
    # check if file exists: if so or if not, set file_ok flag
    file_ok = os.path.isfile( your_file_name )
        
    if file_ok is False:
        print("That file name did not work...please try again: \n")

number_of_reductions = int( input("enter number_of_reductions...e.g. '6' for six files\n") )

fraction_of_reduction = int( input("enter fraction_of_reduction...e.g. '2' for 1/2\n") )

df = pd.read_csv( your_file_name )

df.head()

df.shape

file_counter = 1

def reduce_csv(df, file_counter):
    print(f"Starting on file {file_counter}...")

    # inspection shape
    print("Starting shape:", df.shape)

    # pick where to start and stop
    # from fraction through, to the end
    from_here = int( df.shape[0] / fraction_of_reduction )
    to_here = df.shape[0]

    print("Working...")

    # drop rows from_here to_here 
    df = df.drop(df.index[from_here:to_here])

    print("Still Working to make smaller .csv ...")
    
    # file name
    file_name = f'smaller_{file_counter}.csv'
    
    # make csv
    df.to_csv( file_name, index=False, header=True ) 
    
    print("Made: ", file_name)

    # increment file counter
    file_counter += 1

    # inspection shape
    print("Ending shape: ", df.shape)

    print("All Done!")
    
    return df, file_counter

# iterate and make the requested number of files:
for i in range(number_of_reductions):
    # return both df and file_counter so changes are retained
    df, file_counter = reduce_csv(df, file_counter)

del df

