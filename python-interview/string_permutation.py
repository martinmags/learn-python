import sys

"""
Given two strings, write a method to 
decide if one is a permutation of the other.
"""
# Time Complexity:
# Space Complexity: O(n)
def is_permutatuation(str1, str2):
  sorted_str1 = sorted(list(str1))
  sorted_str2 = sorted(list(str2))

  print(sorted_str1, sorted_str2)
  # Case: Equal
  if sorted_str1 == sorted_str2:
    return True
  # Case: Unequal length
  if len(sorted_str1) !=  len(sorted_str2):
    return False
  # Case: Equal length
  if (len(sorted_str1) == len(sorted_str2)):
    for i in sorted_str1:
      for j in sorted_str2:
        if i != j:
          return False
  return True


str1 = sys.argv[1]
str2 = sys.argv[2]
output = is_permutatuation(str1, str2)
print(output)