empty_list = []
print()
num = [1, 2, 3, 4, 5]
print(num)
triples = [1, 2, 3] * 3
print(triples)
alist = [100, 200, 300, 400, 500]
alist = alist[::-1]
print(alist)


def match(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr = ctr + 1
            lst.append(word)
    print("List of words with first and last character same\n", lst)
    return ctr
count = match(["xyz", "aba", "cfc", "1221"])
print("Number of words having first and last character same: ", count)


l = [4, 5, 1, 2, 9, 7, 10, 0]
print("Original list: ", l)
count = 0
for i in l:
    count = count + i
avg = count/len(l)
print("Average of the numbers is: ", avg)
print("The sum of the numbers is: ", count)
l.sort()
print("Smallest element is: ", l[0])
print("Largest element is: ", l[-1])