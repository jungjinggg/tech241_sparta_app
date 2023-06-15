cool_things = ["Play Station", "Death Star lego", "car", "paint house", "private island"]
print(cool_things)
print(type(cool_things))

# First element
print(cool_things[0])

# Second element
print(cool_things[1])

# Last element
print(cool_things[-1])

# Replace items
cool_things[0] = "Xbox"
cool_things[-1] = "yacht"
print(cool_things)

# Add a new item
cool_things.append("massage chair")
print(cool_things)

# Remove items
print(cool_things.remove("car"))

cool_things.pop()
print(cool_things)