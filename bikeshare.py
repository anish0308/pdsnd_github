 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 19:55:36 2020

@author: anish
"""

import numpy as np
import pandas as pd
import time
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities=['chicago','new york city','washington']

months=['january','february','march','april','may','june','all']

days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    syn="Please follow the proper syntax or please enter a valid entry"
    while(True):
        while(True):
            try:
                city=input('For which city would you like to calculate the data for?:')
                if city.lower() in cities:
                    num=1 
                
                else:
                    num=1/0
                            
            except:
                print(syn)
           
                continue
            else:
                break
            
        while(True):
            try:
                month=input("For which month(s) would you like to calculate the data for?\nPlease enter months from January-June only\nIf you want to filter by all months type 'all' :")
                if month.lower() in months:
                    num=1
                
                else:
                     num=1/0
                           
            except:
                print(syn)
                continue
            else:
                break
            
        while(True):
            try:
                 day=input("For which day(s) would you like to calculate the data for?:\nIf you want to filter by all days type 'all'\n")
           
                 if day.lower() in days:
                      num=1
                 
                 else:
                     num=1/0
                
            except:
                print(syn)
                continue
            else:
                break
               
        print("So you have selected the following data please verify:\n"
              "city:{}\n"
              "month(s):{}\n"
              "day(s):{}\n\n".format(city.lower(),month.lower(),day.lower()))
        confirm=input("In order to confirm your selection please press 'y':")
        if confirm=='y':
             break
       
        else:
             print("\nLet's try this again!")
           

    print('-'*40)
    return city.lower(), month.lower(), day.lower()

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...')
    start_time = time.time()

    # display the most common month
    print('\nFor your selection the most common month for travel is:')
    print(df['month'].mode()[0])

    # display the most common day of week
    print('\nFor your selection the most common day for travel is:')
    print(df['day_of_week'].mode()[0])

    # display the most common start hour
    print('\n For your selection the most common hour for travel is:')
    print(df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...')
    start_time = time.time()

    # display most commonly used start station
    print('\nFor your selection the most popular Start station is:')
    print(df['Start Station'].mode()[0])

    # display most commonly used end station
    print('\nFor your selection the most popular End station is:')
    print(df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
   
    df['Start-End Combination'] = (df['Start Station'] + ' - ' +
                                   df['End Station'])
    most_common_start_end_combination = str(df['Start-End Combination']
                                            .mode()[0])
    print("For your selection, the most common start-end combination "
          "of stations is: " + most_common_start_end_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...')
    start_time = time.time()

    # display total travel time
    print('\nTotal Travel Time:')
    print(datetime.timedelta(seconds=int(df['Trip Duration'].sum())))

    # display mean travel time
    print('\nMean Travel Time:')
    print(datetime.timedelta(seconds=int(df['Trip Duration'].mean())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)    
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...')
    start_time = time.time()

    # Display counts of user types
    print('Counts of User Types:')
    print(df['User Type'].value_counts())

    # Display counts of gender
    print('\nCounts of Genders:')
    try:
        print(df['Gender'].value_counts())
    except:
        print('Gender data not included.')

    # Display earliest, most recent, and most common year of birth
    print('\nEarliest, Latest & Most Common Date of Birth:')
    try:
        print('Earliest: {}\nLatest: {}\nMost Common: {}'
              .format(df['Birth Year'].min(), df['Birth Year'].max(),
                      df['Birth Year'].mode()[0]))
    except:
        print('Data for DOB is not included.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40) 
    
def show(df):
    """Used to return 5 row entries to the terminal"""
    answer = 'yes'
    while answer == 'yes':
        for i in df.iterrows():
            count = 0
            while count < 5:
                print(i)
                count += 1
            response = input('\nView 5 more data entries? Yes or No?\n')
            if response.lower() == 'no':
                answer = 'no'
                break
            
def main():
    """Main Function"""
    while True:
         city,month,day=get_filters()
         df = load_data(city, month, day)
         time_stats(df)
         station_stats(df)
         trip_duration_stats(df)
         user_stats(df)
         show(df)
         
         restart = input('\nWould you like to restart? Yes or No?\n')
         if restart.lower() != 'yes':
              break
           
   
    
    

if __name__ == "__main__":
    main()
        
