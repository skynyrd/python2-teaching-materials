print "Write your weight in kg"
weight = int(raw_input())

print "Write your height in meters"
height = float(raw_input())

bmi = weight / (height * height)
print "Your bmi is {}".format(bmi)