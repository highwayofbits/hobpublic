from jinja2 import Environment, FileSystemLoader

#location of templates
ENV = Environment(loader=FileSystemLoader('.'))

#load the template file
template= ENV.get_template("template.j2")

#provide source info for the template using a list of dictionaries
source_info2 = [
{
    "name":"ge-0/0/0",
    "desc":"MyInterface0",
    "vlan":10
},
{
    "name":"ge-0/0/3",
    "desc":"MyInterface3",
    "vlan":0
},
{
    "name":"ge-0/0/4",
    "desc":"MyInterface4",
    "vlan":10
}
]

#render my config
print(template.render(interface_list=source_info2))