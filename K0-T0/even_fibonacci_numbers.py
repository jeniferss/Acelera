fibonacci_sequence = [1, 2]
current_number = fibonacci_sequence[-2]

while current_number < 4000000:
    current_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(current_number)

even_fibonacci_sequence = [number for number in fibonacci_sequence if number % 2 == 0]
even_fibonacci_sequence_sum = sum(even_fibonacci_sequence)
print(even_fibonacci_sequence_sum)
