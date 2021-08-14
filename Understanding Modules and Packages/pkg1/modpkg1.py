varmodpkg1="variable inside modpkg1 in pkg1"
class A:
    var="variable in class A"

    __var="name mangling variable"  #__variablename are name mangling variables
    #this can't be called directly when this module is imported in other modules

    _var="this is private"#_variablename are private variables as for developers not to python
    #just a naming convection