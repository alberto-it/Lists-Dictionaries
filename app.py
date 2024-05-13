def lb():
    print()
    print( '=' * 50)
    print()

lb()

def squares_list_comp(n): return [x**2 for x in range(1, n+1)]
# Time complexity: O(n) | Space complexity: O(n)
print(squares_list_comp(10))

lb()

def reverse_sublist(lst, i, j):
    if i < 0 or j >= len(lst) or i >= j: return -1
    lst[i:j+1] = reversed(lst[i:j+1])
    return lst
# Time complexity: O(n) | Space complexity: O(1)
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(reverse_sublist(my_list, 2, 4))

lb()

def merge_sorted_lists(list1, list2):
    merged_list = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
           merged_list.append(list1[i])
           i += 1
        else:
           merged_list.append(list2[j])
           j += 1
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    return merged_list
# Time complexity: O(n) | # Space complexity: O(n)
list1 = [1, 3, 5]
list2 = [2, 4, 6]
print(merge_sorted_lists(list1, list2))

lb()

def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict
# Time complexity: O(n) |  Space complexity: O(n)
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
print(merge_dictionaries(dict1, dict2)) 

lb()

def find_intersection(dict1, dict2):
    intersection_dict = {}
    for key in dict1:
        if key in dict2 and dict1[key] == dict2[key]:
            intersection_dict[key] = dict1[key]
    return intersection_dict
# Time complexity: O(n) | Space complexity: O(n)
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 1, 'x': 4, 'c': 3}
print(find_intersection(dict1, dict2)) 

lb()

def word_frequency(words):
    word_counts = {}
    for word in words:
        if word in word_counts: word_counts[word] += 1 
        else: word_counts[word] = 1
    return word_counts
# Time complexity: O(n) | Space complexity: O(n)
words = ["apple", "banana", "apple", "orange", "banana"]
print(word_frequency(words)) 

lb()