number = int(input("Enter a number: "))

is_palindrome = str(number) == str(number)[::-1]

digit_occurrences = {digit: str(number).count(digit) for digit in str(number)}

print("The number is a palindrome." if is_palindrome else "The number is not a palindrome.")
print("Digit occurrences:")
for digit, count in digit_occurrences.items():
    print(f"Digit {digit}: {count} occurrences")
print(digit_occurrences.items())