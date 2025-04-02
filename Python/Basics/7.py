# n = int(input("Enter a number: "))
# print(int(n)+2)

#LIST AND METHOD in Python
# l1 = [87,35,7,75,235,7,51,25]
# l1.append(22) #append function is used to insert a new value to the array
# l1.sort()
# l1.pop(2) #pop function is used to remove the element from an array from its respective index
# l1.clear() #it is used to clear the givem array
# print(l1.index(235)) 

#SETS in Python
s1 = {2,4,6,8,3,9,10}
s2 = {3,4,6,9,11,1,0}

print(s1.union(s2)) #union of two sets
print(s1.intersection(s2)) #prints the common elements from two sets

a= {}
b= set()
print(a, type(a))
print(b,type(b))