def A():
    print('Hello')
def B():
    print('How are you')
def C():
    print('Hi')

x = input('Enter A,B, or C: ')

if x == 'A':
    A()
elif x == 'B':
    B()
elif x == 'C':
    C()
else:
    print('You did not input a correct option.')


#done