# **US Bikeshare Data Analysis Project**


## **Overview:**
In this project, _Python_ is used to explore data related to bike share systems for three major cities in the United States — _Chicago, New York City,_ and _Washington_. 
- The source code takes in raw input from the user to create an interactive experience. 
- According to the input the code will import the data and will provide information by computing descriptive statistics.

## **Files used:**
* bikeshare.py

## **Credits:**

* The data for all 3 cities that is used in this project can be accessed through the link mentioned below :
    - [City Data](https://drive.google.com/file/d/1km4EggJaSvHos_7KKFuHoJxbh-StyM4G/view?usp=sharing)

## **Softwares needed:**
* _Python 3, NumPy,_ and _Pandas_ installed using _Anaconda_
* A text editor, like _VS Code_ or _Atom_.
* A terminal application (_Terminal_ on _Mac_ and _Linux_ or _Cygwin_ on _Windows_).

## **Code explained in Detail:**
### **How the program works:**
The code developed takes in raw input to create an interactive experience in the terminal that answers questions about the dataset. The experience is interactive because depending on a user's input, the answers to the questions will change! There are four questions that will change the answers:

* Would you like to see data for: _1. Chicago_, _2. New York City_, _3. Washington_, or _0. Exit_?
* Would you like to filter the data by: _1. Month_, _2. Day_, _3. Both Month and Day_,_4. No filter (view all data)_, _8. Back to select city_,  or _0. Exit_?
* Which month would you like to filter by: _1. January_, _2. February_, _3. March_, _4. April_, _5. May_, _6. June_, _7. Back to previous question_, _8. Back to select city_, or _0. Exit Program_?
* Which day would you like to filter by:  _1. Monday_, _2. Tuesday_, _3. Wednesday_, _4. Thursday_, _5. Friday_, _6. Saturday_, _7. Sunday_, _8.  Back to previous question_, _9. Back to select city_ or _0. Exit Program_?

The answers to the questions above will determine the city and timeframe on which you'll do data analysis. After filtering the dataset, users will see the statistical result of the data, and choose to start again or exit.

### **The Datasets:**
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

* Start Time (e.g., 2017-01-01 00:07:57)
* End Time (e.g., 2017-01-01 00:20:53)
* Trip Duration (in seconds - e.g., 776)
* Start Station (e.g., Broadway & Barry Ave)
* End Station (e.g., Sedgwick St & North Ave)
* User Type (Subscriber or Customer)

The _Chicago_ and _New York City_ files also have the following two columns:

* Gender
* Birth Year

### **Statistics Computed:**
The code helps user to tell about bike share use in _Chicago_, _New York City_ and _Washington_ by computing a variety of descriptive statistics. In this project, the code output will provide the following information:

* Popular times of travel (i.e., occurs most often in the start time):

  - most common month
  - most common day of week
  - most common hour of day

* Popular stations and trip:

  - most common start station
  - most common end station
  - most common trip from start to end (i.e., most frequent combination of start station and end station)

* Trip duration:

  - total travel time
  - average travel time

* User info:

  - counts of each user type
  - counts of each gender (only available for _NYC_ and _Chicago_)
  - earliest, most recent, most common year of birth (only available for _NYC_ and _Chicago_)


