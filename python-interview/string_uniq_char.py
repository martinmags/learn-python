""" 
Implement an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures?
"""
# Time  Complexity: O(n)
# Space Complexity: O(n)
# where n is the size of the string

def is_uniq(str1):
  # Base Case: if input is invalid
  if type(str1) != str:
    return False
  
  for current in range(1, len(str1)):
    for backtrack in range(0, current):
      print("hi")
      if(str1[current] == str1[backtrack]):
        return False
  return True

result = is_uniq("abc")
print(result)

