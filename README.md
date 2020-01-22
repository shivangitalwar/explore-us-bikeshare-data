This project makes use to python to explore us bikehare data.

BIKESHARE DATA

bikeshare system allows a user to rent bike for short term basis.The user can borrow bike from point 1 and leave it at point 2 ,
from where some other user can pick it up.Thus each bike can have several users a day.

In this project the data is used to conclude bikehshare usage patterns.The data is used tocompare the system usage between three 
large cities: Chicago, New York City, and Washington, DC.

THE DATASETS

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain
the same core six (6) columns:

Start Time (e.g., 2017-01-01 00:07:57)
End Time (e.g., 2017-01-01 00:20:53)
Trip Duration (in seconds - e.g., 776)
Start Station (e.g., Broadway & Barry Ave)
End Station (e.g., Sedgwick St & North Ave)
User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
Gender
Birth Year

Some wrangling has been done on the datasets . The datasets were huge to be uploaded on github so they were uploaded on google drive and then 
added with the python file.


PROBLEMS TACKLED:
1. Popular times of travel 
  a.most common month
  b.most common day of week
  c.most common hour of day
2.Popular stations and trip
  a.most common start station
  b.most common end station
  c.most common trip from start to end
3.Trip duration
  a.total travel time
  b.average travel time
4.User info
  a.counts of each user type
  b.counts of each gender (only available for NYC and Chicago)
  c.earliest, most recent, most common year of birth (only available for NYC and Chicago)
