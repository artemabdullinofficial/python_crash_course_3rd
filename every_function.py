languages = ['Python', 'JavaScript']
print(languages)

print(sorted(languages))  # Output: ['JavaScript', 'Python']
print(languages)  # Output: ['Python', 'JavaScript']

print(sorted(languages, reverse=True))  # Output: ['Python', 'JavaScript']
print(languages)  # Output: ['Python', 'JavaScript']

languages.reverse()
print(languages)  # Output: ['JavaScript', 'Python']

languages.reverse()
print(languages)  # Output: ['Python', 'JavaScript']

languages.sort()
print(languages)  # Output: ['JavaScript', 'Python']

languages.sort(reverse=True)
print(languages)  # Output: ['Python', 'JavaScript']

print(f"Number of programming languages in the list: {len(languages)}")  # Output: Number of programming languages in the list: 2



