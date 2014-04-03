from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('livestreamergui.pyw', base=base, icon='lsgui_icon.ico')
]

setup(name='lsgui',
      version = '1.0',
      description = 'Livestreamer GUI',
      options = dict(build_exe = buildOptions),
      executables = executables)
