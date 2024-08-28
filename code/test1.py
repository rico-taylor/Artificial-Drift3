dictionary = {"hi": 1, 0.00:2.3, "what":"he"}
item = list(dictionary)[0]
print(item)
item2 = dictionary[list(dictionary)[0]]

list = [False, False, False]
for x in range(1,len(list)+1):
  list[x-1] = True

list = [False, True, False]


class Person:
  def __init__(self, age, height, rating):
    self.age = age
    self.height = height
    self.rating = rating

Rico = Person(17, 176, 10)
b=[True,False]

jack = [(1,10),(2,9),(3,8),(4,7)]
for x in range(len(jack)*2):
  print(x%4)

def is_list(input_data):
    return type(input_data) == list

# Testing the function
print(is_list([1, 2, 3]))  # Output: True
print(is_list(42))         # Output: False

b = 0
if type(b) == int:
  print("true")
