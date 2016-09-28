import os
import json
import argparse

def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as error:
        return error

def pretty_print_json(data, **kwargs):
    print( json.dumps(data, indent=4, ensure_ascii=False, **kwargs) )

def get_arguments():
    args = argparse.ArgumentParser()
    args.add_argument('--path', action='store', dest='filepath',
                        help='Path to json file you want to print.')
    return args.parse_args()

if __name__ == '__main__':
    try:
        arguments = get_arguments()
        data = load_data(arguments.filepath)
        if isinstance(data, (dict, list)):
            pretty_print_json(data)
        else:
            print(data)
    except KeyboardInterrupt:
        print('Force Quit')
    finally:
        pass
