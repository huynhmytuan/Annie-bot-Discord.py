from googletrans import Translator

translator = Translator()
lang = translator.detect('이 문장은 한글로 쓰여졌습니다.').lang
print(lang)
