""" 
if "__name__ == "__main__" in Python
    > this idiom is a comman pattern used in python script to determine whether the script is being run directly or being imported as a module into another script.
    > here __name__ variable is built-in variable that is automatically set to the name of the current module.
    > if python script run directly, the __name__variable is set to the string __main__
    > when script is imported as a module into another script, the __name__ variable is set to the name of the module.
"""

import prince
# prince.welcome()

""" 
IS IT A NECESSITY?
    > It's important to note that the if __name__ == "__main__" idiom is not required to run a Python script. 
    > You can still run a script without it by simply calling the functions or running the code you want to execute directly.
    > However, the if __name__ == "__main__" idiom can be a useful tool for organizing and separating code that should be run directly from code that should be imported and used as a module.
"""

""" 
jo je file banavi hoy emo j code run krvano hoy to __name__ == '__main__' lkhvani jrur nthee and jo e file ne import krvani hot to lkhi devu jruri he.
"""