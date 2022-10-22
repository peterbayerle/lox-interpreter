from dataclasses import dataclass

from scanner import TokenType, Token


@dataclass
class ExpressionStmt:
    expression: "Expr"

    def accept(self, visitor):
        return visitor.visitExpressionStmt(self)

    
@dataclass
class PrintStmt:
    expression: "Expr"

    def accept(self, visitor):
        return visitor.visitPrintStmt(self)

    
@dataclass
class VariableStmt:
    name: str # variable name
    expression: "Expr" # variable value

    def accept(self, visitor):
        return visitor.visitVariableStmt(self)

    
@dataclass
class Expr:
    value: "Expr"

    
@dataclass
class Primary(Expr):
    value: str # literal value
    def accept(self, visitor):
        return visitor.visitPrimary(self)


@dataclass
class Variable(Expr):
    value: str # name of variable

    def accept(self, visitor):
        return visitor.visitVariable(self)

    
@dataclass
class Binary(Expr):
    value: str # operator
    lhs: Expr
    rhs: Expr

    def accept(self, visitor):
        return visitor.visitBinary(self)
    

@dataclass
class Unary(Expr):
    value: str #operator
    rhs: Expr

    def accept(self, visitor):
        return visitor.visitUnary(self)
    

class Parser:
    def __init__(self, tokens):
        self.token_stream = iter(tokens)
        self.cur = next(self.token_stream)

    def peek_cur(self):
        return self.cur

    def consume_cur(self):
        prev = self.cur

        try:
            self.cur = next(self.token_stream)
        except StopIteration:
            self.cur = Token(None, None)
        
        return prev

    def not_at_end(self):
        return self.peek_cur().type

    def parse(self):
        statements = []

        while self.not_at_end()  and (s := self.declaration()):
            statements.append(s)

        return statements

    def declaration(self):
        keyword = self.peek_cur()

        if keyword.type == TokenType.VAR:
            return self.var_declaration()
    
        return self.statement()

    def var_declaration(self):
        var = self.consume_cur() 
        assert var.type == TokenType.VAR
        name = self.consume_cur()

        if self.peek_cur().type == TokenType.EQUAL:
            self.consume_cur() # eq
            initial_val = self.expression()
        else:
            initial_val = None

        semi = self.consume_cur()
        assert semi.type == TokenType.SEMI

        return VariableStmt(name, initial_val)
        
    def statement(self):
        keyword = self.peek_cur()

        if keyword.type == TokenType.PRINT:
            return self.print_statement()

        return self.expression_statement()

    def print_statement(self):
        self.consume_cur()
        expr = self.expression()
        semi = self.consume_cur()
        assert semi.type == TokenType.SEMI

        return PrintStmt(expr)

    def expression_statement(self):
        expr = self.expression()
        semi = self.consume_cur()
        print(expr)
        assert semi.type == TokenType.SEMI

        return ExpressionStmt(expr)
    
    def expression(self):
        return self.term()

    def term(self):
        expr = self.factor()

        while self.peek_cur().type in (TokenType.PLUS, TokenType.MINUS):
            op = self.consume_cur().value
            expr = Binary(
                op,
                expr,
                self.factor()
            )

        return expr

    def factor(self):
        expr = self.unary()

        while self.peek_cur().type in (TokenType.STAR, TokenType.SLASH):
            op = self.consume_cur().value
            expr = Binary(
                op,
                expr,
                self.unary()
            )

        return expr

    def unary(self):
        if self.peek_cur().type in (TokenType.MINUS,):
            op = self.consume_cur().value
            return Unary(
                op,
                self.unary()
            )
        
        return self.primary()
            
    def primary(self):
        tkn = self.consume_cur()

        if tkn.type == TokenType.IDENTIFIER:
            return Variable(tkn)
        
        return Primary(tkn.value)
        

    
