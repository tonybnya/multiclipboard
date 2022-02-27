import clipboard
import json
import sys


DB = 'clipboard.json'


def set_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f)


def get_data(file):
    try:
        with open(file) as f:
            data = json.load(f)
        return data
    except:
        return {}


if __name__ == '__main__':
    if len(sys.argv) == 2:
        data = get_data(DB)
        arg = sys.argv[1]

        if arg in ('--set', '-s'):
            key = input('Enter a key: ')
            data[key] = clipboard.paste()
            set_data(DB, data)
            print(f'Data saved! {data}')
        elif arg in ('--get', '-g'):
            key = input('Enter a key: ')
            data = get_data(DB)
            if key in data:
                clipboard.copy(data[key])
                print(f'Data copied to the clipboard! {data[key]}')
            else:
                print(f'{key} does not exist.')
        elif arg in ('--list', '-l'):
            data = get_data(DB)
            print(json.dumps(data, indent=1))
        else:
            print('Unknown argument.')
    else:
        print("Usage: 'python3 app.py {--set (-s) | --get (-g) | --list (-l)}'")
