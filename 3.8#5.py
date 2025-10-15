# ECEGR-2000
# Exercise 5 
# Author: Edrich Rabanes

# predefined testing lists
fruits = ['tomato', 'strawberry', 'mango', 'kiwi', 'guava', 'banana']
vegetables = ['eggplant', 'broccoli', 'carrot', 'cauliflower', 'zucchini']

def combine_and_sort_two_lists(list1, list2):
    newList = []
    
    if (isinstance(list1, list) and isinstance(list2, list)): # checks if both inputs are lists
        for i in range(len(list1)): 
            newList.append(list1[i]) # adds everything in first list to new list
     
        for k in range(len(list2)):
            newList.append(list2[k]) # adds everything to second list to new list
        
        return sorted(newList) # sorts out the combined list
    else:
        print("Error in combine_and_sort_two_lists: one argument is not a list") # error msg if an argument is not a list
        return None

# print tests to ensure code runs correctly
print(combine_and_sort_two_lists(fruits, vegetables))
print(fruits)
print(vegetables)
print(combine_and_sort_two_lists([1, 2, -5], [0, 8, 12, -100]))
print(combine_and_sort_two_lists("I'm not a list", vegetables))
print(combine_and_sort_two_lists(fruits, 42))

