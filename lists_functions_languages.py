# Every Function: Think of something you could store in a list . 
#
# For example, you could make a list of mountains,
# rivers, countries, cities, languages, or anything else you'd like .
#  
# Write a program that creates a list containing these items and then uses each
# function introduced in this chapter at least once .
#
# Functions used in this chapter: append(), insert(), del, pop(), remove(),
# sort(), sorted(reverse=True), reverse(), and len().

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