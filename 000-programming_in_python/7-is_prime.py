def is_prime(number):
    if number < 2:
        return False
    
    
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    
    return True
if __name__ == "__main__":
    test_number = 17
    print(is_prime(test_number))
