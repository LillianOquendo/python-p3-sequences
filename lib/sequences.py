#!/usr/bin/env python3

#adding the laste two numbers to the left and building up to length
 #if length is 1 then print outputs 0
 #if length is 2 then print outputs [0,1]
 #you need to use the .append method to add to the end of your sequence 
 # we need to subtract 2 from your initial integer and subtract 1 from our secondary integer
def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0, 1])
    else:
        fibonacci_sequence = [0, 1]
        for n in range(2, length):
            next_number = fibonacci_sequence[n-1] + fibonacci_sequence[n-2]
            fibonacci_sequence.append(next_number)
        print(fibonacci_sequence)

