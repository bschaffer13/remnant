from interfaces.userInterface import UserInterface


class CliInterface(UserInterface):

    def send_message(self, message: str):
        print(message)

    def get_input(self, msg: str):
        return input('%s> ' % msg)
