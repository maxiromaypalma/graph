from sys import exit
from graph.schema.schema import schema
from .cli import get_name, set_name, get_state, subscribe_to_state, subscribe_to_time_of_day

def run_repl():
    while True:
        print('>> ')
        print('>> ', end='')
        input_command = input()
        if input_command.startswith('help'):
            print('valid commands are:')
            print('===================')
            print('state')
            print('help')
            print('hello')
            print('set name <name>')
            print('delete name')
            print('subscribe time')
            print('subscribe state')
            print('exit')
            print('===================')
            continue
        if input_command.startswith('hello'):
            print('{}'.format(get_name()))
            continue
        if input_command.startswith('set name'):
            while True:
                name = input_command.split(" ")
                if len(name) == 3:
                    name = name[2]
                    break
                print('try again')
                print('>> ')
                print('>> ', end='')
                input_command = input()
            print('set name to {}'.format(set_name(name)))
            continue
        if input_command.startswith('delete name'):
            set_name(None)
            print('name deleted')
            continue
        if input_command.startswith('state'):
            print('{}'.format(get_state()))
            continue
        if input_command.startswith('subscribe time'):
            subscribe_to_time_of_day(schema)
            continue
        if input_command.startswith('subscribe state'):
            subscribe_to_state(schema)
            continue
        if input_command.startswith('exit'):
            exit(0)
        if input_command:
            print('invalid command')

if __name__ == '__main__':
    run_repl()

