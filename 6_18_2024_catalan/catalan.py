import itertools
import random

def parenthesizations(n):
  """
  Returns a list of all possible parenthesizations of length n.

  Parameters:
    n (int): The length of the parenthesizations.

  Returns:
    A list of strings, where each inner string represents a valid parenthesization of length n.

  Example:
  >>> parenthesizations(3)
  {'((()))', '(()())', '(())()', '()(())', '()()()'}
  """

  def generate_helper(open_count, close_count, current_string):
      if open_count == 0 and close_count == 0:
          result.append(current_string)
          return
      if open_count > 0:
          generate_helper(open_count - 1, close_count, current_string + '(')
      if close_count > open_count:
          generate_helper(open_count, close_count - 1, current_string + ')')
  result = []
  generate_helper(n, n, '')
  return set(result)

def product_orders(n):
  """
  Returns a list of all possible ways to multiply of n elements.

  Parameters:
    n (int): The number of elements multiplied.

  Returns:
    A set of strings where each string represents a way to multiply n elements.

  Example:
  >>> product_orders(4)
  {'((?*?)*?)*?', '(?*(?*?))*?', '(?*?)*(?*?)', '?*((?*?)*?)', '?*(?*(?*?))'}
  """
  def product_orders_helper(n, original_n, current_string, open_count, close_count):
    if open_count + close_count == original_n:
        result.append(current_string)
    if n == 1:
      return "?"
    elif n == 2:
      return "?*?"
    else:
      for i in range(1,n):
        if i != 1:
          current_string = current_string +  "("
          open_count = open_count + 1
        current_string = current_string + product_orders_helper(i, n, open_count, close_count, current_string) +  "*"
        if n - 1 != 1:
          close_count = close_count + 1
        current_string = current_string + product_orders_helper(n-i, n, open_count, close_count, current_string)
        if n - i != 1:
          current_string = current_string + ")"
        return current_string


  result = []
  product_orders_helper(n, n, "", 0, 0)
  return result

def permutations_avoiding_231(n):
  """
  Returns a list of permutations of length n avoiding the pattern 2-3-1.

  Parameters:
    n (int): The length of the permutation.

  Returns:
    A list of permutations of length n that do not contain the pattern 2-3-1.

  Example:
  >>> permutations_avoiding_231(4)
  {(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (3, 1, 2, 4), (3, 2, 1, 4), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 3, 1, 2), (4, 3, 2, 1)}
  """
  permutation_set = set(itertools.permutations(range(1, n+1)))
  permutations_avoiding = set()
  if n < 3:
    return permutation_set
  else:
    for permutation in permutation_set:
      p = True
      for i in range(1, n - 2):
        for j in range(i + 1, n - 1):
          for k in range(i+2, n):
            if permutation[i] < permutation[j] and permutation[j] < permutation[k] and permutation[i] > permutation[k]:
              p = False
      if p:
        permutations_avoiding.add(permutation)
    return permutations_avoiding




def triangulations(n):
  """
  Returns a list of all possible triangulations of an n-sided polygon. A triangulation
  is represented as a list of internal edges. Vertices are labeled 0 through n-1 clockwise.

  Parameters:
    n (int): The number of sides of the polygon.

  Returns:
    A set of tuple of pairs, where each pair represents an internal edge in the triangulation.

  Example:
  >>> triangulations(3)
  {((0, 3), (1, 3)), ((1, 4), (2, 4)), ((1, 3), (1, 4)), ((0, 2), (2, 4)), ((0, 2), (0, 3))}
  """

  def triangulations_helper(n, triangulation):
    if len(triangulation) == n - 3:
      result.add(triangulation)
    elif n > 3:
      edge_1 = 0
      for edge_2 in range(1,n):
        if abs(edge_1 - edge_2) < 1:
          edge_1 = 1
          edge_2 = n -1

      triangulation.add("(" + str(edge_1) + ", " + str(edge_2) + ")")
      # Recurse first part of the polygon
      n = (edge_2 - edge_1) % n + 1
      triangulations_helper(n, triangulation)
      # Recurse second part of the polygon
      n = (edge_1 - edge_2) % n + 1
      triangulations_helper(n, triangulation)

  if n < 3:
    return set()
  elif n == 3:
    return {tuple()}
  else:
    result = set()
    triangulations_helper(n, set())


