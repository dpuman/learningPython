class InvalideOperationError(Exception):
    pass


class Streem:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalideOperationError("File already opened")

        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalideOperationError("File already Closed")

        self.opened = False


class FileStream(Streem):
    def read(self):
        print("Reading File")


class NetworkStream(Streem):
    def read(self):
        print("Reading Network")
