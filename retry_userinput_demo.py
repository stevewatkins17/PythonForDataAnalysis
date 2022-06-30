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

prompt = "enter an existing possible value from above:"
retry_count = 3

result = get_user_input(prompt ,retry_count)

if not result:
    print("Fail")
else:
    """ we stub in a 'pass' msg in place of executing stmts"""
    print("Pass")

