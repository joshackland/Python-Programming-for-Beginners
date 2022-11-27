key_value_pairs = {}

while True:
    for k, v in key_value_pairs.items():
        print(f"key: {k}, value: {v}")

    key = input("Enter a key: ")
    value = input("Enter a value: ")

    key_value_pairs[key] = value