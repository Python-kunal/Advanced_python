numbers = [1, 2, 3, 4, 5]

squares = [numbers ** 2 for numbers in numbers]
print(squares)

#next question:--

words = ["hello", "python", "coder"]

capitaliZed = [words.upper() for words in words]
print(capitaliZed)


#next question:--

rangeofnumbers = range(1, 21)

even = [numbers for numbers in rangeofnumbers if numbers % 2 == 0]
print(even)


#next question:--

nums = [10, 15, 20, 25,]

evenodd = ["even" if nums % 2 == 0 else "odd" for nums in nums]
print(evenodd)


#next question:--

