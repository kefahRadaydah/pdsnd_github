import time
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
    print("Hello! Let's explore some US bikeshare data!")

    # Step 1: Get user input for city
    while True:
        print("Would you like to see data for:")
        print("1. Chicago")
        print("2. New York City")
        print("3. Washington")
        print("0. Exit")

        city = input("Please enter the corresponding number: ")

        if city == '1':
            city = "Chicago"
            break
        elif city == '2':
            city = "New York City"
            break
        elif city == '3':
            city = "Washington"
            break
        elif city == '0':
            print("Exiting program.")
            exit()  # Exit the entire script
        else:
            print("Invalid input. Please enter 1, 2, 3, or 0 to exit.")

    # Step 2: Get user input for filter type (month, day, both, or no filter)
    while True:
        print("Would you like to filter the data by:")
        print("1. Month")
        print("2. Day")
        print("3. Both Month and Day")
        print("4. No filter (view all data)")
        print("8. Back to select city")
        print("0. Exit")

        filter_choice = input("Please enter the corresponding number: ")

        if filter_choice == '1':
            month, day = get_month(), "all"
            if month is None:
                continue  # If user chooses "Back", restart filter choice
            break
        elif filter_choice == '2':
            month, day = "all", get_day()
            if day is None:
                continue  # If user chooses "Back", restart filter choice
            break
        elif filter_choice == '3':
            month = get_month()
            day = get_day()
            if month is None:
                continue  # If user chooses "Back", restart filter choice
            if day is None:
                continue  # If user chooses "Back", restart filter choice
            break
        elif filter_choice == '4':
            month, day = "all", "all"
            break
        elif filter_choice == '8':
            return get_filters()  # Restart from selecting city
        elif filter_choice == '0':
            print("Exiting program.")
            exit()  # Exit the entire script
        else:
            print("Invalid input. Please enter a valid number.")

    print('-'*40)
    return city, month, day

def get_month():
    """Get user input for month."""
    while True:
        print("Which month would you like to filter by?")
        print("1. January")
        print("2. February")
        print("3. March")
        print("4. April")
        print("5. May")
        print("6. June")
        print("7. Back to previous question")
        print("8. Back to select city")
        print("0. Exit Program")

        month = input("Please enter the corresponding number: ")

        if month == '1':
            return "January"
        elif month == '2':
            return "February"
        elif month == '3':
            return "March"
        elif month == '4':
            return "April"
        elif month == '5':
            return "May"
        elif month == '6':
            return "June"
        elif month == '7':
            return get_filters()  # Go back to main filter choice
        elif month == '8':
            return get_filters()  # Restart from selecting city
        elif month == '0':
            print("Exiting program.")
            exit()  # Exit the entire script
        else:
            print("Invalid input. Please enter a valid number.")

def get_day():
    """Get user input for day."""
    while True:
        print("Which day would you like to filter by?")
        print("1. Monday")
        print("2. Tuesday")
        print("3. Wednesday")
        print("4. Thursday")
        print("5. Friday")
        print("6. Saturday")
        print("7. Sunday")
        print("8. Back to previous question")
        print("9. Back to select city")
        print("0. Exit Program")

        day = input("Please enter the corresponding number: ")

        if day == '1':
            return "Monday"
        elif day == '2':
            return "Tuesday"
        elif day == '3':
            return "Wednesday"
        elif day == '4':
            return "Thursday"
        elif day == '5':
            return "Friday"
        elif day == '6':
            return "Saturday"
        elif day == '7':
            return "Sunday"
        elif day == '8':
            return None  # Go back to main filter choice
        elif day == '9':
            return get_filters()  # Restart from selecting city
        elif day == '0':
            print("Exiting program.")
            exit()  # Exit the entire script
        else:
            print("Invalid input. Please enter a valid number.")



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
    city = city.lower()  # To handle case-insensitivity in city name
    df = pd.read_csv(CITY_DATA[city])

    # Convert the 'Start Time' column to datetime format for filtering
    df = df.drop(columns=['Unnamed: 0'])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day and hour from the 'Start Time' column
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day'] = df['Start Time'].dt.day_name()
    df['Start Hour'] = df['Start Time'].dt.hour

    # Filter by month if applicable
    if month != "all":
        df = df[df['Month'] == month]

    # Filter by day if applicable
    if day != "all":
        df = df[df['Day'] == day]
    return df

def show_raw_data(df):
    """Displays raw data based on user input for the number of rows."""
    
    show_data = input("\nWould you like to see some raw data? Enter 'yes' or 'no': ").lower()
    
    if show_data != 'yes':
        print("Okay, no raw data will be displayed.")
        return  # Exit the function if the user does not want to see raw data
    
    while True:
        try:
            num_rows = int(input("\nHow many rows of raw data would you like to see? Enter a number: "))
            if num_rows <= 0:
                print("Please enter a positive number.")
                continue
            print(df.head(num_rows))  # Display the specified number of rows
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
        show_data = input("\nWould you like to see more raw data? Enter 'yes' or 'no': ").lower()
        if show_data != 'yes':
            break
            
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if 'Month' in df.columns:
        # Handle missing data (if any)
        most_common_month = df['Month'].mode()
        if not most_common_month.empty:
            print(f"Most common month: {most_common_month[0]}")
        else:
            print("No valid data found for 'Month'.")
    else:
        print("Month column is not available in the data.")

    # TO DO: display the most common day of week
    if 'Day' in df.columns:
        most_common_day = df['Day'].mode()
        if not most_common_day.empty:
            print(f"Most common day: {most_common_day[0]}")
        else:
            print("No valid data found for 'Day'.")
    else:
        print("Day column is not available in the data.")

    # TO DO: display the most common start hour
    if 'Start Hour' in df.columns:
        # Now you can proceed with finding the most common start hour
        most_common_hour = df['Start Hour'].mode()[0]
        print(f"Most common start hour: {most_common_hour}")
    else:
        print("Start Time column is not available in the data.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print(f"Most common start station: {most_common_start_station}")

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print(f"Most common end station: {most_common_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    most_common_trip = (df['Start Station'] + " to " + df['End Station']).mode()[0]
    print(f"Most frequent trip: {most_common_trip}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"Total travel time: {total_travel_time} seconds")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"Average travel time: {mean_travel_time:.2f} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User types count:")
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("\nGender count:")
        print(gender_counts)
    else:
        print("\nGender data not available.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])

        print(f"\nEarliest birth year: {earliest_birth_year}")
        print(f"Most recent birth year: {most_recent_birth_year}")
        print(f"Most common birth year: {most_common_birth_year}")
    else:
        print("\nBirth Year data not available.")

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
        
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
