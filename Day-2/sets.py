# sets - {} - unindexed - unordered - do not allow duplicate values

my_set = {1, 2, 2, 3, 3, 3}

print(my_set)

# set operations:

set_a = {10, 20, 30, 40}
set_b = {40, 50, 60, 70}
#set_c = {80, 90, 100, 110}

print(set_a.union(set_b)) # combined

print(set_a.intersection(set_b)) # common

print(set_a.difference(set_b)) # difference

print(set_a.symmetric_difference(set_b)) # symmetric difference

print(set_a.issubset(set_b)) # subset check

print(set_a.issuperset(set_b)) # superset check

print(set_a.isdisjoint(set_b)) # disjoint check

# extra operations

#add an element
set_a.add(140)

#remove an element
set_b.remove(3) # error if element not found

set_b.discard(3) # no error if not found

#clear all elements
set_a.clear()

set_c={1, 2, 2, 3, 3}

print(len(set_c))