from sys import exit
from graph.schema.schema import schema
from .cli import get_name, set_name, get_state, subscribe_to_state, subscribe_to_time_of_day

def run_repl():
    while True:
        print('>> ')
        print('>> ', end='')
        input_command = input()
        if input_command == 'help':
            print('output: valid commands are:')
            print('output: ===================')
            print('output: state')
            print('output: help')
            print('output: hello')
            print('output: set name <name>')
            print('output: delete name')
            print('output: subscribe time')
            print('output: subscribe state')
            print('output: exit')
            print('output: ===================')
            continue
        if input_command == 'hello':
            print('output: {}'.format(get_name()))
            continue
        if input_command.startswith('set name'):
            while True:
                name = input_command.split(" ")
                if len(name) == 3:
                    name = name[2]
                    break
                print('output: try again')
                print('>> ')
                print('>> ', end='')
                input_command = input()
            print('output: set name to {}'.format(set_name(name)))
            continue
        if input_command.startswith('delete name'):
            set_name(None)
            print('output: name deleted')
            continue
        if input_command == 'state':
            print('output: {}'.format(get_state()))
            continue
        if input_command == 'subscribe time':
            subscribe_to_time_of_day(schema)
            continue
        if input_command == 'subscribe state':
            subscribe_to_state(schema)
            continue
        if input_command == 'exit':
            exit(0)
        if input_command:
            print('output: invalid command')

if __name__ == '__main__':
    run_repl()

