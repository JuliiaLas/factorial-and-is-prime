def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True 1
