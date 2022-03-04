from ast import *
from interp_Cfun import InterpCfun
from utils import *
from interp_Lfun import Function

class InterpCexam(InterpCfun):

  def interp_exp(self, e, env):
    match e:
      case List(es, Load()):
        return [self.interp_exp(e, env) for e in es]
      case BinOp(left, Mult(), right):
          l = self.interp_exp(left, env); r = self.interp_exp(right, env)
          return l * r
      case BinOp(left, FloorDiv(), right):
          l = self.interp_exp(left, env); r = self.interp_exp(right, env)
          return l // r
      case BinOp(left, Mod(), right):
          l = self.interp_exp(left, env); r = self.interp_exp(right, env)
          return l % r
      case _:
        return super().interp_exp(e, env)

  def interp_stmts(self, ss, env):
    if len(ss) == 0:
      return
    match ss[0]:
      case Assign([Subscript(lst, index)], value):
        lst = self.interp_exp(lst, env)
        index = self.interp_exp(index, env)
        lst[index] = self.interp_exp(value, env)
        return self.interp_stmts(ss[1:], env)
      case _:
        return super().interp_stmts(ss, env)
