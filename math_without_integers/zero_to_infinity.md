# Usage of each function

## zero_to_infinity.error()

### Usage

```python
zero_to_infinity.error(messege)
```

This code, when executed will stop your code with generic error messege, containing what you inputed to the function

### Complexity

O(1)

## zero_to_infinity.check_string()

### Usage

```python
zero_to_infinity.check_string(number)
```

This function checks if the string is a number, if it isn't it throws a generic error

### Complexity

O(1)

## zero_to_infinity.get_string()

### Usage

```python
zero_to_infinity.get_string(prompt)
```

This function works exactly like `input()`, but it checks the string with zero_to_infinity.check_string()

### Complexity

O(1)

## zero_to_infinity.count()

### Usage

```python
zero_to_infinity.count(number)
```

It creates a list of a size of inputed number, eg `['4', '3', '2', '1']` for "4" as a input

### Complexity

O(n), where n is how big the number is

## zero_to_infinity.add_one()

### Usage

```python
zero_to_infinity.add_one(number)
```

This function adds 1 to the inputed string.

### Complexity

O(1)

## zero_to_infinity.substract_one()

### Usage

```python
zero_to_infinity.substract_one(number)
```

This function substracts 1 from the inputed string, throws error when trying to substract from 0 (negative numbers are hard to implement)

### Complexity

O(1)

## zero_to_infinity.reverse()

### Usage

```python
zero_to_infinity.reverse(string)
```

This function reverses the inputed string.

### Complexity

O(1)

## zero_to_infinity.compare_bigger()

### Usage

```python
zero_to_infinity.compare_bigger(n1, n2)
```

This function takes 2 numbers and outputs the bigger one

### Complexity

O(min(n1, n2)), where n1 and n2 are the inputed numbers

## zero_to_infinity.compare_smaller()

### Usage

```python
zero_to_infinity.compare_bigger(n1, n2)
```

This function takes 2 numbers and outputs the smaller one

### Complexity

O(min(n1, n2)), where n1 and n2 are the inputed numbers

## zero_to_infinity.is_single_digit()

### Usage

```python
zero_to_infinity.is_single_digit(number)
```

This function takes any number and outputs `true` if it's a single digit number.

### Complexity

O(1)

## zero_to_infinity.add()

### Usage

```python
zero_to_infinity.add(n1, n2)
```

This function takes two numbers and adds them to eachother.

### Complexity

O(min(n1, n2)), where n1 and n2 are the inputed numbers

## zero_to_infinity.substract()

### Usage

```python
zero_to_infinity.substract(n1, n2)
```

This function takes two numbers and substracts second from the first one. Notably, your code will throw an error if you try to substract bigger number from smaller.

### Complexity

O(n2), where n2 is the second number

## zero_to_infinity.multiply()

### Usage

```python
zero_to_infinity.multiply(n1, n2)
```

This function multiplies 2 inputed numbers.

### Complexity

O(n1*n2), where n1 and n2 are the inputed numbers

## zero_to_infinity.divide()

### Usage

```python
zero_to_infinity.divide(n1, n2)
```

This function divides first number by the second number. Make sure the first number is divisible by the second one, else you might get an error

### Complexity

O(n1), where n1 is the first inputed number

## zero_to_infinity.safe_index()

### Usage

```python
zero_to_infinity.safe_index(number, index)
```

This function returns `number[index]` or "0", so you won't get any index errors.

### Complexity

O(1)

## zero_to_infinity.add_optimized()

### Usage

```python
zero_to_infinity.add(n1, n2)
```

This function takes two numbers and adds them to eachother. It's much faster than `add()`

### Complexity

O(d), where d = max(len(n1), len(n2))

## zero_to_infinity.substract_optimized()

### Usage

```python
zero_to_infinity.substract_optimized(n1, n2)
```

This function takes two numbers and substracts second from the first one. Notably, your code will throw an error if you try to substract bigger number from smaller. It's much faster than `substract()`

### Complexity

O(d), where d = max(len(n1), len(n2))

## zero_to_infinity.multiply_optimized()

### Usage

```python
zero_to_infinity.multiply_optimized(n1, n2)
```

This function multiplies 2 inputed numbers. It's much faster than `multiply()`

### Complexity

`O(d1*d2*d_result)`, where d1 and d2 are lengths of input numbers and d_result is length of the result (which is around d1 + d2)

## zero_to_infinity.power()

### Usage

```python
zero_to_infinity.power(n1, n2)
```

n1 is a base, n2 is an exponent. This function can get quite slow for massive numbers.

### Complexity

`O(n2*d1*d2*d_result)`, where n2 is the value of n2, d1 and d2 are lengths of input numbers and d_result is length of the result (which is around d1 + d2)

## zero_to_infinity.factorial()

### Usage

```python
zero_to_infinity.factorial(number)
```

Returns the factorial of the number, this function gets really slow for big numbers

### Complexity

`O(n*d*d*d_result)`, where n is the value of number, d is the length of it numbers and d_result is length of the result