def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

adjective1 = input("Pick a adjective: ")
adjective2 = input("Pick another adjective: ")
bird = input("Pick a bird: ")
verb1 = input("Pick a verb (past tense): ")
verb2 = input("Pick a verb: ")
pet = input("Pick a pet's name: ")
noun1 = input("Pick a noun: ")
liquid = input("Pick a liquid: ")
verb3 = input("Pick a verb ending in -ing: ")
body = input("Pick a part of the body (plural): ")
noun2 = input("Pick a plural noun: ")
verb4 = input("Pick a verb ending in -ing: ")
noun3 = input("Pick a noun:")

print("It was a " + (colored(26, 188, 156, adjective1)) + colored(170, 183, 184, (", cold January day. I")))
print(colored(170, 183, 184, "woke up to the") + (colored(26, 188, 156, adjective2)) + colored(170, 183, 184, ("smell of")) + colored(26, 188, 156, bird))
print(colored(170, 183, 184, "roasting in the") + (colored(26, 188, 156, verb1)) + colored(170, 183, 184,"down the stairs to see if I could"))
print(colored(170, 183, 184, "help") + colored(26, 188, 156, verb2) + colored(170, 183, 184,"the dinner. My wife said,"))
print(colored(170, 183, 184, "See if") + colored(26, 188, 156, pet) + colored(170, 183, 184, "needs a fresh") + colored(26, 188, 156, noun1),colored(170, 183, 184,". So I"))
print(colored(170, 183, 184, "carried a tray of glasses full of") + colored(26, 188, 156, liquid) +colored(170, 183, 184, "into"))
print(colored(170, 183, 184, "the") + colored(26, 188, 156, verb3) + colored(170, 183, 184,("room. When I got there, I")))
print(colored(170, 183, 184, "couldn't believe my") + colored(26, 188, 156, body) + colored(170, 183, 184,"! There were"))
print(colored(26,188,156,noun2) + colored(26,188,156,verb4) + colored(170,183,184,"on the") + colored(26,188,156,noun3) + colored(170,183,184,"!"))




























