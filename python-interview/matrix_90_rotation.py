"""
Given an image represented by an NxN matrix, where each pixel in 
the image is 4 bytes, write a method to rotate the image by 90.
Can you do this in place?
"""
# Time  Complexity: O(nm) = O (n2)
# Space Complexity: O(n2)
# Note to self: use numpy next time

import copy
def rotate_90(m):
  if len(m) != len(m[0]):
    return Exception("Can't perform rotation on non nxn matrices")

  output = copy.deepcopy(m)
  index_row = 0
  for row in range(0, len(m)):
    index = 0
    for col in range(len(m)-1, -1,-1):
      output[index_row][index] = m[col][row]
      index +=1
    index_row += 1 
  return output

m = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
  [10,11,12]
]

"""
Rotated
  [7,4,1]
  [8,5,2]
  [9,6,3]
"""
print("Original:\t", m)
print("Rotated:\t", rotate_90(m))