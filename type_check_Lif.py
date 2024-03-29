from ast import *
from type_check_Lvar import TypeCheckLvar
from utils import *


class TypeCheckLif(TypeCheckLvar):
    def type_check_exp(self, e, env):
        match e:
            case Constant(value) if isinstance(value, bool):
                return BoolType()
            case IfExp(test, body, orelse):
                test_t = self.type_check_exp(test, env)
                self.check_type_equal(BoolType(), test_t, test)
                body_t = self.type_check_exp(body, env)
                orelse_t = self.type_check_exp(orelse, env)
                self.check_type_equal(body_t, orelse_t, e)
                return body_t
            case BinOp(left, Sub(), right):
                l = self.type_check_exp(left, env)
                self.check_type_equal(l, IntType(), left)
                r = self.type_check_exp(right, env)
                self.check_type_equal(r, IntType(), right)
                return IntType()
            case UnaryOp(Not(), v):
                t = self.type_check_exp(v, env)
                self.check_type_equal(t, BoolType(), v)
                return BoolType()
            case BoolOp(op, values):
                left = values[0]
                right = values[1]
                l = self.type_check_exp(left, env)
                self.check_type_equal(l, BoolType(), left)
                r = self.type_check_exp(right, env)
                self.check_type_equal(r, BoolType(), right)
                return BoolType()
            case Compare(left, [cmp], [right]) if isinstance(cmp, Eq) or isinstance(
                cmp, NotEq
            ):
                l = self.type_check_exp(left, env)
                r = self.type_check_exp(right, env)
                self.check_type_equal(l, r, e)
                return BoolType()
            case Compare(left, [cmp], [right]):
                l = self.type_check_exp(left, env)
                self.check_type_equal(l, IntType(), left)
                r = self.type_check_exp(right, env)
                self.check_type_equal(r, IntType(), right)
                return BoolType()
            # case Let(Name(x), rhs, body):
            #   t = self.type_check_exp(rhs, env)
            #   new_env = dict(env); new_env[x] = t
            #   return self.type_check_exp(body, new_env)
            case Begin(ss, e):
                self.type_check_stmts(ss, env)
                return self.type_check_exp(e, env)
            case _:
                return super().type_check_exp(e, env)

    def type_check_stmts(self, ss, env, idx=0):
        # Couldn't modify here because of the entanglement
        if len(ss) == 0:
            return Bottom()
        match ss[idx]:
            case If(test, body, orelse):
                test_t = self.type_check_exp(test, env)
                self.check_type_equal(BoolType(), test_t, test)
                body_t = self.type_check_stmts(body, env)  # TODO
                orelse_t = self.type_check_stmts(orelse, env)  # TODO
                self.check_type_equal(body_t, orelse_t, ss[idx])
                cond_t = body_t if isinstance(orelse_t, Bottom) else orelse_t
                if len(ss[idx:]) > 1:
                    ret_t = self.type_check_stmts(ss[idx + 1 :], env)  # TODO
                    self.check_type_equal(cond_t, ret_t, ss[idx])
                    return ret_t if isinstance(cond_t, Bottom) else cond_t
                else:  # this 'if' statement is in tail position
                    return cond_t
            case _:
                return super().type_check_stmts(ss, env, idx)
