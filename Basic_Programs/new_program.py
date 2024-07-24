'''Given a city name, check if the city is a metro city. Here are the metro cities: 

Delhi, Mumbai, Bangalore, Kolkata, Chennai

If it is a metro city, print “Metro”. If not a metro, print “Not a Metro”


Example: 

Input: Delhi
Output: Metro

Input: Pune
Output: Not a Metro'''
city=input("Please enter the city name : ").lower()
b=[Delhi, Mumbai, Bangalore, Kolkata, Chennai]
def city_metro(city):
	if city=="delhi" or city=="mumbai" or city=="banglore" or city=="kolkata" or city=="chennai" :
		print("Metro")
	else:
		print("Not a Metro")
city_metro(city)