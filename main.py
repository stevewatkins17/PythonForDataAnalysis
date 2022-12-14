#!/usr/bin/env python
import argparse
import sys
import src.retry_userinput_demo as rud

def main():
    """this is the main function
    
    usage: python main.py -r 2 -p 'enter item from list: '
    """
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-p','--prompt'     ,type=str, required=True ,help='words presented to user')
    parser.add_argument('-r','--retry_count',type=int ,required=True ,help='retry count')

    args = parser.parse_args()

    print(f"prompt: {args.prompt} ,retry_count: {args.retry_count}")

    result = rud.main(args.prompt ,args.retry_count)

    return result

if __name__ == '__main__':
    main()