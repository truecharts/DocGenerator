from ruamel.yaml import YAML

yaml = YAML()

with open('Chart.yaml', 'r') as file:
    data = yaml.load(file)


order = [
    "name",
    "type",
    "description",
    "deprecated",
    "apiVersion",
    "kubeVersion",
    "version",
    "appVersion",
    "dependencies",
    "icon",
    "home",
    "sources",
    "keywords",
    "maintainers",
    "annotations"
]

new_data = {}

for key in order:
    with open('NewChart.yaml', 'a') as file:
        yaml.dump({key: data[key]}, file)
