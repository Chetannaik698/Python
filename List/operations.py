#1-append => by default add at end
a = [1,2,3]
a.append(4)
print(a)

#2-extend
b = [1,2,3]
d = [4,5,6]
b.extend(d)
print(b)

#3-insert
x = [1, 2, 3, 4]
x.insert(0, "hi coders")
print(x)

#4-remove => pass data
x.remove(3)
print(x)

#5-pop => pass index
poped = x.pop(0)
print(poped)
print(x)

#6-clear
x.clear()
print(x)

#7.index num
x = [1, 1, 2, 12, 3]
idx = x.index(2)
print(idx)

#8-count
counter = x.count(1)
print(counter)

#9-sort
y = [30, 40, 10, 20]
sorted = y.sort()
print(sorted)

#10-everse
items = ["one", "two", "three"]
items.reverse()
print(items)