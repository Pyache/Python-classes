student = {"id1":{"name":["Sara"],"class":["V"], "Subject Integration":["English, Math, Science"]}, 
           "id2":{"name":["David"], "class":["V"], "Subject Integration":["English, Math, Science"]}, 
           "id3":{"name":["Sara"], "class":["V"], "Subject Integration":["English, Math, Science"]}, 
           "id4":{"name":["Surya"], "class":["V"], "Subject Integration":["English, Math, Science"]}}
result = {}
for key, value in student.items():
    if value not in result.values():
        result[key] = value
print(result)


test = {"Codingal":2, "is":2, "best":2, "for":2, "coding":1}
print("The original dictionary: " + str(test))
k = 2
res = 0
for key in test:
    if test[key] == k:
        res += 1
print("The frequency of 2 in this dictionary is: " + str(res))


code = {"India":"0091", "Australia":"0025", "Nepal":"00977"}
print("Country code for India: ")
print(code.get("India", "Not Found"))
print("Country code for Australia: ")
print(code.get("Australia", "Not Found"))
print("Country code for Japan: ")
print(code.get("Japan", "Not Found"))