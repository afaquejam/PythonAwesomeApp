# Python App Source-Code Organization

## Assumptions
* You want to create an app called `AwesomeApp`.
* You want to organize your logically related code into libraries.
  - In pythonic terms, it means organizing your source-code in terms of packages (sub-packages to be precise), modules and classes.

## Recommendations
* Organize your code as found in this source-code repository.
* Don't use `__init__.py`. It's redundant after Python v3.3 (reference please).
* Don't update `sys.path` in-order to find your packages or modules. Simple imports, as found in this project's modules, shoudl work.
* However, it all depends on where you run your main program from. In this case, it's important to note that `awesomeapp` must be run from project's root directory. Also, the tests need to be run from the project's root directory. Why, you may ask! The reason being python's `sys.path` behavior. When you run a particular python script, then the script's location is added to `sys.path`. After this event, python's module finding rule kick's in, which searches the current directory for modules and packages and so-on.
