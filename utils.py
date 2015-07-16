__author__ = 'Josh Fass'

def sign(x):
    ''' convenience function for cloning MATLAB code--
    convert positive/negative/zero's into +1,-1,0's '''
    return (x>0)-(x<0)
