DYNAMIC = "DYNAMIC"


class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        format_string = "{}, {} Typing, Reflection={}, First appeared in {}"
        return format_string.format(self.name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        return self.typing.upper() == DYNAMIC
