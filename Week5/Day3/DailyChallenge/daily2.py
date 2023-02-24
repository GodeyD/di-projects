from translate import Translator

translate = Translator(form_lang='french', to_lang='english')
french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 

for word in french_words:
    dict [translate.translate(word)] = word
print(dict)