input_list = input("Enter a list of numbers separated by spaces: ").split()

input_list = [int(num) for num in input_list]

output_list = list(filter(lambda x: x % 2 == 0, input_list))

print("Even numbers in the input list:", output_list)
