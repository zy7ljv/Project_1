from sys import argv

script, filename = argv

file = input(">")

txt = open(file)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input(">")

tax_again = open(file_again)

print(tax_again.read())

