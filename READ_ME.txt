                      US Bike Share Data programe.

-The program is a terminal based interface with the user to ask him some questions
 and get inputs from the user to then print a specitic set of statistics based on 
 the user input criteria.

-The program depends on the pandas, numpy, and time modules.

-All user inputs are validated for errors and exceptions.

-The flow of the programe :
1- ask user to choose one of the 3 citys (chicago - new york city- washington) to get stats for.
2- ask the user if he wants to filter data by month or use all.
3- ask the user if he wants to filter data by a day of the week all use all.
4- the we start filtring the data from the .csv file of the choosen city by importing it into 
   a pandas data frame and apply filters.
5- after we have the correct filtered data we start to get the required statistics from the data 
   using different functions that print the results to user.
6- after all statistics are printed we ask the user if he/she wants to see raw data of the choosen 
   city file and print the data 5 rows at a time till user specify else.
7- finally the user is asked if he wants to exit the programe or chose another city toi get its stats.


-A list of sites and resources that was helpful in solving tasks in the project :
1- https://stackoverflow.com/
2- https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html
3- https://www.w3schools.com/python/default.asp
4- https://cmdlinetips.com/category/python/
5- https://docs.python.org/3/tutorial/index.html
7- the udacity course python practice examples.