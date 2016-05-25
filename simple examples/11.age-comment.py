print "How old are you?"
age = int(raw_input())

if age < 18:
	print "You can't drive"
elif age > 18 and age < 60:
	print "You can drive"
else:
	print "Don't drive, take a free akbil :)"