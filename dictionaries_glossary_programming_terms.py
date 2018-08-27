# Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary. 
# 
# Think of five # programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values. 
# 
# Print each word and its meaning as neatly formatted output. You might print
# the word followed by a colon and then its meaning, or print the word on one
# line and then print its meaning indented on a second line. Use the newline
# character(\n) to insert a blank line between each word-meaning pair in your
# output.

glossary_programming_terms = {
    'boolean': 'true or false',
    'string': 'literal or word',
    'integer': 'whole number',
    'float': 'number with decimal',
    'conditional_statement': 'if else elif',
}

print(glossary_programming_terms)

print("Boolean = " + glossary_programming_terms['boolean'])
print("String = " + glossary_programming_terms['string'])
print("Integer = " + glossary_programming_terms['integer'])
print("Float = " + glossary_programming_terms['float'])
print("Conditional Statements = " +
        glossary_programming_terms['conditional_statement'])

print("Boolean:" + "\n" + "\t" + glossary_programming_terms['boolean'])
print("\n")
print("String:" + "\n" + "\t" + glossary_programming_terms['string'])
print("\n")
print("Integer:" + "\n" + "\t" + glossary_programming_terms['integer'])
print("\n")
print("Float:" + "\n" + "\t" + glossary_programming_terms['float'])
print("\n")
print("Conditional Statement:" + "\n" + "\t" + glossary_programming_terms['conditional_statement'])
