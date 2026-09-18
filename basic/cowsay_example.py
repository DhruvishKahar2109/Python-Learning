import cowsay
import random

characters = cowsay.char_names

character = random.choice(characters)

print(cowsay.get_output_string(
    character,
    "Python is awesome!"
))