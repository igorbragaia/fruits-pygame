from fruits.controllers.controller import Controller
from fruits.command import Command


class FruitController(Controller):

    def __init__(self, fruit_entity):
        super(FruitController, self).__init__(fruit_entity)
        self.events = [Command.LEFT_START, Command.RIGHT_START,
                       Command.SPACE_START]

    @property
    def listening_events(self):
        return self.events

    def receive(self, command):
        if command == Command.LEFT_START:
            self.entity.update(horizontal=-4)
        if command == Command.RIGHT_START:
            self.entity.update(horizontal=4)
        if command == Command.SPACE_START:
            self.entity.update(vertical=-20)