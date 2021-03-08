from .time.time import current
class ylist():
    @staticmethod
    def year() -> list:
        new = []
        for i in range(1, 4):
            new.append(int(current()) - i)
        return new
