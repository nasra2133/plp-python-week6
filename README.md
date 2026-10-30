PLP Python Week 6 – Safe Tools

Files

- safe_tools.py: Contains three functions: safe_divide, safe_number, and get_field.
- README.md: Describes the assignment and explains how Python handles errors.

Question: Why can the if check not catch abc on its own?

An if statement checks whether a condition is true or false, but it does not catch errors. When Python tries to convert "abc" into an integer using int(), it raises a ValueError. The try/except block catches this error and prevents the program from crashing.