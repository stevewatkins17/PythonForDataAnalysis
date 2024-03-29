Steps for Demonstrating Iterative Python Development with Git 

Creatio ex nihilo - we start with nothing.

We demonstrate how to:
- create a github repo
- create & run a Python test script
- create & run a Python script
- "giterate" that is, perform a basic code change iteration using git

# Step 0 - create repo "myhello"
- on Github
- on local file system 
> cd Downloads

# Step 1 - clone or pull repo "myhello"
from terminal or git bash:

> git clone https://github.com/stevewatkins17/myhello.git
> cd myhello
> ls

# Step 2 - create "test_hello.py" and "hello.py"
> touch test_hello.py
> touch hello.py

import hello
> python3 test_hello.py

# Step 3 - edit "hello.py"

print("Hello World!")

> python3 hello.py


# Step 4 - complete iteratation (add --> commit --> push)
git status
git add .
git commit -m "init commit hello.py - test success"
git push -u origin main

verify new files in github repo

# Step 5 - start new iteration --> git pull
> git pull origin main

# Step 6 - enhance "hello.py"
def print_hello():
    print("Hello World!")

def main():
    print_hello()

print("Special Hello World!")

if __name__ == '__main__':
    main()

# Step 7 - test enhancement with "test_hello.py"
> python3 test_hello.py
[fails!!]

import hello

hello.print_hello()

> python3 test_hello.py
[success]

# Step 8 - complete iteratation (add --> commit --> push)
git add .
git commit -m "enhance hello.py make FN - test success"
git push -u origin main

# Step 9 - start new iteration --> git pull
> git pull origin main

# Step 10 - iteration 3 "hello.py"
def print_msg(msg_txt):
    print(f"{msg_txt}")
    return 0

mymsg = "Hello World!"

return_code = print_msg(mymsg)

# Step 11 - test iteration 3 "test_hello.py"
> python3 test_hello.py
[FAIL]

import hello

return_code = hello.return_code

print(f"return_code:{return_code}")

> python3 test_hello.py
Hello World!
return_code:0

# Step 12 - complete iteration (add --> commit --> push)
git add .
git commit -m "enhance hello.py make FN with return - test success"
git push -u origin main

# Extras
## delete from local 
> rm -rf myhello
## restore
from terminal or git bash:

> git clone https://github.com/stevewatkins17/myhello.git
> cd myhello
> ls

