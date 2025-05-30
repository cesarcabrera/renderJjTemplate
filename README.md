Mexico, 2025
César A. Cabrera E.
https://cesarcabrera.info/

renderTemplate.py: Takes an Excel File with jinja2 templates and a second file with variable contents to render Jinja2 
templates. The files should have the same sheets names to align values to the templates.

renderTemplates.py -h
usage: renderTemplates.py [-h] [-v] [-f FOLDER] [-c CONFIG] [-p PARAMETERS] [-o OUTPUT] [-u] [-g SECTION_GROUPS] [-s] [-t] [-i] [-d DEBUG]

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         Version
  -f FOLDER, --folder FOLDER
                        Config variables (parameters) file. Def. configVariables.xlsx
  -o OUTPUT, --output OUTPUT
                        Filenames prefix. Def. OUT_
  -u, --unique          Use only the 1st sheet from config file for all the variable sheet
  -g SECTION_GROUPS, --section-groups SECTION_GROUPS
                        Select the groups to show (Sheets name from variables file) Not using "-" nor spaces or special chars, please
  -s, --show-vars       Show detected variables (Optional)
  -t, --show-template   Show templates (Optional)
  -i, --interactive     Wait for after showing one rendered template (Optional)
  -d DEBUG, --debug DEBUG
                        Debug Level (0=Nothing, > 1 more detail)