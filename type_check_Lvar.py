import ast
from types import NoneType
import utils


class TypeCheckLvar:
    def check_type_equal(self, t1, t2, e):
        if t1 != t2:
            raise Exception(
                "error: "
                + repr(t1)
                + " != "
                + repr(t2)
                + " in "
                + repr(e)
                + (
                    ("\nAST info 1: " + utils.ast_loc(e))
                    if isinstance(e, ast.AST)
                    else ""
                )
            )

    def type_check_exp(self, e, env):
        match e:
            case ast.BinOp(left, ast.Add(), right):
                l = self.type_check_exp(left, env)
                self.check_type_equal(l, utils.IntType(), left)
                r = self.type_check_exp(right, env)
                self.check_type_equal(r, utils.IntType(), right)
                return utils.IntType()
            case ast.UnaryOp(ast.USub(), v):
                t = self.type_check_exp(v, env)
                self.check_type_equal(t, utils.IntType(), v)
                return utils.IntType()
            case ast.Name(id):
                return env[id]
            case ast.Constant(value) if isinstance(value, int):
                return utils.IntType()
            case ast.Constant(value) if isinstance(value, NoneType):
                return utils.VoidType()
            case ast.Call(ast.Name("input_int"), []):
                return utils.IntType()
            case _:
                raise Exception(
                    "type_check_exp: unexpected "
                    + repr(e)
                    + "\nAST info 1: "
                    + utils.ast_loc(e)
                )

    def type_check_stmts(self, ss, env, idx=0):
        def _logic(obj, env):
            match obj:
                case ast.Assign([ast.Name(id)], value):
                    t = self.type_check_exp(value, env)
                    if id in env:
                        self.check_type_equal(env[id], t, value)
                    else:
                        env[id] = t
                    return True
                case ast.Expr(ast.Call(ast.Name("print"), [arg])):
                    t = self.type_check_exp(arg, env)
                    self.check_type_equal(t, utils.IntType(), arg)
                    return True
                case ast.Expr(value):
                    self.type_check_exp(value, env)
                    return True
                case _:
                    raise Exception(
                        "type_check_stmts: unexpected "
                        + repr(obj)
                        + (
                            ("\nAST info 1: " + utils.ast_loc(obj))
                            if isinstance(obj, ast.AST)
                            else ""
                        )
                    )

        if self.__class__ == __class__:
            for i in range(len(ss)):
                obj = ss[i]
                ret = _logic(obj, env)
                if not isinstance(ret, (bool, NoneType)):
                    return ret
        else:
            obj = ss[idx]
            ret = _logic(obj, env)
            if not isinstance(ret, (bool, NoneType)):
                return ret

    def type_check(self, p):
        match p:
            case ast.Module(body):
                self.type_check_stmts(body, {})
