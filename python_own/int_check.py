#!/usr/bin/python3
x = int(input('please enter an integer: '))
if x < 0:
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('single')
elif x == 2:
    print('Double')
else:
    print('More')
