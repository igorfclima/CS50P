def convert(text):
    faces = {
        ":)": "🙂",
        ":(": "🙁",
        ":|": "😐"
    }
    for key, value in faces.items():
        text = text.replace(key, value)
    return text

def main():
    text = input("Enter your text: ")
    print(convert(text))

main()
