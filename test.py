# Python Data Storage Demos Example 0: No Data Storage
# Basic setup for demos which show different ways to store program state (data)
# using standard and other Python libraries.  This example has no data storage
# and will always show default values when run.
#
# Author: Tony DiCola
# License: Public Domain


# Create a class to represent a person and their favorite color.
class Person(object):

    def __init__(self):
        # Set name and favorite color to defaults.
        self.name = 'No Name'
        self.favorite_color = 'Black'

    def load(self):
        # Attempt to load the person state from some file/storage system.
        # For now this is unimplemented!
        pass

    def save(self):
        # Attempt to save the person state to a file/storage system.
        # For now this is unimplemented!
        pass


# Main program which creates a person and prompts with a menu to change their
# name or favorite color.
if __name__ == '__main__':
    # Create a person instance and try to load any previous state.
    person = Person()
    person.load()
    # Now run in a loop and allow the name and color to be changed.
    while True:
        # Print out a menu of options.
        print('Hello {0}! Your favorite color is: {1}'.format(person.name, person.favorite_color))
        print('Options:')
        print(' 1 - Change name')
        print(' 2 - Change favorite color')
        print(' 3 - Quit')
        option = input('Enter option: ')
        # Check that the selected option is valid.
        if option not in ('1', '2', '3'):
            # Print an error and go back to the start of the loop.
            print('Unknown option!')
            continue
        if option == '1':
            # Change person's name.
            person.name = input('New name: ')
        elif option == '2':
            # Change person's favorite color:
            person.favorite_color = input('Favorite color: ')
        elif option == '3':
            # Break out of the loop to exit.
            print('Goodbye!')
            break
    # Once the main loop ends (by picking the quit option) save the person state.
    person.save()