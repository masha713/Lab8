first_string = input("Введіть перший рядок: ")
second_string = input("Введіть другий рядок: ")
common_chars = set(first_string) & set(second_string)
if common_chars:
    print("Спільні символи в обох рядках:", "".join(common_chars))
else:
    print("Спільних символів немає.")