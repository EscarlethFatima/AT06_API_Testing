# This function replace a specific word instead the old word given a word to replace


def replace(s, old, new):
    split = s.split(old)
    return new.join(split)


print(replace("Mississippi", "i", "I"))
song = "I love spom! Spom is my favorite food.Spom, spom, yum!"
print(replace(song, "om", "am"))
print(replace(song, "o", "a"))
