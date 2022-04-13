# Write an anonymous functio in that sorts this list by the last name...
# Hint: Use the ".sort()" method and access the key"
# .sort(key=)
authors = ["Connor Milliken", "Victor aNisimov", "Andrew P. Garfield", "David HassELHOFF", "Oprah wInfrey"]
sorted_authors = sorted(authors, key=lambda x: x.split()[-1])
# for n in sorted(authors, key=lambda x: x[-1]):
print(sorted_authors)

