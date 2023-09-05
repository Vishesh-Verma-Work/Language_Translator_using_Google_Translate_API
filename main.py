import googletrans
translator = googletrans.Translator()

# List of commonly used languages
common_languages = {
    1: 'en',  # English
    2: 'es',  # Spanish
    3: 'fr',  # French
    4: 'de',  # German
    5: 'it',  # Italian
    6: 'pt',  # Portuguese
    7: 'hi',  # Hindi
    8: 'ja',  # Japanese
    9: 'ko',  # Korean
    10: 'zh-cn'  # Chinese (Simplified)
}

print("Select the destination language here : ")
for key, value in common_languages.items():
    print(f"{key}: {googletrans.LANGUAGES[value]}")

choice = int(input("Enter the number of the destination language: "))
selected_language = common_languages.get(choice)

if selected_language:
    querry = input("Enter the text you want to translate: ")
    translation = translator.translate(querry, dest=selected_language)
    print(f"Translated text in {googletrans.LANGUAGES[selected_language]}: {translation.text}")
else:
    print("Invalid choice. Please select a valid language.")
