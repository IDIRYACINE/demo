input_list = input("Enter a list of integers separated by spaces: ").split()

input_list = [int(num) for num in input_list]

if len(input_list) < 3:
    print("Error: Input list must contain at least three integers.")
    exit()

input_list.sort(reverse=True)

output_list = input_list[:3]

print("Three largest integers in the input list:", output_list)
