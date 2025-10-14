
fruits = ['tomato', 'strawberry', 'mango', 'kiwi', 'guava', 'banana']
vegetables = ['eggplant', 'broccoli', 'carrot', 'cauliflower', 'zucchini']

def combine_and_sort_two_lists(list1, list2):
    newList = []
    
    if (isinstance(list1, list) and isinstance(list2, list)):
        for i in range(len(list1)):
            newList.append(list1[i])
     
        for k in range(len(list2)):
            newList.append(list2[k])
        
        return sorted(newList)
    else:
        return "None"

print(combine_and_sort_two_lists(fruits, vegetables))
print(fruits)
print(vegetables)
print(combine_and_sort_two_lists([1, 2, -5], [0, 8, 12, -100]))
print(combine_and_sort_two_lists("I'm not a list", vegetables))
print(combine_and_sort_two_lists(fruits, 42))
