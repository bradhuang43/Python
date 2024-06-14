from array import array
import numpy
import random

number_list1 = []
for i in range(10):
    number_list1.append(random.randint(0, 9))

number_list2 = []
for i in range(10):
    number_list2.append(random.randint(0, 9))

number_list3 = []
for i in range(10):
    number_list3.append(random.randint(0, 9))

number_list4 = []
for i in range(10):
    number_list4.append(random.randint(0, 9))

number_list5 = [number_list1, number_list2, number_list3, number_list4]

def norm_square_list(vector):
    norm = 0
    for v in vector:
        norm += v*v
    return norm

def norm_square_list_comprehension(vector):
    return sum([v*v for v in vector])

def norm_squared_generator_comprehension(vector):
    return sum(v*v for v in vector)

def norm_square_array(vector):
    norm = 0
    for v in vector:
        norm += v*v
    return norm

def norm_square_numpy(vector):
    return numpy.sum(vector * vector)

def norm_square_numpy_dot(vector):
    return numpy.dot(vector, vector)

print(norm_square_list(random.choice(number_list5)))
print(norm_square_list_comprehension(random.choice(number_list5)))
print(norm_squared_generator_comprehension(random.choice(number_list5)))
print(norm_square_array(random.choice(number_list5)))
print(norm_square_numpy(random.randint(0, 9)))
print(norm_square_numpy_dot(random.randint(0, 9)))
