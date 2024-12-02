from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["pikachu", "squirtle", "charmander"])
table.add_column("type", ["ellectric", "water", "fire"])
table.align = "r"
print(table)
