# find_module.py
# given an input module name, we test its existence by importing it
# note this is an intientionally simple & immature script for demo purposes
import importlib ,argparse

def import_mod(module_name):
    try:
        target_module = importlib.import_module(module_name, package=None)
        return 0
    except ModuleNotFoundError as err:
        return 1

def main(module_name):
    try:
        target_module = importlib.import_module(module_name, package=None)
        print(f"pass - module exists: {module_name}")
    except ModuleNotFoundError as err:
        print(f"fail - module NOT exists: {module_name}")

if __name__ == '__main__':
    """
    usage: python main.py -r 2 -p 'enter item from list: '
    """
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-n','--namemodule'     ,type=str, required=True ,help='words presented to user')

    args = parser.parse_args()

    main(args.namemodule)
