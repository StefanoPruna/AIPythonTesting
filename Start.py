import numbers
import pprint

#1. Creating the function and reading the message file
# def decode():
#     f = open("message_file.txt", "r")
#     print(f.read())
 
# decode()

#2. Loop each row to separate the numbers to the words, then print the numbers only
# def decode(n):
#     f = open("message_file.txt", "r")
#     onlyNumbers = []
#     for line in f:
#         for subitem in line.split():
#             if(subitem.isdigit()):
#                 onlyNumbers.append(subitem)
       
#     onlyNumbers.sort()
    
#     #pyramid code
#     num=1
#     list =[]
#     for i in range(0,n):
#         for j in range(0, i+1):            
#             print(num, end=" ")
#             num+=1

#         print("\r")   
    
#     return list
#     #return onlyNumbers
# n=3
# print('\n'.join(decode(n)))

#3. Create the dictionary
def decode():
    f = open("coding_qual_input.txt", "r")
    onlyNumbers = {}
    for line in f:
        (key, val) = line.split()
        onlyNumbers[int(key)] = val
                    
    sortedDic = dict(sorted(onlyNumbers.items()))
    
    sortedDic.pop(2)
    sortedDic.pop(4)
    sortedDic.pop(5)

    keys = sortedDic.keys()
    values = sortedDic.values()
        
    #print("{"+",\n".join("{!r}:{!r}".format(k, v) for k, v in sortedDic.items()) + "}")   
    #Print the keys and the values
    for k, v in sortedDic.items():
        print(k,':',v)
    #Print the values only    
    for values in sortedDic.values():
        print(values)
                 
    return sortedDic.values()

print(decode())