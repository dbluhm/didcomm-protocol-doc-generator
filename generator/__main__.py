from sys import stdin
import yaml
from yaml import SafeLoader
from jinja2 import Environment, PackageLoader

ENV = Environment(
    loader=PackageLoader("generator", "templates")
)
PROTOCOL_TEMPLATE = ENV.get_template("protocol.jinja2")

context_yaml = stdin.read()
context = yaml.load(context_yaml, Loader=SafeLoader)
print(PROTOCOL_TEMPLATE.render(context["protocols"][0]))
