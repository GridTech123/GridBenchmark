import cx_Freeze

executables = [cx_Freeze.Executable('Grid_Benchmark.py')]

cx_Freeze.setup(name = 'Poly Cities [alpha]', version = '1.0.0', options = {'build_exe': {'packages':['pygame', 'pygame.locals', 'pickle', 'pyError', 'tkFileDialog'], 'include_files':['left.png', 'right.png', 'benchmarks']}}, executables = executables)
