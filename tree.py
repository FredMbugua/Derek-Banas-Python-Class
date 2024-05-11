#enter height of tree
tree_height = input("Enter height of tree: ")
#convert string to integer
tree_height = int(tree_height)
#space
space = tree_height - 1
#hash
hash = 1
#trunk_space
trunk_space = tree_height - 1
while (tree_height != 0):
#print the spaces
    for i in range(space):
        print(' ', end="")
    for i in range(hash):
        print('#', end='')
    #print new line
    print()
    space -= 1
    hash += 2
    tree_height -= 1
for i in range(trunk_space):
    print(" ", end="")
print("#")