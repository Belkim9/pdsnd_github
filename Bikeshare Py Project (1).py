#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import math
import pandas as pd
import numpy as np

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
    print("Hello! Let\'s explore some US bikeshare data!")
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ""
    while city not in CITY_DATA.keys():
        print("\nWelcome! Please select the city you want to explore:")
        print("\n1. Chicago 2. New York City or 3. Washington")
        print("\nPlease put in the full name of the city, written as previously displayed.")

        city = input().lower()

        if city not in CITY_DATA.keys():
            print("\nPlease check your spelling. Your input seems to be different from the previously displayed options.")
            print("\nPlease try again...")

    print(f"\n You chose the city {city.title()} to explore.")
        # TO DO: get user input for month (all, january, february, ... , june)
    MONTH_DATA = {"january":1, "february":2, "march":3, "april":4, "may":5, "june":6, "all":7}
    month = ""
    while month not in MONTH_DATA.keys():
        print("\nFor which month would you like to explore the data? Select a month from January to June.")
        print("\nPlease put in the full name of the month.")
        print("\nIf you want to explore all months, please type 'all'.")

        month = input().lower()

        if month not in MONTH_DATA.keys():
            print("\nPlease check your spelling. Your input seems to be different from the previously displayed options.")
            print("\nPlease try again...")

    print(f"\n You chose the month {month.title()} to explore.")    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DAY_DATA = {"monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"}
    day = ""
    while day not in DAY_DATA:
        print("\nFor which day would you like to explore the bikeshares? Please enter a day of the week of your choice.")
        print("\nPlease write the name of the day as the following example: 'Monday'.")
        print("\nYou can also select the whole week by writing 'all'.")

        day = input().lower()

        if day not in DAY_DATA:
            print("\nPlease check your spelling. Your input seems to be different from the previously displayed options.")
            print("\nPlease try again...")

    print(f"\nYou chose {day.title()} to explore.")
    print (f"\nYou will be exploring the bikeshare data for the city of {city.upper()}, in the month of {month.upper()} and for the day {day.upper()}.")

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
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()
    
    if month != "all":
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1
        
        df = df[df["month"] == month]
        
    if day != "all":
        df = df[df["day_of_week"] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df["month"].mode()[0]
    print(f"\nThe most common month is (1 = January,...,6 = June): {common_month}")

    # TO DO: display the most common day of week
    common_day = df["day_of_week"].mode()[0]
    print(f"\nThe most common day is: {common_day}")
    
    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    common_hour = df["hour"].mode()[0]
    print(f"\nThe most common day is: {common_hour}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df["Start Station"].mode()[0]
    print(f"\nThe most common start station is {common_start_station}.")

    # TO DO: display most commonly used end station
    common_end_station = df["End Station"].mode()[0]
    print(f"\nThe most common end station is {common_end_station}.")

    # TO DO: display most frequent combination of start station and end station trip
    df["Start and End"] = df["Start Station"].str.cat(df["End Station"], sep=" and ")
    combo = df["Start and End"].mode()[0]
    print(f"\nMost frequently people ride the bikes between {combo}.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df["Trip Duration"].sum()
    minute, second = divmod(total_time, 60)
    hour, minute = divmod(minute, 60)
    print(f"\nThe total travel time is {hour} hours, {minute} minutes and {second} seconds.")

    # TO DO: display mean travel time
    mean_time = round(df["Trip Duration"].mean())
    minute, second = divmod(mean_time, 60)
    if minute > 60:
        hour, minute = divmod(minute, 60)
        print(f"\nThe mean travel time is {hour} hours, {minute} minutes and {second} seconds.")
    else:
        print(f"\nThe mean travel time is {minute} minutes and {second} seconds.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df["User Type"].value_counts()
    print(f"\nThe types of users ar: \n{user_type}")

    # TO DO: Display counts of gender
    try:
        gender = df["Gender"].value_counts()
        print(f"\nUsers by gender are \n{gender}")
    except:
        print(f"\nGender not found.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df["Birth Year"].min())
        latest = int(df["Birth Year"].max())
        common_year = int(df["Birth Year"].mode()[0])
        print(f"\nThe earliest year of birth is {earliest}. \nThe latest year of birth is {latest}. \nThe most common year of birth is {common_year}.")
    except:
        print(f"\nThere is no information on birth year.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    choice = input('Would you like to see some of the raw data? Yes/No ').lower()
    print()
    if choice == 'yes' or choice == 'y':
        choice = True
    elif choice == 'no' or choice == 'n':
        choice = False
    else:
        print('Please check your spelling and try again. ')
        display_data(df)
        return

    if choice:
        index = 0
        while 1:
            for i in range(index, index+5):
                print(df.iloc[i])
                print()
            choice = input('Another five? Yes/No ').lower()
            if choice == 'yes' or choice=='y':
                index += 5
                continue
            elif choice == 'no' or choice == 'n':
                break
            else:
                print('Please check your spelling and try again.')
                return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        print()
        if restart != 'yes' and restart != 'y' and restart != 'yus':
            break

if __name__ == "__main__":
	main()


# In[ ]:




