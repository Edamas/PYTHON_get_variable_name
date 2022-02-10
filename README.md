# PYTHON get variable name(s) (and values)

## In the Python's code you'll find these 4 functions to get:
- a single variable name
- a single variable name and it's value
- multiple variable names as a list
- multiple variable names and their values as a dictionary

Python's code: https://github.com/Edamas/PYTHON_get_variable_name/blob/main/get_variable_name_and_values.py
---------------------------------------------------------

### 1 How to get a variable name as a string

get_a_single_variable_name(any_function='any value')

Result:
any_function

---------------------------------------------------------

### 2 How to get a variable name and value as a dictionary

get_a_single_variable_name_and_value(a_function='a value')

Result:
{'a_function': 'a value'}

---------------------------------------------------------

# 3 How to get multiple variable names as a list of strings

get_multiple_variable_names(
                            first_function='first value', 
                            second_function='second_value'
                            )

Result:
['first_function', 'second_function']

---------------------------------------------------------

# 4 How to get multiple variable names and values as a dictionary
get_multiple_variable_names_and_values(
                                        first_function='first value', 
                                        second_function='second_value'
                                        )

Result:
{'first_function': 'first value', 'second_function': 'second_value'}

