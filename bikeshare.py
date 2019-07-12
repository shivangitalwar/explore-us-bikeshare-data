import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def parser(input_value, valid_values, indices=2, str_to_ind=False):
    
    """
    Parses the input_value and matches inside the valid_values
    input_value => Taken from outside
    valid_values => List of possible valid values
    indices => How many indexes to verify of input_value to valid_values
    """
    try:
        
        
        
        if type(valid_values) is not list:
            raise Exception
        
       
        valid_values = [value.title() for value in valid_values]
        input_value = str(input_value).title()
        
        if input_value == 'All' or input_value == '*':
                input_value = 'ALL'
                return input_value
            
        """
        The core of the function. Performs two checks:
        1) When the given input is a number, check if the corresponding index exists
            in the valid list. Or
        2) If the input is a string, check its first two indices. Indices are dynamic. 
            Specify how many indices to check while calling this function.
        This type of loop is called list comprehension.
        
        Return => list 
        """
        input_value = [x for i, x in enumerate(valid_values) if ( str(i) == input_value ) or
                           x[:indices] == input_value[:indices] ]
        
       
        if input_value:
            input_value = input_value.pop()
            
            
            if input_value.isdigit():    
                input_value = valid_values[input_value]
            if str_to_ind:
                input_value = int(valid_values.index(input_value)) 
            
               
        return input_value
    except Exception as e:
        print(e)

def newlines(num=2):
    """
    Need some spacing in between? print any number
    of newlines
    num => No of newlines. Default = 2
    """
    i = 0
    while i < num:
        print()
        i=i+1


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('-'*50)
    newlines(2)
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august'
              'september', 'october', 'november', 'december']
    days=['all', '*', "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    
    
    while(True):
        print('Enter as so: [ c|ch|chicago, n|ne|new york|, w|wa|washington ]')
        city=input("Enter city: ")
        city = parser(city, cities, indices=1)
        if city:
            break;
        else:
            print("ERROR!!WRONG INPUT!!\nTRY AGAIN!!");
            newlines()
    
    newlines(3)
    
    while(True):             
    # TO DO: get user input for month (all, january, february, ... , june)
        print('Enter as so: [ All|*, Jan|1, Feb|2, ...., Jun|6 ]')
        month=input("Enter the month: ")
        # Bug when 2 indices are used, march and may....
        month = parser(month, months, indices=3, str_to_ind=True)
        if month:
            break
        else:
            print("ERROR!!WRONG INPUT!!\nTRY AGAIN!!")
            newlines()
            
    newlines(3)
        
    while(True):
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        print('Enter as so: [All|*, su|Su|Sunday,mo|Mo|monday, ... sa|Sa|Saturday ]')
        day=input("Enter the day: ")
        day = parser(day, days)
        if day:
            break
        else:
             print('ERROR!!WRONG INPUT!!\nTRY AGAIN!!')
             newlines()
    
    newlines(3)
    print('-'*40)
    # DEBUG
    print("City: %s  Month: %s (%s) Day: %s" % (city, month, months[month-1] if str(month).isdigit() else "*", day))
    print('-'*40)
    newlines(3)
    print("PROCESSING RESULTS...............")
    print("\nThis might take a while :)")
    newlines(3)
    return city, month, day

def filter_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    dateparser = lambda date: pd.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    
    df = pd.read_csv(CITY_DATA[city.lower()], parse_dates=['Start Time'], date_parser=dateparser)
    df1= pd.read_csv(CITY_DATA[city.lower()], parse_dates=['Start Time'], date_parser=dateparser)
    
    df['year'] = df['Start Time'].dt.year
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    
    
    if month == 'ALL' or day == 'ALL':
        if month == 'ALL' and day == 'ALL':
            new_df = df
        elif month == 'ALL':
            new_df = df.loc[(df['day'] == day), : ]
        elif day == 'ALL':
            new_df = df.loc[(df['month'] == month), : ]
    else:
        new_df = df.loc[(df['month'] == month) & (df['day'] == day), : ]
    
    

    return new_df,df1

def filter_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    
    """

    dateparser = lambda date: pd.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
   
    df = pd.read_csv(CITY_DATA[city.lower()], parse_dates=['Start Time'], date_parser=dateparser)
    df1= pd.read_csv(CITY_DATA[city.lower()], parse_dates=['Start Time'], date_parser=dateparser)
    
    df['year'] = df['Start Time'].dt.year
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    
    
    if month == 'ALL' or day == 'ALL':
        if month == 'ALL' and day == 'ALL':
            new_df = df
        elif month == 'ALL':
            new_df = df.loc[(df['day'] == day), : ]
        elif day == 'ALL':
            new_df = df.loc[(df['month'] == month), : ]
    else:
        new_df = df.loc[(df['month'] == month) & (df['day'] == day), : ]
   

    return new_df,df1
    





def time_stats(df,df1):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df1['Start Time'] = pd.to_datetime(df1['Start Time'])
    df1['month'] =df1['Start Time'].dt.month
    df1['day_of_week'] = df1['Start Time'].dt.weekday_name
    df1['hour'] = df1['Start Time'].dt.hour
    

    

    # TO DO: display the most common month
    comman_month = df1['month'].mode()[0]
    print("The most comman month = ",comman_month)


    # TO DO: display the most common day of week
    comman_weekday = df1['day_of_week'].mode()[0]
    print("The most comman day of week = ",comman_weekday)



    # TO DO: display the most common start hour
    comman_start_hour = df1['hour'].mode()[0]
    print("The most comman start hour = ",comman_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    newlines(3)
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    newlines()
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most commanly used start station = ",popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most commanly used end station = ",popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    popular_combination = df.groupby(['Start Station','End Station']).size().sort_values(ascending=False)
    print("The most commanly used combination = ",popular_combination.index[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    newlines(3)
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    newlines()
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Travel Duration =",df['Trip Duration'].sum())
    

    # TO DO: display mean travel time
    print("Mean of Travel Duration =",df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    newlines(3)
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    newlines()
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    column_list=np.array([df.columns])
    newlines()
    print("Gender counts...")
    if 'Gender' in column_list :
        gender_types = df['Gender'].value_counts()
        print("\n",gender_types)
    else:
        print("\n NO DATA RELATED TO GENDERS FOUND!!")

    newlines()
    # TO DO: Display earliest, most recent, and most common year of birth
    print("Information about Birth years...")
    newlines()
    if 'Birth Year' in column_list:
        min_birth_year = df['Birth Year'].min()
        print("Earliest birth year =",min_birth_year)
        max_birth_year = df['Birth Year'].max()
        print("Most recent birth year =",max_birth_year)
        popular_birth_year = df['Birth Year'].mode()[0]
        print("The most comman birth year = ",popular_birth_year)
    else:
        print("\n NO DATA RELATED TO BIRTH YEAR FOUND!!!")


    print("\nThis took %s seconds." % (time.time() - start_time))
    newlines(3)
    print('-'*40)
    i=0
    j=5
    while(True):
        data=input("\nWant to display trip data?[y/n]:\n")
        if data.lower()[:1]=='y':
            print(df.iloc[i:j,0:])
            i+=5
            j+=5
            newlines()
        else:
            newlines(3)
            print('-'*40)
            print("\n      THANKS FOR TUNING IN!!\n")
            print('-'*40)
            break
            
  
                           

def main():
    while True:
        city, month, day = get_filters()
        df, df1 = filter_data(city, month, day)

        time_stats(df,df1)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
       
            

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
