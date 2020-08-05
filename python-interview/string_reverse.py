import sys
"""
Implement a function void reverse(char* str) which
reverses a null-terminated string.
"""
# Time  Complexity: O(n)
# Space Complexity: O(n)
class Solution():
  def __init__(self, s):
    self.s = s
    
  def reverse(self):
    output = ''
    end = len(self.s)-1
    start = -1

    for i in range(end, start, -1):
      output += s[i]
    print(output)

# input
s = sys.argv[1]
solution = Solution(s)
solution.reverse()


