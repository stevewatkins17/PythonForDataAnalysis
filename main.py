#!/usr/bin/env python
import argparse
import sys
import src.retry_userinput_class as ruc

def main(prompt ,retry_count):
    """ this is the main function """
    myuserinput = ruc.UserInput(retry_count ,prompt)
    myuserinput.get_user_input()

    myuserinput.prompt = "True or False: The Louisville Cardinals RULE!!!"
    myuserinput.possible_values = ["True"]

    #myuserinput2 = ruc.UserInput(retry_count ,prompt ,possible_values)
    myuserinput.get_user_input()

    return 0

if __name__ == '__main__':
    """
    usage: python main.py -r 2 -p 'enter item from list: '
    """
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-p','--prompt'     ,type=str, required=True ,help='words presented to user')
    parser.add_argument('-r','--retry_count',type=int ,required=True ,help='retry count')

    args = parser.parse_args()

    #print(f"prompt: {args.prompt} ,retry_count: {args.retry_count}")

    main(args.prompt ,args.retry_count)
