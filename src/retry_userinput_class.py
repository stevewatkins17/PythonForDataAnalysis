# retry_userinput_class.py
import argparse

class UserInput:
    def __init__(self ,retry_count ,prompt ,possible_values = ["a" ,"b" ,"c"]):
        self.retry_count = retry_count
        self.prompt = prompt
        self.possible_values = possible_values

    def get_user_input(self):
        """follows pattern: MSSQL connection with retry"""
        v_result = self._validate_retry_count()

        if v_result == 0:
            for _ in range(self.retry_count):
                try:
                    print(f"Possible Answers: {self.possible_values}")
                    self.user_input = input(self.prompt)

                    if self.user_input not in self.possible_values:
                        raise ValueError()
                    else:
                        self.result = True
                except:
                    if _ < self.retry_count-1:
                        print(f"Fail: try again!!!!!")
                    continue
                else:
                    return self.result
            else:
                print(f"After {self.retry_count} attempts, failed to enter matching value")

    def _validate_retry_count(self):
        try:
            if not self.retry_count > 0:
                #raise 
                raise Exception("CRITICAL FAIL: retry count not > 0")
        except Exception as e:
            print(e)
            return 1
        else:
            return 0

