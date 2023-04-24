class Mood():
    """learning how to create a new Python object based on the Mood class"""

    # Class initializer. It has 2 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, label):
        self.id = id
        self.label = label
