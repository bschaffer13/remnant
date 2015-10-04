communicator = None


def send_message(message: str):
    if communicator:
        communicator.send_message(message)


def get_message():
    if communicator:
        return communicator.get_message()