import os
from ruamel.yaml import YAML

yaml = YAML()

# Configuration
TRAINS_PATH = "./charts"
VERBOSE = False
EXCLUDED_TRAINS = [
]
EXCLUDED_APPS = [
    "dev/acestream",
    "games/acestream",
]
TRAIN_ORDER_IN_PORT_LIST_FILE = [
    "core",
    "stable",
    "incubator",
    "dev"
]


# General Utils
def logger(message, color):
    if VERBOSE:
        if color == "RED":
            print(Colors.RED + message)
        if color == "GREEN":
            print(Colors.GREEN + message)
        if color == "BLUE":
            print(Colors.BLUE + message)
        if color == "YELLOW":
            print(Colors.YELLOW + message)


class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'


# Data
class App:
    def __init__(self, name, train):
        self.name = name
        self.train = train
        self.services = []
        # Later we can add things like
        # self.persistence etc

    def set_svc(self, values):
        self.services = process_services(values)


# Logic
def process_active_trains():
    """Returns a list of trains that are not excluded"""
    all_trains = os.listdir(TRAINS_PATH)
    apps = []
    for train in all_trains:
        if train in EXCLUDED_TRAINS:
            logger(
                "##########################################################################################", "YELLOW")
            logger(f'Skipping - Train: <{train}>', "RED")
            logger(
                "##########################################################################################", "YELLOW")
        else:
            logger(
                "##########################################################################################", "YELLOW")
            logger(f'Processing - Train: <{train}>', "GREEN")
            logger(
                "##########################################################################################", "YELLOW")
            apps += process_active_charts_from_train(train)
    return apps


def process_active_charts_from_train(train):
    """Returns a list of apps that are not excluded from this train"""
    all_apps = os.listdir(os.path.join(TRAINS_PATH, train))
    apps = []
    for app in all_apps:
        if f'{train}/{app}' in EXCLUDED_APPS:
            logger(
                "------------------------------------------------------------------------------------------", "YELLOW")
            logger(
                f'Skipping - App: <{app}> from Train: <{train}>', "RED")
        else:
            logger(
                "------------------------------------------------------------------------------------------", "YELLOW")
            logger(
                f'Processing - App: <{app}> from Train: <{train}>', "BLUE")
            curr_app = App(name=app, train=train)
            curr_app.set_svc(get_all_values_for_app(train, app))
            apps.append(curr_app)
    return apps


def get_all_values_for_app(train, app):
    """Returns all values of the app"""
    with open(os.path.join(TRAINS_PATH, train, app, "values.yaml"), "r", encoding="utf_8") as values_file:
        return yaml.load(values_file)


def process_services(values):
    """Returns all services of the values"""
    services = []
    # If no service is defined we are done here
    if not 'service' in values:
        logger("\t\t\t└No service found", "RED")
        services.append({
            "svc_name": "-",
            "port_name": "-",
            "port": 0,
            "protocol": "-",
            "status": "No Service Defined",
            "note": ""
        })
    else:
        for service in values['service'].items():
            logger(f'\t\t\t└Processing - Service <{service[0]}>', "BLUE")
            # If key enabled does not exist in service, service is enabled by default (eg. main), get the ports
            # If key enabled exists in service, and service is enabled, get the ports
            if (not 'enabled' in service[1]) or ('enabled' in service[1] and service[1]['enabled']):
                logger("\t\t\t\t\t\t└Service is Active", "GREEN")
                if 'ports' in service[1]:
                    # ports = get_ports(service[1]['ports'].items())
                    for port in service[1]['ports'].items():
                        logger(
                            f'\t\t\t\t\t\t└Processing - Port: <{port[0]}>', "BLUE")
                        cleaned_port = process_port(port)
                        services.append({
                            "svc_name": service[0],
                            **cleaned_port,
                            "note": ""
                        })
                else:
                    logger("\t\t\t\t\t\t└No Ports found", "RED")
                    services.append({
                        "svc_name": service[0],
                        "port_name": "-",
                        "port": 0,
                        "protocol": "-",
                        "status": "No Ports Defined",
                        "note": ""
                    })
            # If service is disabled, we are done here
            else:
                logger("\t\t\t\t\t\t└Service is Disabled", "RED")
                services.append({
                    "svc_name": service[0],
                    "port_name": "-",
                    "port": 0,
                    "protocol": "-",
                    "status": "Service is Disabled",
                    "note": ""
                })
    return services


def process_port(port):
    if (not 'enabled' in port[1]) or ('enabled' in port[1] and port[1]['enabled']):
        logger('\t\t\t\t\t\t\t\t\t└Port is Active', "GREEN")
        return{
            "port_name": port[0],
            "port": port[1]['port'],
            "protocol": port[1]['protocol'] if 'protocol' in port[1] else "TCP",
            "status": "Active"
        }
    else:
        logger('\t\t\t\t\t\t\t\t\t└Port is Disabled', "RED")
        return{
            "port_name": port[0],
            "port": 0,
            "protocol": "-",
            "status": "Port is Disabled"
        }


def get_available_trains(apps):
    trains = []
    for app in apps:
        if app.train not in trains:
            trains.append(app.train)
    return trains


def get_order_of_available_trains(apps):
    available_trains = get_available_trains(apps)
    # Order trains that are available (a train might be excluded)
    order = [
        train for train in TRAIN_ORDER_IN_PORT_LIST_FILE if train in available_trains]
    # Add rest of the available trains that has not be ordered to the end of the order
    order += [
        train for train in available_trains if train not in TRAIN_ORDER_IN_PORT_LIST_FILE]
    return order


def get_apps_of_train(apps, train):
    return [app for app in apps if app.train == train]


def create_default_ports_file(apps):
    # TODO: Sort them by port
    order = get_order_of_available_trains(apps)
    if os.path.exists("default_ports.md"):
        os.remove("default_ports.md")
    with open('default_ports.md', 'a', encoding='utf-8') as file:
        for train in order:
            file.write(f'## {train.capitalize()}\n\n')
            file.write(
                "| App | Service | Port Name | Port | Protocol | Status | Note |\n")
            file.write(
                "|:----|:-------:|:---------:|:----:|:--------:|:------:|:----:|\n")
            apps_in_train = get_apps_of_train(apps, train)
            port_list = []
            for app in apps_in_train:
                for port in app.services:
                    port_list.append(dict(
                        app_name=app.name,
                        svc_name=port["svc_name"],
                        port_name=port["port_name"],
                        port=port["port"],
                        protocol=port["protocol"],
                        status=port["status"],
                        note=port["note"]
                    ))
            # Sort by name
            sorted_port_list = sorted(
                port_list, key=lambda item: item['app_name'])
            sorted_port_list = sorted(
                sorted_port_list, key=lambda item: item['port'])

            for port in sorted_port_list:
                line = (
                    f'|{port["app_name"]}|'
                    f'{port["svc_name"]}|'
                    f'{port["port_name"]}|'
                    f'{port["port"] if port["port"] > 0 else "-"}|'
                    f'{port["protocol"]}|'
                    f'{port["status"]}|'
                    f'{port["note"]}|\n'
                )
                file.write(line)


def main():
    processed_apps = process_active_trains()
    create_default_ports_file(processed_apps)


main()
