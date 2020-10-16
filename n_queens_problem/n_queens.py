'''
@author : jhhalls
'''

def n_queens(n):

	""" Python3 program to solve N Queen Problem
	 using backtracking """

    sol=0
    cols = range(n)
    for combo in permutations(cols):
        if n == len(set(combo[i] + i for i in cols)) 
        == len(set(combo[i]-i for i in cols )):
            sol+=1
            print('solution' + str(sol) + ': '+str(combo)+'\n')
            print('\n'.join(' o '*i +' X '+' o '*(n-i-1) for i in (combo))) 
