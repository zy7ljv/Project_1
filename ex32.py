the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

print(">>>>>>>> the_count", repr(the_count))

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what is in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = ['a', 'b']

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")

    print(">>>>> elements", repr(elements))

    # append is a function that lists understand
    elements.append(i)

print(">>>>> elements", repr(elements))

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")

print(f"THis is the list {elements}")
print("THis is the list again", elements)


