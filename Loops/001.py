"""Write a script to print out multiplication able of the user input
input: 2
2 * 1 = 2
....
2 * 12 = 24
"""

# collect input
user_input = int(input("What is your input:? "))
limit = 12


for i in range(1, limit + 1):
    result: int = user_input * i
    message: str = f"{user_input} x {i} = {result}"
    print(message)
