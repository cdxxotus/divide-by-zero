def bitwise_simulation_divide(numerator, denominator, precision=10):
    quotient = 0
    remainder = numerator
    num_bits = numerator.bit_length()

    # Integer division part
    for i in range(num_bits - 1, -1, -1):
        shifted_denominator = denominator << i
        if remainder >= shifted_denominator:
            remainder -= shifted_denominator
            quotient |= 1 << i

    # Handle fractional part
    fractional_part = 0.0
    remainder <<= 1  # Shift remainder to handle fractional part
    factor = 0.5  # Each bit in the fractional part corresponds to a power of 2

    for _ in range(precision):
        if remainder >= denominator:
            remainder -= denominator
            fractional_part += factor
        remainder <<= 1
        factor /= 2

    result = quotient + fractional_part
    return result

def generate_division_by_zero_table():
    results = []
    denominator = 0
    precision = 10000  # fixed precision for this example

    for numerator in range(101):  # 0 to 100
        result = bitwise_simulation_divide(numerator, denominator, precision)
        results.append(f"{numerator} divisé par {denominator} = {result}")

    return results

# Generate and print the division by 0 table
division_by_zero_table = generate_division_by_zero_table()
for line in division_by_zero_table:
    print(line)
