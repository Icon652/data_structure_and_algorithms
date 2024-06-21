def find_first_occurrence(my_list, num):
    try:
        return my_list.index(num)
    except ValueError:
        return None

# Test the function
if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    num_to_find = 5
    print(find_first_occurrence(test_list, num_to_find))
