import compiler
import interp_Lfun
import interp_Cfun
import type_check_Lfun
import type_check_Cfun
from utils import run_tests, enable_tracing
import sys

sys.setrecursionlimit(10000)

compiler = compiler.Compiler()

# enable_tracing()
run_tests("var", compiler, "var", type_check_Lfun.TypeCheckLfun().type_check, interp_Lfun.InterpLfun().interp, type_check_Cfun.TypeCheckCfun().type_check, interp_Cfun.InterpCfun().interp)
run_tests("regalloc", compiler, "regalloc", type_check_Lfun.TypeCheckLfun().type_check, interp_Lfun.InterpLfun().interp, type_check_Cfun.TypeCheckCfun().type_check, interp_Cfun.InterpCfun().interp)
run_tests("lif", compiler, "lif", type_check_Lfun.TypeCheckLfun().type_check, interp_Lfun.InterpLfun().interp, type_check_Cfun.TypeCheckCfun().type_check, interp_Cfun.InterpCfun().interp)
run_tests("tuples", compiler, "tuples", type_check_Lfun.TypeCheckLfun().type_check, interp_Lfun.InterpLfun().interp, type_check_Cfun.TypeCheckCfun().type_check, interp_Cfun.InterpCfun().interp)
run_tests("fun", compiler, "fun", type_check_Lfun.TypeCheckLfun().type_check, interp_Lfun.InterpLfun().interp, type_check_Cfun.TypeCheckCfun().type_check, interp_Cfun.InterpCfun().interp)
