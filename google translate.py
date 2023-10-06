from googletrans import Translator

def translate_to_sanskrit(text):
    translator = Translator()
    translated_text = translator.translate(text, src='en', dest='bn').text
    return translated_text

# Example usage
english_text = "Hello, how are you?"
sanskrit_translation = translate_to_sanskrit(english_text)
print("English: ", english_text)
print("Bengali: ", sanskrit_translation)
