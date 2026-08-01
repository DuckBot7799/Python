list = ["123", "456"]
print(len(list))

group = [True, False, False]
print(group)


group2 = ["123", "456", "789"]
print(group2[-3])



thislist = ["apple", "banana", "cherry", "kiwi", "mango", 123, 5.2]
b = "berry"
if b in thislist:
    print(f"Yes, {b} is available")
else:
    print(f"No, {b} is not available")