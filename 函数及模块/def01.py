def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


# Print string;
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# Print;
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Print string;
print("We can even do math inside too:")
# print;
cheese_and_crackers(10 + 20, 5 + 6)

# Print;
print("And we can combine the tow, variables and math:")
# Print;
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
