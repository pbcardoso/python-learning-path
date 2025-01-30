# A program that reads a person's birth year and displays a message indicating
# whether they can vote this year or not (not considering the month they were born).

born_year = int(input('What year were you born? '))
current_year = 2025

if current_year - born_year >= 16:
    print('\nYou can vote this year!')

else:
    print('\nYou cannot vote this year!')
    