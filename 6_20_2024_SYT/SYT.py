import itertools
import random

def is_valid_SYT(candidate):
  """
  Check if the given candidate tableau is a valid standard Young tableau.

  Parameters:
  - candidate (Tuple[Tuple[int]]): The tableau to be checked.

  Returns:
  - bool: True if the matrix is valid, False otherwise.

  The function checks if the given matrix is a valid SYT matrix by verifying that:
  1. The elements in each column are in strictly increasing order.
  2. The elements in each row are in strictly increasing order.

  Example:
  >>> is_valid_SYT(((1, 2, 3), (4, 5, 6), (7, 8, 9)))
  True
  >>> is_valid_SYT(((1, 2, 3), (5, 4), (6))
  False
  """

  # Check if the elements in each column are in strictly increasing order
  for tuple in candidate:
    previous = tuple[0]
    for i in range(1, len(tuple)):
      if tuple[i] < previous:
        return False
      previous = tuple[i]

  # Check if the elements in each row are in strictly increasing order

  for i in range(len(candidate)- 1):
    for j in range(len(candidate[i])):
      if len(candidate[i+1]) <= j:
        candidate[i][j] >= candidate[i+1][j]
        return False

  return True

def reshape_perm(perm, shape):
  """
  Reshapes a permutation into a tableau based on the given shape.

  Parameters:
  - perm (Tuple[int]): The permutation to be reshaped.
  - shape (Tuple[int]): The shape of the resulting tableau as a weakly decreasing tuple of integers.

  Returns:
  - Tuple[Tuple[int]]: A tuple of tuples representing the reshaped permutation as a tableau.

  Example:
  >>> reshape_perm((1, 2, 3, 4, 5, 6), (3, 2, 1))
  ((1, 2, 3), (4, 5), (6,))
  """
  prev = 0
  tuple_list = []
  for i in range(len(shape)):
    tuple_list.append(perm[prev:prev + shape[i]])
    prev = prev + shape[i]
  return tuple(tuple_list)


def SYTs(shape):
  """
  Generates SYTs (Standard Young Tableaux) of on the given shape.

  Parameters:
  - shape (Tuple[int]): The shape of the resulting SYTs as a tuple of integers.

  Returns:
  - List[Tuple[Tuple[int]]]: A list of valid SYTs generated based on the given shape.

  Example:
  >>> SYTs((2, 1))
  [((1, 2), (3,)), ((1, 3), (2,))]
  """
  results = []

  # Create initial tableau of 0s
  tableau = [[0] for i in range(len(shape))]
  for i in range(len(shape)):
    tableau[i] = [[0] for j in range(shape[i])]
    tableau[0][0] = 1
  results.append(tableau)

  n = sum(shape)

  # Fill it up with numbers 1-n
  if n > 1:
    for i in range(2, n):
      # make list of potential empty squares: the ones that directly border filled up squares
      possible_squares = {}
      for j in range(len(shape)):
        for k in range(len(shape[i])):
          if tableau[i][j] == 0 and (tableau[i -1][j] or tableau[i][j-1] != 0):
            possible_squares.add(i, j)
      for square in possible_squares.items():
        for l in range(len(results)):
          tableau = results[l]
          if tableau[square[0]][square[1]] == 0:
            tableau[square[0]][square[1]] = n
          else:
            tableau_copy = tableau
            tableau[square[0]][square[1]] = n
            tableau.append[tableau_copy]

  return results

def random_SYT(shape):
  """
  Generates a random Standard Young Tableau (SYT) of the given shape.

  Parameters:
  - shape (Tuple[int]): The shape of the resulting SYT as a tuple of integers.

  Returns:
  - Tuple[Tuple[int]]: A random valid SYT generated based on the given shape.

  This function generates a random permutation of numbers from 1 to n+1, where n is the sum of the elements in the `shape` tuple. It then reshapes the permutation into a tableau using the `reshape_perm` function. If the resulting tableau is not valid, it shuffles the permutation and tries again. The function continues this process until a valid SYT is found, and then returns the reshaped permutation as a tableau.

  Example:
  >>> random_SYT((2, 1))
  ((1, 2), (3,))
  """
  nums = list(range(1, n+2))
  permutation = random.shuffle(nums)
  tableau = reshape_perm(permutation, shape)
  if is_valid_SYT(tableau):
    return tuple()

def random_SYT_2(shape):
  """
  Generates a random Standard Young Tableau (SYT) of the given shape.

  Parameters:
  - shape (Tuple[int]): The shape of the resulting SYT as a tuple of integers.

  Returns:
  - Tuple[Tuple[int]]: A random valid SYT generated based on the given shape.

  The function generates a random SYT by starting off with the all zeroes tableau and greedily filling in the numbers from 1 to n. The greedy generation is repeated until a valid SYT is produced.

  Example:
  >>> random_SYT_2((2, 1))
  ((1, 2), (3,))
  """
  # Create initial tableau of 0s
  tableau = [[0] for i in range(len(shape))]
  for i in range(len(shape)):
    tableau[i] = [[0] for j in range(shape[i])]
  tableau[0][0] = 1
  n = sum(shape)

  # Fill it up with numbers 1-n
  if n > 1:
    for i in range(2, n):
      # make list of potential empty squares: the ones that directly border filled up squares
      possible_squares = {}
      for j in range(len(shape)):
        for k in range(len(shape[i])):
          if tableau[i][j] == 0 and (tableau[i -1][j] or tableau[i][j-1] != 0):
            possible_squares.add(i, j)
      random_num = random.randint(0, len(possible_squares))
      possible_squares_list = list(possible_squares.items())
      chosen_square = possible_squares_list[random_num]
      tableau[chosen_square[0]][chosen_square[1]] = n

  return tuple(tableau)

random_SYT_2((2, 1))