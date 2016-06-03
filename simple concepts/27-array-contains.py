sample_array = [45,39,32,12,44,50,26,42,16,20]

print "Guess the number:"
input = int(raw_input());

print "Your guess is {}".format(input)

if input in sample_array:
    print "...and it is in array!"
else:
    print "...and it is not in the array..."
    
# for item in sample_array:
#     if item == input:
#         print "...and it is in array!"
#         break
#     else:
#         if sample_array[-1] == item:
#             print "...and it is not in the array..."   
#         continue
