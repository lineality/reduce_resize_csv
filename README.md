# reduce_resize_csv
if you need a half size (or quarter etc) and reduced content csv for testing

### To Run the Notebook
```
pipenv shell
pipenv install pandas
pipenv install jupyter
jupyter notebook
```

### To run the script:
```
pipenv shell
pipenv install pandas
python3 reduce_size_csv_v5.py
```


Sometimes you need to work on a .csv file but the file is very large (e.g. 1.6 gigs) and is cumbersome for some tasks where you do not need the whole file.

With this tool you can make smaller versions of the .csv file.

A python script version and a python notebook version are both available.


## .py
The python script can be run in a terminal and will ask for:
1. file name
2. how many smaller files you want
3. the size fraction of each reduction ("2" for half, "4" for quarter, etc.)
