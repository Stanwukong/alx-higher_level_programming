# 0x00. Python - Hello, World

## Learning Objectives :bookmark_tabs:
- Why Python programming is awesome
- Who created Python
- Where does the name ‘Python’ come from
- Who is Guido van Rossum
- What is the Zen of Python
- How to use the Python interpreter
- How to print text and variables using print
- How to use strings
- What are indexing and slicing in Python
- What is the official Python coding style and how to check your code with pycodestyle

## Tasks :page_with_curl:
### Mandatory
- [0-run](./0-run)
	- Write a Shell script that runs a Python script.
	- The Python file name will be saved in the environment variable `$PYFILE`

- [1-run_inline](./1-run_inline)
	- Write a Shell script that runs Python code.
	- The Python code will be saved in the environment variable `$PYCODE`

- [2-print.py](./2-print.py)
	- Write a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.
	- Use the function `print`

- [3-print_number.py](./3-print_number.py)
	- Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.
	- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py)
	- The output of the script should be:
		- the number, followed by `Battery street`,
		- followed by a new line
	- You are not allowed to cast the variable `number` into a string
	- Your code must be 3 lines long

- [4-print_float.py](./4-print_float.py)
	- Complete the [source code](https://github.com/alx-tools/0x00.py/blob/master/4-print_float.py) in order to print the float stored in the variable `number` with a precision of 2 digits.
		- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/4-print_float.py)
	- The output of the program should be:
		- `Float:`, followed by the float with only 2 digits
		- followed by a new line
	- You are not allowed to cast `number` to string

- [5-print_string.py](./5-print_string.py)
	- Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py) in order to print 3 times a string stored in the variable `str`, followed by its first 9 characters.
		- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py)
	- The output of the program should be:
		- 3 times the value of `str`
		- followed by a new line
		- followed by the 9 first characters of `str`
		- followed by a new line
	- You are not allowed to use any loops or conditional statement

- [6-concat.py](./6-concat.py)
	- Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/6-concat.py) to print `Welcome to Holberton School!`
		- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/6-concat.py)
	- You are not allowed to use any loops or conditional statements.
	- You have to use the variables `str1` and `str2` in your new line of code
	- Your program should be exactly 5 lines long

- [7-edges.py](./7-edges.py)
	- Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/7-edges.py)
		- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/7-edges.py)
	- You are not allowed to use any loops or conditional statements
	- Your program should be exactly 8 lines long
	- `word_first_3` should contain the first 3 letters of the variable `word`
	- `word_last_2` should contain the last 2 letters of the variable `word`
	- `middle_word` should contain the value of the variable `word` without the first and last letters

- [8-concat_edges.py](./8-concat_edges.py)
	- Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py) to print `object-oriented programming with Python`, followed by a new line.
		- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py)
	- You are not allowed to use any loops or conditional statements
	- Your program should be exactly 5 lines long
	- You are not allowed to create new variables
	- You are not allowed to use string literals

- [9-easter_egg.py](./9-easter_egg.py)
	- Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.
	- Your script should be maximum 98 characters long (please check with `wc -m 9-easter_egg.py`)

- [10-check_cycle.c](./10-check_cycle.c)
	- Write a function in C that checks if a singly linked list has a cycle in it.
	- Prototype: `int check_cycle(listint_t *list);`
	- Return: `0` if there is no cycle, `1` if there is a cycle
	- Requirements:
		- Only these functions are allowed: `write`, `printf`, `putchar`, `puts`, `malloc`, `free`
	- You are not allowed to use global variables
	- Your code must be compiled with the `-Wall -Werror -Wextra -pedantic` flags

### Advanced
- [100-write.py](./100-write.py)
	- Write a Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line.
	- Use the function `write` from the `sys` module
	- You are not allowed to use `print`
	- Your script should print to `stderr`
	- Your script should exit with the status code `1`
	- (Dora Korpar was a Holberton student in Cohort 0 of San Francisco)

- [101-compile](./101-compile)
	- Write a script that compiles a Python script file.
	- The Python file name will be stored in the environment variable `$PYFILE`
	- The output filename has to be `$PYFILEc` (ex: `export PYFILE=my_main.py` => output filename: `my_main.pyc`)
	- Requirements:
		- Only these functions are allowed: `print`, `open`, `exit`, `reload`, `compile`
		- You are not allowed to use `*` for importing or `__import__`
		- Your code should not be executed when imported
	- Tip: you have to use the Python `compile()` function

- [102-magic_calculation.py](./102-magic_calculation.py)
	- Write the Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:
		```
		3           0 LOAD_CONST               1 (98)
		            3 LOAD_FAST                0 (a)
		            6 LOAD_FAST                1 (b)
		            9 BINARY_POWER
		           10 BINARY_ADD
		           11 RETURN_VALUE
		```
	- Your code should be written at line 4 (`...`)
	- You are not allowed to use the `*` character
	- Your code should be maximum 4 lines long

