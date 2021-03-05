from sys import stdin, exit, stderr
import yaml
import json
from yaml import SafeLoader
from jinja2 import Environment, PackageLoader

ENV = Environment(
    loader=PackageLoader("generator", "templates")
)
PROTOCOL_TEMPLATE = ENV.get_template("protocol.jinja2")

raw_context = stdin.read()
try:
    context = json.loads(raw_context)
    if not isinstance(context, dict):
        raise ValueError("Invalid JSON object")
except (json.JSONDecodeError, ValueError):
    print("Input is not valid JSON, attempting to parse as YAML", file=stderr)
    try:
        context = yaml.load(raw_context, Loader=SafeLoader)
        if not isinstance(context, dict):
            raise ValueError("Invalid JSON object")
    except (yaml.YAMLError, ValueError):
        print("Input is not valid YAML")
        print("Failed to parse input!", file=stderr)
        exit(1)


print(PROTOCOL_TEMPLATE.render(context["protocols"][0]))
