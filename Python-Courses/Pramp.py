def array_of_array_products(arr):
    
  result = []
  for i in range(len(arr)):
    a = arr[:i] + arr[i+1:]
    m = 1
    for element in a:
      m = m * element
    result.append(m)
  return result

def array_of_array_products_1(arr):
  result = []
  for i in range(len(arr)):
      pass


if __name__ == "__main__":

    arr = [2] #, 7] #, 3, 4]
    r = array_of_array_products(arr)
    print(r)