def main(array):
  if array == None or len(array) == 0:
    raise ValueError("Empty array")
  
  for i in array:
    if type(i) != int:
      raise ValueError("Non integer entry")
  
  largest = array[0]
  for i in range(1, len(array)):
    if array[i] > largest:
      largest = array[i]
  return largest