# Write a Python program to print all positive numbers in a range.
# Your Input and output must look something like this
# Input: list1 = [12, -7, 5, 64, -14] Output: 12, 5, 64
# Input: list2 = [12, 14, -95, 3] Output: [12, 14, 3]
#list1 = int(input("Enter the list"))

def print_positive_num(list1):
    for ele in list1:
        if ele > 0:
            print(ele)
print_positive_num([12, -7, 5, 64, -14])