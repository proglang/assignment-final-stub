from ast import *
from types import NoneType
from type_check_Lif import TypeCheckLif
from utils import *


class TypeCheckLwhile(TypeCheckLif):
    def type_check_stmts(self, ss, env, idx=0):
        def _logic(obj, env):
            match obj:
                case While(test, body, []):
                    test_t = self.type_check_exp(test, env)
                    self.check_type_equal(BoolType(), test_t, test)
                    body_t = self.type_check_stmts(body, env)
                    return True
                case _:
                    return False

        if self.__class__ == __class__:
            for i in range(len(ss)):
                obj = ss[i]
                ret = _logic(obj, env)
                if not isinstance(ret, (bool, NoneType)):
                    return ret
                if ret == False:
                    ret_s = super().type_check_stmts(ss, env, i)
                    if not isinstance(ret_s, (bool, NoneType)):
                        return ret_s
        else:
            obj = ss[idx]
            ret = _logic(obj, env)
            if not isinstance(ret, (bool, NoneType)):
                return ret
            if ret == False:
                ret_s = super().type_check_stmts(ss, env, idx)
                if not isinstance(ret_s, (bool, NoneType)):
                    return ret_s
