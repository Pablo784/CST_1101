numbers = [1,2,3,4,5]

for medieval_times in range(len(numbers)):

  print("Original value: ", numbers[medieval_times], "at index# ", medieval_times)

  numbers[medieval_times] = numbers[medieval_times]**2

  print("New value: ", numbers[medieval_times], "at index# ", medieval_times)

  print()
