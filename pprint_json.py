import os
import json


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as file_handler:
        return json.load(file_handler)


def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    print("Enter the path to the json file")
    file_name = load_data(input())
    pretty_print_json(file_name)
