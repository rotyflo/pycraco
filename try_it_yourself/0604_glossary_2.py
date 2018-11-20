
# ADD 5 MORE TERMS
glossary = {
    'string': "a series of characters",
    'float': "any number with a decimal point",
    'list': "a collection of items in a particular order",
    'tuple': "an immutable list",
    'dictionary': "a collection of key-value pairs"
}

# ALREADY LOOPED THROUGH ITEMS IN 0603
for term, definition in glossary.items():
    print("\nA " + term + " is " + definition + ".\n")