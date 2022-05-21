import os
from ruamel.yaml import YAML

yaml = YAML()

trains = os.listdir('charts')


def get_charts_of_train(train):
    return os.listdir(f"charts/{train}")


def get_data_of_chart_in_train(train, chart):
    with open(f"charts/{train}/{chart}/values.yaml", "r", encoding="utf_8") as file:
        return yaml.load(file)


def is_services_exist(values):
    return 'service' in values


def is_service_enabled(service):
    if 'enabled' in service:
        return service['enabled']
    else:
        return True


def get_port_number(port):
    if 'enabled' in port:
        if port['enabled']:
            return port['port']
        else:
            return 0
    else:
        return port['port']


def get_note_for_enabled_service(port_num):
    return "" if port_num > 0 else "Port Disabled"


def get_port_protocol(port):
    return port['protocol'] if 'protocol' in port else "TCP"


def print_verbose_output(train, chart, service_enabled, service, port_name, port):
    print("-----------------------------")
    print(f'Train name: {train}')
    print(f'Chart name: {chart}')
    print(f'Service enabled: {service_enabled}')
    print(f'Service name: {service}')
    print(f'Port name: {port_name}')
    print(f'Port Number: {port}')


def create_port_list_item(train, chart, service_name, port_name, port, protocol, note):
    return {
        "train": train,
        "chart": chart,
        "service_name": service_name,
        "port_name": port_name,
        "port": port,
        "protocol": protocol,
        "note": note
    }


def main():
    port_list = {}
    for train in trains:
        port_list[train] = []
        charts = get_charts_of_train(train)
        for chart in charts:
            data = get_data_of_chart_in_train(train, chart)
            if is_services_exist(data):
                services = data['service']
                for service_name, service in services.items():
                    if is_service_enabled(service):
                        for port_name, port in service['ports'].items():
                            protocol = "TCP"
                            # port_num, protocol = get_port_number_and_protocol(
                            #     port)
                            port_num = get_port_number(port)
                            note = get_note_for_enabled_service(port_num)
                            protocol = get_port_protocol(port)
                            print_verbose_output(
                                train,
                                chart,
                                is_service_enabled(service),
                                service_name,
                                port_name,
                                port_num)
                            port_list[train].append(create_port_list_item(
                                train,
                                chart,
                                service_name,
                                port_name,
                                port_num,
                                protocol,
                                note))
                    else:
                        port_list[train].append(create_port_list_item(
                            train, chart, service_name, "-", 0, "-", "Service Disabled"))

    order = ["core", "stable", "games", "incubator", "dev"]
    if os.path.exists("default_ports.md"):
        os.remove("default_ports.md")
    with open('default_ports.md', 'a', encoding='utf-8') as file:
        for train in order:
            if train in port_list:
                # Sort first by name (because of apps with disabled services)
                sorted_port_list = sorted(
                    port_list[train], key=lambda d: d['chart'])
                # Then sort by port number
                sorted_port_list = sorted(
                    sorted_port_list, key=lambda d: d['port'])
                file.write(f'## {train.capitalize()}\n\n')
                file.write(
                    "| App | Service | Port Name | Port | Protocol | Note |\n")
                file.write(
                    "|:----|:-------:|:---------:|:----:|:--------:|:----:|\n")
                for port in sorted_port_list:
                    line = (
                        f'|{port["chart"]}|'
                        f'{port["service_name"]}|'
                        f'{port["port_name"]}|'
                        f'{port["port"] if port["port"] > 0 else "-"}|'
                        f'{port["protocol"]}|'
                        f'{port["note"]}|\n'
                    )
                    file.write(
                        line)
                file.write('\n\n')


if __name__ == "__main__":
    main()
