# def perform_operation(num1 , num2, operation)
#     match: operation:
#         case:'add':
            
def perform_operation(num1: float, num2: float, operation: str) -> float:
  """
  Performs basic arithmetic operations based on the provided parameters.

  Args:
      num1: The first operand (float).
      num2: The second operand (float).
      operation: The operation to perform (string, must be 'add', 'subtract', 'multiply', or 'divide').

  Returns:
      The result of the arithmetic operation (float).
      A specific message ("Division by zero") if operation is 'divide' and num2 is zero.
  """
  operation = operation.lower()  # Ensure case-insensitive operation handling

  if operation == 'add':
    return num1 + num2
  elif operation == 'subtract':
    return num1 - num2
  elif operation == 'multiply':
    return num1 * num2
  elif operation == 'divide':
    if num2 == 0:
      return "Division by zero"
    else:
      return num1 / num2
  else:
    raise ValueError("Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide'.")






    