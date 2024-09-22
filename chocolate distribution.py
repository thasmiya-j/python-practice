def find_min_diff(chocolates, m):
  # Step 1: Sort the array of chocolates
  chocolates.sort()

  # Initialize the minimum difference to a large value
  min_diff = float('inf')

  # Step 2: Traverse all the groups of size m
  for i in range(len(chocolates) - m + 1):
      # Find the difference between the largest and smallest in the current group
      diff = chocolates[i + m - 1] - chocolates[i]

      # Update the minimum difference
      if diff < min_diff:
          min_diff = diff

  # Return the smallest difference found
  return min_diff
