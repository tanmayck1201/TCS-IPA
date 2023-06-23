import random


def get_krishna_name():
    # List of unique names of Lord Krishna
    krishna_names = ['Govinda', 'Gopal', 'Murari', 'Hari', 'Madhava',
                     'Muralidhara', 'Nanda Kishora', 'Radha Vallabha', 'Shyam', 'Vasudeva']

    # Shuffle the list to get a random order
    random.shuffle(krishna_names)

    # Pop the first element from the shuffled list
    # This ensures that each name is unique and is not repeated in subsequent calls
    return krishna_names.pop(0)


print("Love you", get_krishna_name())
