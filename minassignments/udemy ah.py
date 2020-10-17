#%%* Create a Python application that reads the data on Udemy Web Development offerings.
import os
import csv
udemy_csv = os.path.join("..", "Resources", "web_starter.csv")
#%% * Then store the contents of the Title, Price, Subscriber Count, Number of Reviews, and Course Length into Python Lists.
# Lists to store data
title = []
price = []
subscribers = []
reviews = []
review_percent = []
length = []
#%% Then zip these lists together into a single tuple.
with open(udemy_csv, newline='', encoding='utf-8') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")
     for row in csvreader:
        
        course_title = row[1]
        course_price = row[4]
        course_subscribers = row[5]
        course_reviews = row[6]        
        
        # Add title
        title.append(course_title)

        # Add price
        price.append(course_price)

        # Add number of subscribers
        subscribers.append(course_subscribers)

        # Add amount of reviews
        reviews.append(course_reviews)

        # Determine percent of review left to 2 decimal places
        percent = round(float(course_reviews) / float(course_subscribers), 2)
        review_percent.append(percent)

        # Get length of the course to just a number
        new_length = row[9].split(" ")
        length.append(float(new_length[0]))
