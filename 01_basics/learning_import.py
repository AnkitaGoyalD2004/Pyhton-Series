from basics import add

add(10, 20)

# .pyc extension means compiled python file -> compiled python files are generated when we import a module. It is generated to make the execution faster. and in this we have frozen binary code of python files. It is generated in __pycache__ folder. 
# __Pycache__ folder is generated when we import a module. It is generated to make the execution faster. and in this we have frozen binary code of python files. It is generated in __pycache__ folder.
# What actually happens behind the scenes:

 # 1. You write Python code in a .py file (human-readable).
 # 2. When you import or run that file, Python converts it into bytecode (computer-
 # friendly instructions) ending with .pyc.
 # 3. Python saves those .pyc files inside the __pycache__ folder.
 # 4. Next time you run your code, if the file hasn't changed, Python skips the
 # translation step and runs the bytecode directly.
