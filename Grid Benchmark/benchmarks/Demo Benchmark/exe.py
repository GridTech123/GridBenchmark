import cx_Freeze

executables = [cx_Freeze.Executable('benchmark.py')]

cx_Freeze.setup(name = 'Poly Cities [alpha]', version = '1.0.0', options = {'build_exe': {'packages':['pygame', 'pygame.locals', 'pickle', 'pyError', 'tkFileDialog', 'gbAPI'], 'include_files':['cover.png', 'update.run']}}, executables = executables)
