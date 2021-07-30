from collections import OrderedDict

n = int(input("Enter number of strings you want to enter: "))
dic = {}   #Declaration of Dictonary
l = []   #Declaration of List

for i in range(n):
  a = input("Enter string: ")
  l.append(a)
  if a in dic:
    dic[a] += 1  #if word is already in dic, increment key-value by 1
  else:
    dic[a] = 1  #if word is not in dic, assign key-value 1
    
print("Total number of Distinct strings= ", len(dic))
print(' '.join([str(dic[a]) for a in dic]))

#BONUS

print("\nBonus: ")
print("\nWords in Descending:")
dic_sorted = sorted(dic, key=dic.get, reverse=True)
for r in dic_sorted:
    print(r,": ", dic[r])
    
maximum = max(dic, key=dic.get)  # Gets max. key value, i.e  number of occurences
print("\nMost repeated word is:", maximum, "=", dic[maximum])

minimum = min(dic, key=dic.get)  # Gets min. key value, i.e  number of occurences
print("\nLeast repeated word is:",minimum, "=",dic[minimum])
