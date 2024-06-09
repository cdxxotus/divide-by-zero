def bitwise_simulation_divide(numerator, denominator, precision=10):
    if denominator == 0:
        print("Indéfini (Division par zéro)")

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

def main():
    numerator = 42  # Numerator is fixed at 42

    while True:
        try:
            denominator_input = input("Veuillez entrer le dénominateur: ")
            denominator = int(denominator_input)
            break
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entier.")

    while True:
        try:
            precision_input = input("Veuillez entrer la précision (nombre de décimales): ")
            precision = int(precision_input)
            if precision < 0:
                raise ValueError("La précision doit être un nombre entier positif.")
            break
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entier positif.")

    result = bitwise_simulation_divide(numerator, denominator, precision)
    print(f"Résultat de la division bitwise avec précision: {result}")

if __name__ == "__main__":
    main()
