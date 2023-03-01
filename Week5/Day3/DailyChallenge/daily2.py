from translate import Translator

translate = Translator(form_lang='french', to_lang='english')
french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 

type(translate.translate('Bienvenue'))

# word_translated = {}
# for word in french_words:
#     word_translated[translate.translate(word)] = word
# print(dict)