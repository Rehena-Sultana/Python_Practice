'''
4. দুটো list এর:
   - Common elements বের করো
   - যেগুলো শুধু প্রথম list এ আছে
   - Merge করে duplicates বাদ দিয়ে sort করো
'''
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

# common elements
common = [x for x in list1 if x in list2]

print("Common Elements =", common)

# only in first list
only_first = [x for x in list1 if x not in list2]

print("Only in First List =", only_first)

# merge, remove duplicates, and sort
merged = sorted(list(set(list1 + list2))) #set removes the duplicate

print("Merged Sorted List =", merged)