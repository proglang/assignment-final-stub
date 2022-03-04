from type_check_Lexam import TypeCheckLexam
from interp_Lexam import InterpLexam
from type_check_Cexam import TypeCheckCexam
from interp_Cexam import InterpCexam
from utils import run_tests, validate_tests
from compiler_Lexam import CompilerLexam
import sys


sys.setrecursionlimit(10000)

compiler = CompilerLexam()

if False:
    enable_tracing()

if validate_tests("exam", InterpLexam().interp):
    print("Congratulations, the interpreter verifies all tests!")
else:
    print("The interpreter failed on one or more tests.")

run_tests("exam", compiler, "exam", 
    TypeCheckLexam().type_check, 
    InterpLexam().interp, 
    TypeCheckCexam().type_check, 
    InterpCexam().interp)
