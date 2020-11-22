import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# glopal Tuples of monthes and days names to be used later
Months = ("january", "february", "march", "april", "may", "june")
Days = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")

# Global Flages
Month_filter_flage = False
Day_filter_flage = False

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        try :
            inputed_city = input("please type a city name to analyze its data from the following (chicago, new york city, washington): ").lower()
            if inputed_city == "chicago" or inputed_city == "new york city" or inputed_city == "washington" :
                print ("good input")
                break
            else :
                print ("Wrong city name please try again....")
        except Exception as e :
            print ("Exception is :{}".format(e))

    # get user input for month (all, january, february, ... , june)
    months_list = ["all", "january", "february", "march", "april", "may", "june"]
    while True :
        try :
            inputed_month = input("please type the name of the month to filter data by, or 'all' to apply no month filter: ").lower()
            if inputed_month in months_list :
                print ("good input")
                break
            else :
                print ("Wrong month name please input a month from the first six months of the year as below :\n{}".format('["all", "january", "february", "march", "april", "may", "june"]'))
        except Exception as e :
            print ("error is :{}".format(e))


    # get user input for day of week (all, monday, tuesday, ... sunday)
    days_list = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    while True :
        try :
            inputed_day = input("please type the name of the day to filter data by, or 'all' to apply no day filter: ").lower()
            if inputed_day in days_list :
                print ("good input")
                break
            else :
                print ("Wrong day name please input a day of the week, choose one of below :\n{}".format('["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]'))
        except Exception as e :
            print ("error is :{}".format(e))

    print('-'*40)
    return inputed_city, inputed_month, inputed_day

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #declearing global flages to apply changes
    global Month_filter_flage, Day_filter_flage
    
    #load all the desired city data
    city_data_df = pd.read_csv (CITY_DATA[city])
    
    #filtering all data by:
    
    # 1-converting the ride [Start Time] column of Data frame into Date Time object from a string object.
    city_data_df["Start Time"]= pd.to_datetime(city_data_df["Start Time"])
    
    # 2-creating new columns for [month] and [day] from [Start Time] column
    city_data_df["Month"]= city_data_df["Start Time"].dt.month
    city_data_df["Day"]= city_data_df["Start Time"].dt.weekday_name
    
    # 3-filtring data by month (if user desired)
    if month in Months :
        Month_filter_flage = True
        month= Months.index(month) + 1                              # got the month int number to filter the [Month] column with
        city_data_df= city_data_df[city_data_df["Month"] == month]  # filtring the data frame rows my the month number 
    else :
        Month_filter_flage = False
        
    # 4-filtring data by day (if user desired)
    if day in Days :
        Day_filter_flage = True
        city_data_df= city_data_df[city_data_df["Day"] == day.title()]  #filtring the data frame by day name {remember [data_frame.dt.weekday_name] returnes capital first letter of the day name}
    else :
        Day_filter_flage = False
        
    # 5-Return filtered data frame for further processing
    return city_data_df

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def time_stats(df, month, day):
    """
    Displays statistics on the most frequent times of travel.
    
    Args:
        (df ) Pandas DataFrame containing city data filtered as per user inputs
        (str) month - name of the month inputed by the user
        (str) day - name of the day of week inputed by the user
    Returns:
        no return
    """
    # printing a title 
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if Month_filter_flage == True : # if we filter by month we do not need any computation to get common month
        print("most common month is: {}".format(month.title()))
    else :
        # get most common month using mood method
        most_common_month = df["Month"].mode()[0]
        print("most common month is: {}".format(Months[most_common_month-1].title()))
        
    # display the most common day of week
    if Day_filter_flage == True : # if we filter by month we do not need any computation to get common day
        print("most common day is: {}".format(day.title()))
    else :
        # get most common day using mood method
        most_common_day = df["Day"].mode()[0]
        print("most common day is: {}".format(most_common_day))
        
    # get most common hour using mood method
    df["start_hour"]= df["Start Time"].dt.hour      # creating new column for start hour only to filter data with
    most_common_hour = df["start_hour"].mode()[0]
    print("most common start hour is: {}".format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    
    Args:
        (df ) Pandas DataFrame containing city data filtered as per user inputs
    Returns:
        no return    
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts()[0]
    print("most common start station is: {}".format(most_common_start_station))

    # display most commonly used end station
    most_common_end_station = df["End Station"].value_counts()[0]
    print("most common end station is: {}".format(most_common_end_station))

    # display most frequent trip
    df["trip"]= df["Start Station"] + ":" + df["End Station"]    # creating new column for Trip to get trip stats
    most_common_trip = df["trip"].value_counts()[0]
    #print("most common trip station is: [{}] ----> [{}]".format(most_common_trip.split(":")[0], most_common_trip.split(":")[1]))
    #print(df['trip'].value_counts()) # validate answer
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
       #print("filtered data frame is :\n", df.head()) # debuging line
       # trip_duration_stats(df)
       # user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
            
if __name__ == "__main__":
	main()
