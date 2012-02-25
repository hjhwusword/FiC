

def checkRange(value, beginInclusive, endExclusive):
    if value < beginInclusive or value >= endExclusive :
        raise ValueError('"' + str(value) + '" is not between [' + str(beginInclusive) + ', '\
                         + str(endExclusive) + ')')
    
def checkInstanceInt(integer):
    if(not isinstance(integer,int)) :
        raise TypeError('"' + str(integer) + '" is not an integer')
    
def checkInstanceNonnegInt(integer):
    checkInstanceInt(integer)
    if(integer < 0) :
        raise TypeError('"' + str(integer) + '" is not a non negative integer')


def checkInstancePosInt(integer):
    checkInstanceInt(integer)
    if(integer <= 0) :
        raise TypeError('"' + str(integer) + '" is not a positive integer')    

def checkInstanceString(string):
    if(not isinstance(string, str)):
        raise TypeError('"' + str(string) + '" is not a string')
    
def checkInstanceBool(boolean):
    if(not isinstance(boolean,bool)) :
        raise TypeError('"' + str(boolean) + '" is not a boolean')