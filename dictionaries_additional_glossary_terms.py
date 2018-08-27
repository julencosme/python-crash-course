# Glossary 2: Now that you know how to loop through a dictionary, clean up 
# the code from Exercise 6-3 (page 102) by replacing your series of print
# statements with a loop that runs through the dictionary’s keys and values.
#
# When you’re sure that your loop works, add five more Python terms to your 
# glossary.
#  
# When you run your program again, these new words and meanings should
# automatically be included in the output .

glossary_programming_terms = {
    'boolean': 'true or false',
    'string': 'literal or word',
    'integer': 'whole number',
    'float': 'number with decimal',
    'conditional_statement': 'if else elif',
}

for term in glossary_programming_terms.keys():
    print(term.title())

for term in glossary_programming_terms.values():
    print(term)


glossary_programming_terms = {
    'boolean': 'true or false',
    'string': 'literal or word',
    'integer': 'whole number',
    'float': 'number with decimal',
    'conditional_statement': 'if else elif',
    'list': 'sequence of values and is mutable',
    'tuple': 'sequence of values and is not mutable',
    'if_elif_else_chain': 'runs each conditional test in order until one passes',
    'if_else_statement': 'takes one aciton when a conditional test passes and a different action in all other cases',
    'if statement': 'simplest kind of if statement and has one test and one action',
}

for term in glossary_programming_terms.keys():
    print(term.title())

for term in glossary_programming_terms.values():
    print(term)
