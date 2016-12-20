# jupyter-hpcc

## Introduction
%%hpcc magic for jupyter/ipython notebooks (http://jupyter.org/), aiming to mesh data science through HPCC (http://hpccsystems.com) with exploration through Jupyter notebooks.

Allows HPCC's ECL to be run in each Jupyter cell

ECLPLUS used to send ECL to HPCC

Local python variables can be bound to placeholders in ECL

Allows polygot development of solutions using ECL along with python and any other embedded languages in one Jupyter notebook.
e.g. Transform your data at scale with HPCC using ECL then visualise the results using Python and matplotlib

## How to raise issues or feature requests:
* https://github.com/andrew-farrell/jupyter-hpcc/issues

## Prerequsites:
* Install https://hpccsystems.com/download/developer-tools/client-tools
** make sure eclplus is available on the path envinronment var
* Python 2.7.X
* Jupyter, http://jupyter.org/ or via Anaconda  https://www.continuum.io/downloads
* HPCC virtual machine (https://hpccsystems.com/download/virtual-machine-image) or have HPCC installed already

## Examples:
* https://github.com/andrew-farrell/jupyter-hpcc/blob/master/jupyter-hpcc-first-notebook.ipynb

## TODO:
* integrate with hpcc visualisation library
* allow easy ingestion of data e.g. spraying of csv into HPCC
* create tighter integration with ECPLUS or SOAP services to give more subtle control
* create tighter integration with pandas
* make it easier to handle outputs
* move to asychronous mechansim, poll workunit instead

## Credits:

## hpcc magic based on code from:
* https://github.com/catherinedevlin/ipython-sql
* https://github.com/abingham/boost_python_tutorial
