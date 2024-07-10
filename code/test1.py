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

print(Rico.rating)

