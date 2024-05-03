import sys
import textwrap


list_mod = ','.join(sys.builtin_module_names)

print(textwrap.fill(list_mod,width=70))