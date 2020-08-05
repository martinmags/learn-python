"""
Write a method to replace all spaces in a string with '%20'.
You may assume that the string ha sufficient space at the end 
of the string to hold the additional characters, and that you 
are given the "true" length of the string.
EX:
  Input:  "Mr John Smith", 13
  Output: "Mr%20John%20Smith"
"""
# Time Complexity: O(n)
# Space Complexity: O(n)
def space_replace(str1, n):
  output = ''
  for i in str1:
    if ord(i) == 32:
      i = '%20'
    output += i
  return output

str1 = "Yo I'm Casey."
output = space_replace(str1, len(str1))
print(output)