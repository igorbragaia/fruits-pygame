

class Command:

    # User Actions
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    SPACE = 4
    ESCAPE = 5

    def __init__(self, action) -> None:
        self.count = 0
        self.action = action

    def increment_count(self) -> None:
        self.count = self.count + 1

    def get_action(self) -> int:
        return self.action

    def get_count(self) -> int:
        return self.count


