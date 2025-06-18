#  1. Iterator
# An iterator is an object which implements two methods:

# __iter__() → returns the iterator object itself

# __next__() → returns the next value from the sequence, and raises StopIteration when the items are exhausted
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

counter = Counter(1, 5)

for num in counter:
    print(num)


#  2. Generator
# A generator is a special type of iterator that is defined using a function with the yield keyword. It automatically saves state between yields and resumes where it left off.
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

gen = count_up_to(5)

for num in gen:
    print(num)

# Differences: Iterator vs Generator
# Feature	Iterator Class	Generator Function
# Syntax	Needs __iter__ and __next__	Uses yield inside a function
# Code Length	More verbose	More concise
# State Handling	Manually managed	Automatically handled by Python
# Use Case	Fine-grained control	Simpler iteration

def read_large_file_line_by_line(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

# Usage
for line in read_large_file_line_by_line('bigfile.txt'):
    print(line)

# This avoids loading the entire file into memory, unlike reading all lines at once.
