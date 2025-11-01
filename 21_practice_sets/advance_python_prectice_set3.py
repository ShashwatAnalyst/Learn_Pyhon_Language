# 8.
    # Use the walrus operator to read input until the user enters "quit". Print each input as it is entered.
    # Use the walrus operator in a list comprehension to store lengths of words from ["python", "rocks", "ai"] in a list while filtering out words shorter than 4 characters.


while (i := input("Enter something: ")) != "python":
    print(f"You entered {i}")

l = ["python", "rocks", "ai"]

lenl = [a for i in l if (a := len(i)) >= 4]

print(lenl)