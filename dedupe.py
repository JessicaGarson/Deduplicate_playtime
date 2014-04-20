# Challenge level: Beginner

# Scenario: You have two files containing a list of email addresses of people who attended your events.
#       File 1: People who attended your Film Screening event
#       https://github.com/shannonturner/python-lessons/blob/master/section_09_(functions)/film_screening_attendees.txt
#
#       File 2: People who attended your Happy hour
#       https://github.com/shannonturner/python-lessons/blob/master/section_09_(functions)/happy_hour_attendees.txt

# Goal 1: You want to get a de-duplicated list of all of the people who have come to your events.

#creating the function 
def deduplicate(list1, list2):
	
	return list(set(list1+list2))

#open up the files

with open("film_screening_attendees.txt", "r") as film_people:

	film = film_people.read().split('\n')

with open("happy_hour_attendees.txt", "r") as happy_hour_people:

	happy_hour = happy_hour_people.read().split('\n')

#who attended 

print "Peeps who attended one of the events:"

#print the people who attend stuff

for person in deduplicate(film, happy_hour):

	print person

print "\n"

# Goal 2: Who came to *both* your Film Screening and your Happy hour?

#instead of + I can use & to get both 

def intersect(list1, list2):

	return list(set(list1) & set(list2))

print "Peeps who attended both:"

for person in intersect(film, happy_hour):

	print person

print "\n"

