
lst = [4, 3, 5, 1, 2]

# print(min(lst))


for i, num in enumerate(lst[:-1]):
    test = min(num, lst[i + 1])

print(test)


# test = lst[0]

# for i in lst:
#     if i < test:
#         test = i

# print(test)
