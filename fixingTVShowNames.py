import os

def rename(name):
    # episode changing
    name = name.replace('Episode ', 'E', 1)
    name = name.replace('Episode', 'E', 1)
    name = name.replace('episode ', 'E', 1)
    name = name.replace('episode', 'E', 1)

    # season changing
    name = name.replace('Season ', 'S', 1)
    name = name.replace('Season', 'S', 1)
    name = name.replace('season ', 'S', 1)
    name = name.replace('season', 'S', 1)

    return name

print('Running!')

# os.walk() should have name of outer directory in it
for root, directories, files in os.walk('F:/TV Shows'):
    print('Entered TV Shows')
    for directory in directories:
        if 'Episode ' or 'Season ' in directory:
            newName = rename(directory)
            print('Old name:', directory)
            print('New name:', newName)
            os.rename(os.path.join(root, directory), os.path.join(root, newName))
            print('')

    for file in files:
        if 'Episode ' or 'Season ' in file:
            newName = rename(file)
            print('Old name:', file)
            print('New name:', newName)
            os.rename(os.path.join(root, file), os.path.join(root, newName))
            print('')
