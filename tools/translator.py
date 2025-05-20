from googletrans import Translator

def translate_response(text, query):
    translator = Translator()
    try:
        target_lang = query.lower().split("to")[-1].strip()
        translated = translator.translate(str(text), dest=target_lang)
        return translated.text
    except Exception as e:
        return f"Translation error: {e}"