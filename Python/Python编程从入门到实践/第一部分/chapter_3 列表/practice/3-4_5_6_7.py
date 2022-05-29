
from subprocess import list2cmdline


list = ['bob','lily','alex']

print(f"The Guest list is : {list}")

print("Bob can't come")
list.remove('bob')
print(f"The new list is {list}")

print("I found a larger table, so I can invite more people")
list.insert(0,'alice')
list.insert(2,'eric')
list.append('mox')
print(f"So the new lsit is:{list}")

print("There is a sad message that I only can invite 2 persons")
print(f"I'm sorry,{list.pop()}")
print(f"I'm sorry,{list.pop()}")
print(f"I'm sorry,{list.pop()}")
print(f"Luckily,{list[0]},you can still attend the party!")
print(f"Luckily,{list[1]},you can still attend the party!")

del list[1]
del list[0]

print(f"The list is:{list}")

