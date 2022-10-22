from scanner import Token, TokenType
from parser import Parser
from interpret import Interpreter
import pprint


token_print = Token(TokenType.PRINT, "print")
token_semi = Token(TokenType.SEMI, ";")
token_add = Token(TokenType.PLUS, "+")
token_mul = Token(TokenType.STAR, "*")
token_neg = Token(TokenType.MINUS, "-")
token_div = Token(TokenType.SLASH, "/")
token_num = lambda x: Token(TokenType.NUMBER, str(x))
token_semi = Token(TokenType.SEMI, ";")
token_var = Token(TokenType.VAR, "var")
token_identifier = lambda x: Token(TokenType.IDENTIFIER, x)
token_equal = Token(TokenType.EQUAL, "=")


def test_eval_expr():
    tokens = [
        token_neg,
        token_num(3),
        token_add,
        token_num(5),
        token_add,
        token_num(2),
        token_mul,
        token_num(10),
        token_div,
        token_neg,
        token_num(5)
    ]

    expr = Parser(tokens).expression()
    pprint.pprint(expr)

    Interpreter().evaluate(expr)


def test_execute_stmt():
    tokens = [
        token_print,
        token_neg,
        token_num(3),
        token_add,
        token_num(5),
        token_add,
        token_num(2),
        token_mul,
        token_num(10),
        token_div,
        token_neg,
        token_num(5),
        token_semi,

        token_print,
        token_num(5),
        token_semi,

        token_num(3),
        token_semi,
    ]

    tokens = [
        token_var,
        token_identifier("x"),
        token_equal,
        token_neg,
        token_num(3),
        token_add,
        token_num(5),
        token_add,
        token_num(2),
        token_mul,
        token_num(10),
        token_div,
        token_neg,
        token_num(5),
        token_semi,

        token_var,
        token_identifier("y"),
        token_equal,
        token_num(2),
        token_semi,
        
        token_print,
        token_identifier("y"),
        token_add,
        token_identifier("x"),
        token_semi,
    ]


    statements = Parser(tokens).parse()
    pprint.pprint(statements)
    
    Interpreter().interpret(statements)


# TODO: refactor so tokens, not chars, are stored in BinaryExpr
if __name__ == "__main__":
    test_execute_stmt()
