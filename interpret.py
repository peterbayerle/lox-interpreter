from parser import Expr, Binary, Unary, Primary, Variable, ExpressionStmt, PrintStmt, VariableStmt


class Interpreter:
    env = dict()
    
    # expression evaluation
    def evaluate(self, expr: Expr):
        return expr.accept(self)
        
    def visitBinary(self, expr: Binary):
        op = expr.value
        lhs = self.evaluate(expr.lhs)
        rhs = self.evaluate(expr.rhs)

        if op == "+":
            return lhs + rhs
        elif op == "-":
            return lhs - rhs
        elif op == "*":
            return lhs * rhs
        elif op == "/":
            return lhs / rhs

    def visitUnary(self, expr: Unary):
        op = expr.value

        if op == "-":te
            return - self.evaluate(expr.rhs)

    def visitVariable(self, expr: Variable):
        return self.env.get(expr.value)

    def visitPrimary(self, expr: Primary):
        return int(expr.value)

    # statement execution
    def interpret(self, statements):
        for statement in statements:
            self.execute(statement)

    def execute(self, statment):
        return statment.accept(self)

    def visitVariableStmt(self, stmt: VariableStmt):
        val = self.evaluate(stmt.expression) if stmt.expression else None
        self.env[stmt.name] = val

    def visitExpressionStmt(self, stmt: ExpressionStmt):
        self.evaluate(stmt.expression)
        return None

    def visitPrintStmt(self, stmt: PrintStmt):
        value = self.evaluate(stmt.expression)
        print(value)
        return None

    
