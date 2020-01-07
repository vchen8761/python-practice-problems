# def count_bits(x):
#     num_bits = 0
#     while x:
#         num_bits += x & 1
#         x >>= 1
#     return num_bits

# print(count_bits(92))

# def parity(x):
#     result = 0
#     while x:
#         result ^= 1
#         x &= (x-1)
#     return result

# print(parity(3))

# 4.4 Find the closest integer with the same weight
# Naive solution - try all numbers y > x and y < x
# def same_weight(x):
#     weight = count_bits(x)
#     change = 1
#     while(True):
#         if(count_bits(x+change) == weight):
#             return x+change
#         if(count_bits(x+(-1*change)) == weight):
#             return x+(-1*change)

# Time complexity of O(n) where n is the integer width 
# def same_weight(x):
#     NUM_UNSIGNED_BITS = 64
#     for i in range(NUM_UNSIGNED_BITS - 1):
#         if (x >> i) & 1 != (x >> (i + 1)) & 1:
#             x ^= (1 << i) | (1 << (i + 1)) #swaps bit-i and bit-(i+1)
#             return x
# print(same_weight(7))

# 4.7: x^y
# Naive solution
# def double_pow(x,y):
#     if (y == 0):
#         return 1
#     if (x == 0):
#         return 0
#     new_x = 1
#     for i in range(y):
#         new_x *= x
#     return new_x

# Recursive solution
# def recursive_pow(x,y):
#     result, power = 1.0, y
#     if y < 0:
#         power, x = -power, 1.0/x
#     while power:
#         if power & 1:
#             result *= x
#         x, power = x * x, power >> 1
#     return result

# print(recursive_pow(2.0,5))

# 4.8 Reverse int
# def reverse_int(x):
#     result, x_remaining = 0, abs(x)
#     while x_remaining:
#         result = result * 10 + x_remaining % 10
#         x_remaining //= 10
#     return -result if x < 0 else result

# print(reverse_int(1132))

# 5.1 Dutch Flag Partition
# def dutch_flag_partition(pivot_index, A):
#     pivot = A[pivot_index]
#     smaller, equal, larger = 0, 0, len(A)
#     while equal < larger:
#         if A[equal] < pivot:
#             A[smaller], A[equal] = A[equal], A[smaller]
#             smaller, equal = smaller + 1, equal + 1
#         elif A[equal] == pivot:
#             equal += 1
#         else:
#             larger -= 1
#             A[equal], A[larger] = A[larger], A[equal]
#     return A

# A = [-3, 0, -1, 1, 1, 2, 3, 1, 4, 2]
# print(dutch_flag_partition(1,A))
