
def sum_even_numbers(my_list):
    return sum(num for num in my_list if num % 2 == 0)

# If we put a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_even_numbers(my_list))  
