from ast import *
from cProfile import label
from typing import Optional
from register_allocation import build_interference, color_graph
from register_allocation import color_to_register, all_argument_passing_registers, callee_saved_registers
from utils import *
from x86_ast import *
from ast import List
from dataclasses import dataclass, field
from pprint import pprint

from compiler import Compiler, Binding, Temporaries

@dataclass
class CompilerLexam(Compiler):
    pass
