Mexico, 2025
César A. Cabrera E.
https://cesarcabrera.info/

renderTemplate.py: Takes an Excel File with jinja2 templates (one line per cell) and a second file with variable contents to render Jinja2 
templates, when the data is complex, variable content can be json objects. There are two scenarios: 
a) (Default) Using two excel files with same sheet names, one pair of template-variable identified by the sheet name, 
b) (-u option) Two excel files, one with jinja templates (only 1st sheet used) and the second with a set of different variable contents to generate as many files as sheet names on the variables file.
Note: Given that this project is for generating device configurations, the template file is called "configTemplates" and variable files is sometimes called "parameters".

renderTemplates.py -h<br>
usage: renderTemplates.py [-h] [-v] [-f FOLDER] [-c CONFIG] [-p PARAMETERS] [-o OUTPUT] [-u] [-g SECTION_GROUPS] [-s] [-t] [-i] [-k] [-d DEBUG] [-x]<br>
<br>
optional arguments:<br>
  -h, --help            show this help message and exit<br>
  -v, --version         Version<br>
  -f FOLDER, --folder FOLDER<br>
                        Config+parameters+output folder. Default: .<br>
  -c CONFIG, --config CONFIG<br>
                        Config Filename. Def. configTemplates.xlsx<br>
  -p PARAMETERS, --parameters PARAMETERS<br>
                        Config variables (parameters) file. Def. configVariables.xlsx<br>
  -o OUTPUT, --output OUTPUT<br>
                        Filenames prefix. Def. OUT_<br>
  -u, --unique          Use only the 1st sheet from config file for all the variable sheets (one template for all sites)<br>
  -g SECTION_GROUPS, --section-groups SECTION_GROUPS<br>
                        Select the groups to show (Sheet name from variables file) Do not use "-" nor spaces or special chars, please<br>
  -s, --show-vars       (Optional)Show detected variables<br>
  -t, --show-template   (Optional)Show templates<br>
  -i, --interactive     (Optional)Wait for enter/key after showing one rendered template<br>
  -k, --cat             (Optional)Write all on one single file<br>
  -d DEBUG, --debug DEBUG<br>
                        Debug Level (0=Nothing, > 1 more detail)<br>
  -x                    Consolidate ouput on 1 file<br>
