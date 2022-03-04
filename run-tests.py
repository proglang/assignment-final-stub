import compiler
import interp_Lfun
import interp_Cfun
from type_check_Lexam import TypeCheckLexam
from interp_Lexam import InterpLexam
from interp_Cexam import InterpCexam
import type_check_Lfun
import type_check_Cfun
from utils import run_tests, enable_tracing
import sys

sys.setrecursionlimit(10000)

compiler = compiler.Compiler()

if False:
    enable_tracing()

run_tests("var", compiler, "var", type_check_Lfun.TypeCheckLfun().type_check, interp_Lfun.InterpLfun().interp, type_check_Cfun.TypeCheckCfun().type_check, interp_Cfun.InterpCfun().interp)
run_tests("regalloc", compiler, "regalloc", type_check_Lfun.TypeCheckLfun().type_check, interp_Lfun.InterpLfun().interp, type_check_Cfun.TypeCheckCfun().type_check, interp_Cfun.InterpCfun().interp)
run_tests("lif", compiler, "lif", type_check_Lfun.TypeCheckLfun().type_check, interp_Lfun.InterpLfun().interp, type_check_Cfun.TypeCheckCfun().type_check, interp_Cfun.InterpCfun().interp)
run_tests("tuples", compiler, "tuples", type_check_Lfun.TypeCheckLfun().type_check, interp_Lfun.InterpLfun().interp, type_check_Cfun.TypeCheckCfun().type_check, interp_Cfun.InterpCfun().interp)
run_tests("fun", compiler, "fun", type_check_Lfun.TypeCheckLfun().type_check, interp_Lfun.InterpLfun().interp, type_check_Cfun.TypeCheckCfun().type_check, interp_Cfun.InterpCfun().interp)
