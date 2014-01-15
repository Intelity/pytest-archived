import pkg_resources
import yaml

def load_data():
    source = pkg_resources.resource_stream('resources', 'input.yaml')
    data = yaml.load(source.read())
    return data
