# Using module 'collections', and class 'OrderedDict,
# with dictionary 'glossary_programming_terms'
# from, file 'dictionaries_glossary_programming_terms.py'

from collections import OrderedDict

glossary_programming_terms = OrderedDict()

glossary_programming_terms['boolean'] = 'true or false'
glossary_programming_terms['string'] = 'literal or word'
glossary_programming_terms['integer'] = 'whole number'
glossary_programming_terms['float'] = 'number with decimal'
glossary_programming_terms['conditional_statement'] = 'if else elif'

for term, glossary in glossary_programming_terms.items():
    print(term.title() + ": means " + glossary + ".")
