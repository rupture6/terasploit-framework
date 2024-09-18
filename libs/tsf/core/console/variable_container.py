# GET Class
class Value(object):

    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

# SET Class
class set_user(Value):
    # prompt user
    def __set__(self, instance, value):
        self.value = value

class set_prompt(Value):
    # prompt
    def __set__(self, instance, value):
        self.value = value

class set_command_name(Value):
    # command name
    def __set__(self, instance, value):
        self.value = value

class set_command_parameter(Value):
    # command parameter
    def __set__(self, instance, value):
        self.value = value

class set_parameter_value(Value):
    # parameter value
    def __set__(self, instance, value):
        self.value = value

class set_options_value(Value):
    # options value
    def __set__(self, instance, value):
        self.value = value