dictionary = {"hi": 1, 0.00:2.3, "what":"he"}
item = list(dictionary)[0]
print(item)
item2 = dictionary[list(dictionary)[0]]

list = [False, False, False]
for x in range(1,len(list)+1):
  list[x-1] = True

list = [False, True, False]
print(list.index(True))

