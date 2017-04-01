class Currency:
    def __init__(self, name, abbreviation):
        self.name = name
        self.abb = abbreviation
        self.last_values = []

    def add_value(self, value):
        self.last_values.append(value)
