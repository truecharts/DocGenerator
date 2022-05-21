from ruamel.yaml import YAML
import os

yaml = YAML()

trains = os.listdir('charts')

port_list = {}
for train in trains:
    port_list[train] = []
    charts = os.listdir(f'charts/{train}')
    for chart in charts:
        with open(f'charts/{train}/{chart}/values.yaml', 'r', encoding='utf_8') as file:
            data = yaml.load(file)
        if 'service' in data:
            services = data['service']
            for service in services:
                if 'enabled' in services[service]:
                    if services[service]['enabled']:
                        service_enabled = True
                    else:
                        service_enabled = False
                else:
                    service_enabled = True
                if service_enabled:
                    for port_name in services[service]['ports']:
                        port_enabled = None
                        protocol = "TCP"
                        if 'enabled' in services[service]['ports'][port_name]:
                            if services[service]['ports'][port_name]['enabled']:
                                port_enabled = True
                                if port_enabled:
                                    port = services[service]['ports'][port_name]['port']
                            if 'protocol' in services[service]['ports'][port_name]:
                                protocol = services[service]['ports'][port_name]['protocol']
                        else:
                            port = services[service]['ports'][port_name]['port']
                        # print("-----------------------------")
                        # print(f'Train name: {train}')
                        # print(f'Chart name: {chart}')
                        # print(f'Service enabled: {service_enabled}')
                        # print(f'Service name: {service}')
                        # print(f'Ports Enabled: {port_enabled}')
                        # print(f'Port name: {port_name}')
                        # print(f'Port Number: {port}')
                        port_list[train].append({
                            "train": train,
                            "chart": chart,
                            "service_name": service,
                            "port_name": port_name,
                            "port": port,
                            "protocol": protocol,
                            "note": ""
                        })
                else:
                    port_list[train].append({
                        "train": train,
                        "chart": chart,
                        "service_name": service,
                        "port_name": "-",
                        "port": 0,
                        "protocol": "-",
                        "note": "Service Disabled"
                    })


order = ["core", "stable", "games", "incubator", "dev"]
with open('portlist.md', 'a', encoding='utf-8') as f:
    for train in order:
        if train in port_list:
            # Sort first by name (because of apps with disabled services)
            sorted_port_list = sorted(
                port_list[train], key=lambda d: d['chart'])
            # Then sort by port number
            sorted_port_list = sorted(
                sorted_port_list, key=lambda d: d['port'])
            f.write(f'## {train.capitalize()}\n\n')
            f.write("| App | Service | Port Name | Port | Protocol | Note |\n")
            f.write("|:----|:-------:|:---------:|:----:|:--------:|:----:|\n")
            for port in sorted_port_list:
                f.write(
                    f'|{port["chart"]}|{port["service_name"]}|{port["port_name"]}|{port["port"] if port["port"] > 0 else "-"}|{port["protocol"]}|{port["note"]}|\n')
            f.write('\n\n')