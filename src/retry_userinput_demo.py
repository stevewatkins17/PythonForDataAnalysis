# python retry_userinput_demo.py -r 2 -p 'enter item from list: '
import argparse

def get_user_input(prompt ,retry_count):
    """follows pattern: MSSQL connection with retry"""
    for _ in range(retry_count):
        try:
            possible_values = ["a" ,"b" ,"c"]
            print(possible_values)
            user_input = input(prompt)

            if user_input not in possible_values:
                raise ValueError()
            else:
                result = True
        except:
            if _ < retry_count-1:
                print(f"Fail: try again!!!!!")
            continue
        else:
            return result
    else:
        print(f"After {retry_count} attempts, failed to enter matching value")

def validate_retries(r):
    try:
        if not r > 0:
            #raise 
            raise Exception("CRITICAL FAIL: retry count not > 0")
    except Exception as e:
        print(e)
        return 1
    else:
        return 0

def main(prompt ,retry_count):
    result = get_user_input(prompt ,retry_count)

    if not result:
        print("Fail")
    else:
        """ we stub in a 'pass' msg in place of executing stmts"""
        print("Pass")

if __name__ == '__main__':
    """usage: python retry_userinput_demo.py -r 2 -p 'enter item from list: ' """
    parser = argparse.ArgumentParser(description='retry for input')

    parser.add_argument('-retries', type=int, default=3, required=True ,help="number of retries")
    parser.add_argument('-prompt', type=str, default=None, required=True ,help="message to prompt input")

    args = parser.parse_args()

    main(args.prompt ,args.retries)
