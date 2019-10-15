# Author:Mahtab Zilaie
# Date: 10-15-19
# Description: function that finds Fibonacci sequence

def fib(n):
    """Function finds Fibonacci sequence of n"""
    if n < 2:
        return n ==1
    else:
        return fib(n-2) + fib(n-1)