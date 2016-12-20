import re
from IPython.core.magic import Magics, magics_class, cell_magic, line_magic, needs_local_scope
try:
    from traitlets.config.configurable import Configurable
    from traitlets import Bool, Int, Unicode
except ImportError:
    from IPython.config.configurable import Configurable
    from IPython.utils.traitlets import Bool, Int, Unicode
try:
    from pandas.core.frame import DataFrame, Series
except ImportError:
    DataFrame = None
    Series = None

from collections import defaultdict

@magics_class
class HpccMagic(Magics, Configurable):
    """Runs ECL.

    Provides the %%hpcc magic."""


                           
  



    def __init__(self, shell):
        Configurable.__init__(self, config=shell.config)
        Magics.__init__(self, shell=shell)

        # Add ourself to the list of module configurable via %config
        self.shell.configurables.append(self)

    @needs_local_scope
    #@line_magic('hpcc')
    @cell_magic('hpcc')
    def execute(self, line, cell='', local_ns={}):
        """ 
        
        Runs HPCC ECL

        """
        # save globals and locals so they can be referenced in bind vars
        user_ns = self.shell.user_ns.copy()
        user_ns.update(local_ns)
        
        def param_details():
            return 'Usage %%hpcc [cell_name] user=[user] password=[password] server=[server] cluster=[cluster]'
        
        def replace_local(input):
            result = input
            #tokens = re.findall(r"%(\w+)%",input)
            #return re.sub(r"[%]\s*[^%]+\s*[%]",lambda k:self.shell.user_ns.get(k[1,-1].strip(),k),input)
            for v in re.findall(r"%(\w+)%",input):
                result = re.sub(r'%\s?' + v + '\s?%', str(self.shell.user_ns[str(v)]), result)
                
            return result
            
        p_line = replace_local(line)
            
        parsed_args = {}
        parsed_args = dict(re.findall(r'(\S+)=(".*?"|\S+)', p_line))
        args = p_line.split()
        name = args[0]
        

        # Define the source and executable filenames.
        source_filename = '{}.ecl'.format(name)

        try:
            p_cell = replace_local(cell)
            # Write the code contained in the cell to the ECL file.
            with open(source_filename, 'w') as f:
                f.write(p_cell)

            result = []

            # Prepare ECL for use with ECLPLUS
            cmd = "eclplus {} {} {} {} {} {} {} {}".format(
                'action=query',
                'user='+parsed_args['user'],
                'password='+parsed_args['password'],
                'server='+parsed_args['server'],
                'cluster='+parsed_args['cluster'],
                'ecl=@' + source_filename,
                'format=xml',
                'output=' + '{}.xml'.format(source_filename))

        
            compile = self.shell.getoutput(cmd)
         
            f = open('{}.xml'.format(source_filename), "r") 
            result = f.read()
            f.close()
            
            return result 

        except (RuntimeError) as rune:
            if self.short_errors:
                print(rune)
            else:
                raise
        except (NameError) as ne:
            return param_details()
        except (KeyError) as ke:
            return param_details()



def load_ipython_extension(ip):
    """Load the extension in IPython."""
    ip.register_magics(HpccMagic)
