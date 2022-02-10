# 1 How to get a variable name as a string

def get_a_single_variable_name(**variable):
    '''
    For one variable
    Usage:
    name(variable_name=value)
    returns 'variabe_name'
    '''
    return [x for x in variable][0]

print(get_a_single_variable_name(any_function='any value'))
# any_function


# 2 How to get a variable name and value as a dictionary

def get_a_single_variable_name_and_value(**variable_value):
    '''
    For one variable
    Usage:
    name(variable_name=value)
    returns a dictionary:
    {'variable_name': value}
    '''
    return variable_value

print(get_a_single_variable_name_and_value(a_function='a value'))
# {'a_function': 'a value'}


# 3 How to get multiple variable names as a list of strings

def get_multiple_variable_names(**variables):
    '''
    For multiple variables
    Usage:
    name(variable1=value1, variable2=value2)
    returns ['variabe1', 'variable2']
    '''
    return [x for x in variables]

print(get_multiple_variable_names(first_function='first value', second_function='second_value'))
# ['first_function', 'second_function']


# 4 How to get multiple variable names and values as a dictionary

def get_multiple_variable_names_and_values(**variables):
    '''
    For multiple variables
    Usage:
    name(variable1=1, variable2=2)
    returns {'variable1': 1, 'variable2': 2}
    '''
    return variables

print(get_multiple_variable_names_and_values(first_function='first value', second_function='second_value'))
# {'first_function': 'first value', 'second_function': 'second_value'}
