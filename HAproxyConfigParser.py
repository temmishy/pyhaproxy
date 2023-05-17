from pyhaproxy.parse import Parser
from pyhaproxy.render import Render
import pyhaproxy.config as configs
import csv


# Build the configuration instance by calling Parser('config_file').build_configuration()
config_path = 'haproxy.cfg'
cfg_parser = Parser(config_path)
configuration = cfg_parser.build_configuration()

#Table headers
headers = [
     ("Frontend name:", "Fontend host:", "Frontend port:", "Backend name:", "Server host:", "Server port:")
]
#Table name "*.cvs"
table_name = "data.cvs"
#Create csv file
with open (table_name, "w") as file:
    writer = csv.writer(file)
    writer.writerows(
       headers
    ) 

frontend_sections = configuration.frontends

# Server exclusions
patterns = [
    
    ]

for fe_section in frontend_sections:
    the_fe_section_name = fe_section.name
    the_fe_section = configuration.frontend(str(the_fe_section_name))
    usebackends = the_fe_section.usebackends()  
    for usebe in usebackends:
        the_be_section_name = usebe.backend_name
# Operates the Server in a backend
        the_be_section = configuration.backend(str(the_be_section_name))
        for server in the_be_section.servers():
            if any(pattern in server.host for pattern in patterns) == False:
                data = [
                    [the_fe_section_name, fe_section.host, fe_section.port, the_be_section_name, server.host, server.port]
                ]
                with open (table_name, "a") as file:
                    writer = csv.writer(file)
                    writer.writerows(
                        data
                   ) 