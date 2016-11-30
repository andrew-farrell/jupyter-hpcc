"""This file contains "magic" implementations for IPython Notebook
that allow you to build Boost.Python programs and modules.
"""

import IPython.core.magic as ipym
import numpy as np
from numpy import genfromtxt

# IMPORTANT: Adjust these flags to match your system.
#
# For the Python flags you can often use the ``python-config`` command.
# For boost.python, you just need to know.


# STOP EDITING
#
# Don't edit below this line unless you know what you're doing or are
# feeling adventurous (or perhaps are stuck.)

@ipym.magics_class
class HPCCPythonMagics(ipym.Magics):

    @ipym.cell_magic
    def hpcc(self, line, cell=None):
        """Compile, execute C++ code, and return the standard output."""

        args = line.split()
        name = args[0]

        # args = args[1:]
        # debug = 'debug' in args

        # Define the source and executable filenames.
        source_filename = '{}.ecl'.format(name)

        # Write the code contained in the cell to the ECL file.
        with open(source_filename, 'w') as f:
            f.write(cell)

        result = []

        # Compile the C++ code into an executable.
        cmd = "eclplus {} {} {} {} {} {} {} {}".format(
		    'action=query',
            'user=hpccdemo',
            'password=hpccdemo',
            'server=http://192.168.23.129:8010',
            'cluster=thor',
            'ecl=@' + source_filename,
            'format=csv',
            'output=' + '{}.csv'.format(name))

        # if debug:
        # result.append(cmd)

        compile = self.shell.getoutput(cmd)
        result = genfromtxt('{}.csv'.format(name), delimiter=',')
        #output = self.shell.getoutput(program_filename)
        # result.append(output)

        if any(result):
		   return result
           # return ' -- '.join(map(str, filter(None, result)))
		   


def load_ipython_extension(ipython):
    ipython.register_magics(HPCCPythonMagics)
