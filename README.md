Mexico, 2025
César A. Cabrera E.
https://cesarcabrera.info/

renderTemplate.py: Takes an Excel File with jinja2 templates and a second file with variable contents to render Jinja2 
templates. The files should have the same sheets names to align values to the templates.

renderTemplates.py -h<br>
usage: renderTemplates.py [-h] [-v] [-f FOLDER] [-c CONFIG] [-p PARAMETERS] [-o OUTPUT] [-u] [-g SECTION_GROUPS] [-s] [-t] [-i] [-d DEBUG]<br>
optional arguments:<br>
  -h, --help            Show this help message and exit<br>
  -v, --version         Version<br>
  -f FOLDER, --folder FOLDER<br>
                        Config+parameters+output folder. Default: .<br>
  -o OUTPUT, --output OUTPUT
                        Filenames prefix. Def. OUT_<br>
  -u, --unique          Use only the 1st sheet from config file for all the variable sheets<br>
  -g SHEET_NAME, --section-groups SHEET_NAME<br>
                        Select the section groups to show (Sheet name from variables file). Do not use "-" nor spaces or special chars, please<br>
  -s, --show-vars       (Optional) Show detected variables<br>
  -t, --show-template   (Optional) Show templates<br>
  -i, --interactive     (Optional) Wait for after showing one rendered template<br>
  -d DEBUG, --debug DEBUG<br>
                        Debug Level (0=Nothing, > 1 more detail)<br>