
from value.string import *

class Log:

    # log normal message to console
    @staticmethod
    def ln(msg: str) -> None:
        print(sslog + '[NOR] ' + msg)

    # log warning message to console
    @staticmethod
    def lw(msg: str) -> None:
        print(sslog + '[WAR] ' + msg)

    # log error message to console
    @staticmethod
    def le(msg: str) -> None:
        print(sslog + '[ERR] ' + msg)

