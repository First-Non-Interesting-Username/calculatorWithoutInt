# General usage tips

- Remember to not input actual numbers, you can use `zero_to_nine.check_string()` to check if input is a elegible number.
- When taking inputs from user, you should use `zero_to_nine.get_string()` or at least check the string before using it in the code.
- This is an early version of the library. It's reccommended to use zero_to_infinity version.

## [Example program](example_zero_to_nine.py)

# Usage of each function

## Terminology

Number - string representing a number

d (in case of complexity calculations) - length


## zero_to_nine.error()

### Usage

```python
zero_to_nine.error(messege)
```

This code, when executed will stop your code with generic error messege, containing what you inputed to the function

### Complexity

O(1)

## zero_to_nine.check_string()

### Usage

```python
zero_to_nine.check_string(number)
```

This function checks if the string is a number, if it isn't it throws a generic error

### Complexity

O(1)

## zero_to_nine.get_string()

### Usage

```python
zero_to_nine.get_string(prompt)
```

This function works exactly like `input()`, but it checks the string with zero_to_nine.check_string()

### Complexity

O(1)

## zero_to_nine.add_one()

### Usage

```python
zero_to_nine.add_one(number)
```

This function adds 1 to the inputed string, throws error when trying to add to 9

### Complexity

O(1)

## zero_to_nine.substract_one()

### Usage

```python
zero_to_nine.substract_one(number)
```

This function substracts 1 from the inputed string, throws error when trying to substract from 0 (negative numbers are hard)

### Complexity

O(1)

## zero_to_nine.count()

### Usage

```python
zero_to_nine.count(number)
```

It creates a list of a size of inputed number, eg `['3', '2', '1', '0']` for "4" as a input

### Complexity

O(n), where n is how big the number is

## zero_to_nine.compare_bigger()

### Usage

```python
zero_to_nine.compare_bigger(n1, n2)
```

This function takes 2 numbers and outputs the bigger one

### Complexity

O(min(n1, n2)), where n1 and n2 are the inputed numbers

## zero_to_nine.compare_smaller()

### Usage

```python
zero_to_nine.compare_bigger(n1, n2)
```

This function takes 2 numbers and outputs the smaller one

### Complexity

O(min(n1, n2)), where n1 and n2 are the inputed numbers

## zero_to_nine.add()

### Usage

```python
zero_to_nine.add(n1, n2)
```

This function takes two numbers and adds them to eachother.

### Complexity

O(min(n1, n2)), where n1 and n2 are the inputed numbers

## zero_to_nine.substract()

### Usage

```python
zero_to_nine.substract(n1, n2)
```

This function takes two numbers and substracts second from the first one. Notably, your code will throw an error if you try to substract bigger number from smaller.

### Complexity

O(n2), where n2 is the second number

## zero_to_nine.multiply()

### Usage

```python
zero_to_nine.multiply(n1, n2)
```

This function multiplies 2 inputed numbers. Remember that the result can't exceed 9 or you will get an error.

### Complexity

O(n1*n2), where n1 and n2 are the inputed numbers

## zero_to_nine.divide()

### Usage

```python
zero_to_nine.divide(n1, n2)
```

This function divides first number by the second number. Make sure the first number is divisible by the second one, else you might get an error

### Complexity

O(n1), where n1 is the first inputed number
