max_kg_for_elevator = 200
weight_of_ann = 55
weight_of_joe = 120
weight_of_rose = 70

print "max kg for elevator is " + str(max_kg_for_elevator)
print "max kg for elevator is {}".format(max_kg_for_elevator)
print "weight_of_joe is {}, weight_of_rose is {}, weight_of_ann is {}".format(weight_of_joe, weight_of_rose, weight_of_ann)

print "sum of the weights are {}".format(weight_of_rose + weight_of_joe + weight_of_ann)

weights_of_all = weight_of_ann + weight_of_joe + weight_of_rose
print "this three people can use the elevator: {}".format(weights_of_all <= max_kg_for_elevator)
print "joe and rose can use the elevator: {}".format((weight_of_joe + weight_of_rose) <= max_kg_for_elevator)