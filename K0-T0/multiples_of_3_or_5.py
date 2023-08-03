numbers = [number for number in range(1, 1000) if number % 3 == 0 or number % 5 == 0]
sum_of_multiples_of_3_or_5_bellow_1000 = sum(numbers)
print(sum_of_multiples_of_3_or_5_bellow_1000)
