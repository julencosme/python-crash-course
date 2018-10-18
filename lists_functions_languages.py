languages = ['Chamorro', 'Tagalog', 'English', 'russian']
print(languages)

languages.append('Spanish')
print(languages)

languages.insert(0, 'Finish')
print(languages)

del languages[0]
print(languages)

popped_language = languages.pop(0)
print(languages)
print(popped_language)

popped_language = languages.pop(0)
print(languages)
print(popped_language)

languages.remove('English')
print(languages)

fluent_language = 'russian'
languages.remove(fluent_language)
print(languages)
print(fluent_language.title() + " is my fluent language.")
