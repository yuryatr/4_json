import os
import json

def load_data(filepath):
    if os.path.exists(filepath):
        f = open(filepath, 'r')
        content = f.read()
        f.close()
        return json.loads(content)
    else:
        print('File not found: {}'.format(filepath))

def pretty_print_json(data, **kwargs):
    print( json.dumps(data, indent=4, ensure_ascii=False, **kwargs) )

def main():
    # The full path to the file.
    main_dir = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(main_dir, 'stores.json')

    # Keyboard Input data
    print('Enter the full path to the file (Example: "{}")'.format(filepath))
    filepath = input('> ')

    # To get data
    data = load_data(filepath)

    if data:
        # Output data
        pretty_print_json(data)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Force Quit')
    finally:
        pass
