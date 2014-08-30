'''
Created on Apr 9, 2014

@author: rajni
'''
# Fibonacci series:
#the sum of two elements define the next
a, b=0, 1
while b < 10:
    print(b)
    a,b =b, a+b

    
def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint
        
ask_ok(a)