text = input("Input: ")
vowels = ["a","e","i","o","u"]
shortened = ""
for char in text:
    if char.lower() not in vowels:
        shortened += char
print(f"Output: {shortened}")
