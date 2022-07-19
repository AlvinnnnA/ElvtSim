class Reporter:
    def __init__(self):
        pass

    @classmethod
    def warning(self, *args):
        print("Warning", args)

    @classmethod
    def debug(self, *args):
        print("Debug", args)


class Chime:
    def __init__(self):
        pass

    @classmethod
    def warning(self, *args):
        print("Warning", args)

    @classmethod
    def debug(self, *args):
        print("Debug", args)

    @classmethod
    def info(self, *args):
        print("Info", args)

    @classmethod
    def error(self, *args):
        print("Error", args)

    @classmethod
    def critical(self, *args):
        print("Critical", args)