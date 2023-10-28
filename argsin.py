# print() functions are called as scaffolding and may be commented out



def argsin_returnback(a, b, c) :

  print(f"\nPrint statements of variable values are scaffolding in the function.\n")

  print(f"Inside argsin_returnback() variable a's value: {a}")

  print(f"Inside argsin_returnback() variable b's value: {b}")

  print(f"Inside argsin_returnback() variable c's value: {c}")

  print("Those^ came from the arguments in to argsin_returnback()")

  # So far all that has happened is arguments came in and were printed



  # The following code creates local variables and assigns them values

  x = 7

  y = 12.0

  z = 100

  print("The following come from assignments in argsin_returnback()")

  print(f"Inside argsin_returnback() variable x's value: {x}")

  print(f"Inside argsin_returnback() variable y's value: {y}")

  print(f"Inside argsin_returnback() variable z's value: {z}")



  # The following code ends the function and returns two values (y and x)

  return y, x



# Main program code follows



print(f"\n\nInvoking argsin_returnback() with arguments: ('Hello', [1,2,3], 2021)\n{argsin_returnback('Hello', [1,2,3], 2021)}")
