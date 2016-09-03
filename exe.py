import cx_Freeze

executables = [cx_Freeze.Executable('Grid_Script.py')]

cx_Freeze.setup(name = 'Grid Script Compiler', version = '1.0.0', options = {'build_exe': {'packages':['sys', 'time']}}, executables = executables)
