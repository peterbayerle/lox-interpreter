from collections import namedtuple
from enum import Enum


class TokenType(Enum):
    NUMBER = "number"
    PLUS = "plus"
    MINUS = "minus"
    STAR = "star"
    SLASH = "slash"
    PRINT = "print"
    SEMI = "semicolon"
    VAR = "var"
    EQUAL = "equal"
    IDENTIFIER = "identifier"

    
Token = namedtuple("Token", ["type", "value"])
