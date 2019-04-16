cool_languages = ['japanese', 'german', 'spanish', 'chinese', 'french', 'icelandic']

print(cool_languages[-1])

cool_languages.append('korean')
print(cool_languages)

cool_languages.insert(2, 'latin')
print(cool_languages)

del cool_languages[2]
print(cool_languages)

best_language = cool_languages.pop(0)
print(best_language)
print(cool_languages)

cool_languages.remove('korean')
print(cool_languages)

print(sorted(cool_languages))
print(cool_languages)

print(sorted(cool_languages, reverse=True))
print(cool_languages)

cool_languages.reverse()
print(cool_languages)

cool_languages.sort(reverse=True)
print(cool_languages)

print(len(cool_languages))