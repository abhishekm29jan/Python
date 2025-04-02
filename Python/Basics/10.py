# DICTIONARY FUNCTIONS
dict1 = {'Abhishek':45, 'Aditya':99,'Shreya':56, 'Jaadu':97, 'Rakesh':76}
print(dict1['Aditya'])
# print(dict1['Aditya malhotra']) #throws an error
print(dict1.get('Aditya')) #get is used to give the value from the dict1
print(dict1.get('Abhishek Bachan')) #get doesnot gove error even if the value is not stored in the dictionary
print(dict1.keys())
print(dict1.values())