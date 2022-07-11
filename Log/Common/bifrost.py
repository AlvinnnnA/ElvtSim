class Reporter:
    def __init__(self):
        pass

    @classmethod
    def warning(self, *args):
        print("Warning", args)

    @classmethod
    def debug(self, *args):
        print("Warning", args)