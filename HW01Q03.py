# These are the easy to change variables.
eggs_per_box = 6
eggs_per_omelette = 4
boxes_of_eggs = 6

# Now I calculate the total number of eggs.
total_eggs = eggs_per_box * boxes_of_eggs

# Then I calculate the number of omelettes dividing the total eggs by the n of eggs per omelette.
omelettes = total_eggs // eggs_per_omelette

# This is the output.
print(f'You can make {omelettes} omelettes with {boxes_of_eggs} boxes of eggs')
