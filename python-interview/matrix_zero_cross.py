"""
Write an algorithm such that if an element in an MxN matrix 
is 0, its entire row and column are set to 0.
NOTE: Revisit this and review bit arithmetic
NOTE:
# set operations:
z = set()
1 in z # O(1) time membership check
z.add(1) # O(1) time add
z.remove(1) # O(1) delete
"""

import numpy as np
# Time  Complexity: O(mn)
# Space Complexity: O(1)
def matrix_zero_cross(m):
  m = np.array(m)
  num_rows = m.shape[0]
  num_cols = m.shape[1]

  # Bit vector (limited to the 32 bits?)
  zero_rows= 0
  zero_cols= 0
  # Find rows and columns to zero out
  for rows in range(0, num_rows):
    for cols in range(0, num_cols):
      # Found 0 in a row
      if m[rows][cols] == 0:
        zero_rows = zero_rows | (1 << rows)
        zero_cols = zero_cols | (1 << cols)
  # Zero out rows
  for row in range(0, num_rows):
    for col in range(0, num_cols):
      if ((1 << row) & zero_rows) or ((1 << col) & zero_cols):
        m[row][col] = 0

  return m

m = [
  [1,0,2,5,2],
  [1,5,3,7,3],
  [6,2,8,0,4],
  [3,2,4,5,5]
]
output = matrix_zero_cross(m)
print(output)

