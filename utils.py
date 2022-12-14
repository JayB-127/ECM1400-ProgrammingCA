# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification


def sumvalues(values):
    """Receives a list/array, returning the sum of the values in that sequence.

    Keyword arguments:
        (List/Array) values: The list/array of values.
        
    Returns:
        (Int) sum: The sum of all the values.
        
    Raises:
        Exception: If list/array contains non-numerical values"""
    sum = 0
    #iterate through each item of list/array, checking type of each item
    for item in values:
        #if item is correct type, add item to sum
        if type(item) in [int, float, complex]:
            sum += item
        #if item is incorrect type, raise exception
        else:
            raise TypeError("All values in sequence must be numerical. Wrong data type given.")
    #return sum of all values in list/array
    return sum


def maxvalue(values):
    """Receives a list/array, returning the index of the maximum value in that sequence.
    
    Keyword arguments:
        (List/Array) values: The list/array of values.
        
    Returns:
        (Int) maxIndex: The index of the maximum value.
            
    Raises:
        Exception: If list/array contains non-numerical values"""
    maxIndex = 0
    max = values[0] #set maximum to first value in list/array
    i = 0
    #iterate i from 0 to length of list/array, checking type of item with index i
    while i < len(values):
        if type(values[i]) in [int, float, complex]:
            #if item is correct type, check item is greater than current max
            if values[i] > max:
                maxIndex = i
                max = values[i]
            i += 1
        #if item is incorrect type, raise exception
        else:
            raise TypeError("All values in sequence must be numerical. Wrong data type given.")
    #return index of maximum value in list/array
    return maxIndex


def minvalue(values):
    """Receives a list/array, returning the index of the minimum value in that sequence.

    Keyword arguments:
        (List/Array) values: The list/array of values.
        
    Returns:
        (Int) minIndex: The index of the minimum value.
            
    Raises:
        Exception: If list/array contains non-numerical values"""
    minIndex = 0
    min = values[0] #set minimum to first value in list/array
    i = 0
    #iterate i from 0 to length of list/array, checking type of item with index i
    while i < len(values):
        if type(values[i]) in [int, float, complex]:
            #if item is correct type, check item is less than current min
            if values[i] < min:
                minIndex = i
                min = values[i]
            i += 1
        #if item is incorrect type, raise exception
        else:
            raise TypeError("All values in sequence must be numerical. Wrong data type given.")
    #return index of minimum value in list/array
    return minIndex


def meannvalue(values):
    """Receives a list/array, returning the arithmetic mean value in that sequence.
    
    Keyword arguments:
        (List/Array) values: The list/array of values.
        
    Returns:
        (Float) mean: The mean value.
            
    Raises:
        Exception: If list/array contains non-numerical values"""    
    sum = 0
    #iterate through each item of list/array, checking type of each item
    for item in values:
        #if item is correct type, add item to sum
        if type(item) in [int, float, complex]:
            sum += item
        #if item is incorrect type, raise exception
        else:
            raise TypeError("All values in sequence must be numerical. Wrong data type given.")
    #calculate mean by dividing sum by amount of values in list/array, returning result
    mean = sum / len(values)
    return mean


def countvalue(values,x):
    """Receives a list/array values and a value x, returning the number of occurrences of the value x in that sequence.
    
    Keyword arguments:
        (List/Array) values: The list/array of values.
        (String) x: The value to find in the sequence.
        
    Returns:
        (Int) occurences: The amount of times x is present in the sequence."""
    occurences = 0
    #iterate through each item of list/array
    for item in values:
        #if item is equal to the value of x, increase occurence value by 1
        if item == x:
            occurences += 1
    #return amount of times the value of x is repeated in list/array
    return occurences