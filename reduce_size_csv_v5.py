# -*- coding: utf-8 -*-

## This requires pandas and jupyter to be installed in pipenv shell

## This will make halfed sized reductions in the .csv 
## equal to the number you set as number_of_reductions

import pandas as pd

your_file_name = input("enter your file name...")

number_of_reductions = input("enter number_of_reductions...e.g. 6")

df = pd.read_csv( your_file_name )

df.head()

df.shape

file_counter = 1

def reduce_csv(df, file_counter):
    print("Starting...")

    # inspection shape
    print("Starting shape:", df.shape)

    # pick where to start and stop
    # from halfway through, to the end
    from_here = int( df.shape[0] / 2 )
    to_here = df.shape[0]

    print("Working...")

    # drop rows from_here to_here 
    df = df.drop(df.index[from_here:to_here])

    print("Still Working...")
    
    # file name
    file_name = f'smaller_{file_counter}.csv'
    
    # make csv
    df.to_csv( file_name, index=False, header=True ) 
    
    print("Made: ", file_name)

    # increment file counter
    file_counter += 1

    # inspection shape
    print("Ending shape:", df.shape)

    print("All Done!")
    
    return df, file_counter

for i in range(number_of_reductions):
    df, file_counter = reduce_csv(df, file_counter)

del df
