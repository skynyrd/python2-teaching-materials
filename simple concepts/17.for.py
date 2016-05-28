import sys

for index in range (10): #0-10, 10 is not included.
    print index
    
print "***********"

for index in range(3,7): #3-7, 7 is not included
    sys.stdout.write(str(index))
    
print "\n***********"

for index in range(4, 10, 2): #4-10, 10 not included, increasing by 2.
    print index

print "***********"

for letter in "Python":
    print letter