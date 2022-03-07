from ast import *
from type_check_Cfun import TypeCheckCfun
from utils import *

class TypeCheckCexam(TypeCheckCfun):
  def type_check_exp(self, e, env):
    match e:
      case List(es, Load()):
        ts = [self.type_check_exp(e, env) for e in es]
        elt_ty = ts[0]
        for (ty, elt) in zip(ts, es):
            self.check_type_equal(elt_ty, ty, elt)
        e.has_type = ListType(elt_ty)
        return e.has_type
      case Call(Name('len'), [tup]):
        tup_t = self.type_check_exp(tup, env)
        tup.has_type = tup_t
        match tup_t:
          case TupleType(_) | ListType(_):
            return IntType()
          case _:
            raise Exception('len expected a tuple, not ' + repr(tup_t))
      case Subscript(tup, index, Load()):
        tup_ty = self.type_check_exp(tup, env)
        index_ty = self.type_check_exp(index, env)
        self.check_type_equal(index_ty, IntType(), index)
        match tup_ty:
          case TupleType(ts):
            match index:
              case Constant(i):
                return ts[i]
              case _:
                raise Exception('subscript required constant integer index')
          case ListType(ty):
            return ty
          case _:
            raise Exception('subscript expected a tuple, not ' + repr(tup_ty))
      case BinOp(left, Mult() | FloorDiv() | Mod() , right):
        l = self.type_check_exp(left, env)
        self.check_type_equal(l, IntType(), left)
        r = self.type_check_exp(right, env)
        self.check_type_equal(r, IntType(), right)
        return IntType()
      case _:
        return super().type_check_exp(e, env)

  def type_check_stmt(self, s, env):
    match s:
      case Assign([Subscript(tup, index, Store())], value):
        tup_t = self.type_check_exp(tup, env)
        value_t = self.type_check_exp(value, env)
        index_ty = self.type_check_exp(index, env)
        self.check_type_equal(index_ty, IntType(), index)
        match tup_t:
          case ListType(ty):
            self.check_type_equal(ty, value_t, s)
          case _:
            super().type_check_stmt(s, env)
            # raise Exception('type_check_stmts: expected a list, not ' \
            #                + repr(tup_t))
      case _:
        return super().type_check_stmt(s, env)
