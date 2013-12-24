import datetime

def check_data(min, max, user_input):
	if user_input > max or user_input < min:
		return 0 
	return 1
	

print "\n"
print "Welcome to the number of days you have been alive program!\n"
now = datetime.datetime.now()

correct = 0
while(correct == 0):
	year = input("Please enter your year of birth. ")
	correct = check_data(1900,now.year,year)

correct = 0
while(correct != 1):		
	month = input("Please enter your month of birth. ")
	correct = check_data(1,12,month)
	
correct = 0
while(correct != 1):			
	day = input("Please enter your day of birth. ")
	correct = check_data(1, 30, day)

if year == now.year and month > now.month:
	correct = 0
	while(correct != 1):	
		month = input("Please enter a new month that is not in the future. ")
		correct = check_data(1, 12, month)
elif month == now.month and day > now.day:
	correct = 0
	while(correct != 1):	
		day = input("Please enter a new day that is not in the future. ")
		correct = check_data(1, now.day, day)
	
		
if year == now.year:
	if month == now.month:
		total_days = now.day-day
	elif month < now.month:
		total_days = now.day + ((now.month-month)*30-day)
else:
	total_days = (now.year-year)*365+(month*30)-(30-day)
print "this is the number of days you have been alive! " + str(total_days)
