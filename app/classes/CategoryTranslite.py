import json
from transliterate import translit

class CategoryTranslite:
    #Класс для управления именем категории. Наиболее часто нужно для того, чтобы обрабатывать имя категории
    @staticmethod
    def CleanCat(categoryName): # транслит и замена пробела на -
        # Check if the URL ends with ".jpg"
        latin_text = translit(categoryName, 'ru', reversed=True)
        latin_text = latin_text.replace(" ","-")
        return latin_text
