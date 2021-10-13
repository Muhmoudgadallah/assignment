import time
import pandas as pd
import numpy as np
from statistics import mode

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('city (chicago, new york city, washington)')
    print('month (all, january, february, ... , june)')
    print('day of week (all, monday, tuesday, ... sunday)')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # get user input for month (all, january, february, ... , june)
    # get user input for day of week (all, monday, tuesday, ... sunday)

    city = str(input("enter the city :"))
    month = str(input("enter the month :"))
    day = str(input("enter the day : "))
    print('-'*40)
    return city, month, day


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
    
    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df["Start Time"]) 
    df["Time"]  = df["Start Time"].dt.hour
    df["day"]   = df["Start Time"].dt.day
    df["month"] = df["Start Time"].dt.month
    days ={'monday':1,'tuesday':2,'wednesday':3,'thursday':4,'friday':5,'saturday':6,'sunday':7}
    months = {'january':1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6}
    if month != 'all' and day != 'all' :
            # use the index of the months list to get the corresponding int
        # filter by month to create the new dataframe
        df = df[(df['month'] == months[month]) & (df['day'] == days[day])]
        return df
    # filter by day of week if applicable
    else :
        # filter by day of week to create the new dataframe
        return df
    
    


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    print( f"the most common month : {mode(df['month'])}")

    # display the most common day of week
    print(f"most common day of week : {mode(df['day'])}")

    # display the most common start hour
    print(f"most common start hour : {mode(df['Time'])}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):

    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most
    print("commonly used start station")
    print(mode(df['Start Station']))
    print("---------------------")
    # display most commonly used end station
    print("commonly used end station")

    print(mode(df['End Station']))
    print("---------------------")

    # display most 
    print("frequent combination of start station and end station trip")
    print(mode(zip(df['Start Station'],df['End Station'])))
    print("---------------------")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display 
    print("total travel time")
    print(df['Trip Duration'].sum())
    print("total travel mean")
    print(df['Trip Duration'].mean())

    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts())

    # Display counts of gender
    # Display earliest, most recent, and most common year of birth
    print("counts of gender")
    print(df['Gender'].value_counts())
    print('-----------------------')
    print("old Birth Year",':',df["Birth Year"].min()) #old
    print('-----------------------')

    print("latest Birth Year",':',df["Birth Year"].max()) #young
    print('-----------------------')

    print("common Birth Year",':',mode(df["Birth Year"])) #young
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
