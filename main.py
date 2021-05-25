  
import string
alpha = string.ascii_lowercase

def print_rangoli(size):
    lst1 = []
    for row in range(size):
        to_print = "-".join(alpha[row:size])
        lst1.append(to_print[::-1] + to_print[1:])
    width = len(lst1[0])
    
    for row in range(size-1, 0, -1):
        print(lst1[row].center(width, '-'))
        
    for row in range(size):
        print(lst1[row].center(width, '-'))


print(print_rangoli(32))