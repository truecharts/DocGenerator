from pathlib import Path
from ruamel.yaml import YAML
from helpers.logger import logger

yaml = YAML()


def get_values(yaml_path):
    """
    Returns the yaml data of the path
    """

    return yaml.load(yaml_path)


def get_service(app):
    """
    Returns the SERVICE section of an app
    """
    data = get_values(Path.joinpath(app, "values.yaml"))

    return data['service'] if 'service' in data else None


def get_raw_services_list(apps):
    """
    Returns a LIST of dicts
    Each Dict has the APP name and the SERVICE Section
    """
    service_list = []
    for app in apps:
        service = get_service(app)
        if not service == None:
            service_list.append({"app_name": app.stem, "service": service})
        else:
            service_list.append(
                {"app_name": app.stem, "service": False})

    return service_list


def create_row(app_name, status, svc_name="-", port_name="-", port="-", protocol="-", note="-"):
    """
    Creates a row for the processes services list
    """
    if status == "port_dis":
        status = "Port is Disabled"
    if status == "port_und":
        status = "Port not Defined"
    if status == "svc_dis":
        status = "Service is Disabled"
    if status == "svc_und":
        status = "Service not Defined"
    return {
        "app_name": app_name,
        "svc_name": svc_name,
        "port_name": port_name,
        "port": port,
        "protocol": protocol,
        "status": "Service not Defined" if status == "svc_und" else status,
        "note": note
    }


def get_processed_services_list(raw_services_list):
    """
    Returns a processes list of services
    """
    services_list = []
    for service_section in raw_services_list:
        # If there is no service, create a row accordingly
        if not service_section['service']:
            logger(
                f'App: <{service_section["app_name"]}> has no Service Defined', "BLUE")
            services_list.append(create_row(
                app_name=service_section['app_name'],
                status="svc_und"
            ))
        else:
            # if there is service, process it
            for service in service_section['service'].items():
                services_list.append(process_service(
                    service, service_section['app_name']))

    return services_list


def process_service(service, app_name):
    """
    Processes the service and create rows
    """
    # If there is no "enabled" key, it's probably main. Assume service is enabled.
    # If there is "enabled" key and it's true, service is enabled
    # If there is "enabled" key and it's false, service is disabled
    if (not 'enabled' in service[1]) or ('enabled' in service[1] and service[1]['enabled']):
        # If there are no ports (This is probably unusual), but still create a row
        if not 'ports' in service[1]:
            logger(
                f'Service: <{service[0]}> of App: <{app_name}> has no ports defined', "RED")
            return create_row(
                app_name=app_name,
                status="port_und",
                svc_name=service[0]
            )
        else:
            for port in service[1]['ports'].items():
                processed_port = process_port(port, app_name)
                return create_row(
                    app_name=app_name,
                    status=processed_port['status']
                ) if 'port' not in processed_port else create_row(
                    app_name=app_name,
                    status=processed_port['status'],
                    svc_name=service[0],
                    port_name=processed_port['port_name'],
                    port=processed_port['port'],
                    protocol=processed_port['protocol']
                )
    else:
        logger(
            f'App: <{app_name}> has it\'s Services Disabled', "BLUE")
        return create_row(
            app_name=app_name,
            status="svc_dis",
            svc_name=service[0]
        )


def process_port(port, app_name):
    """
    Returns a processed port
    """
    # If there is no "enabled" key, it's probably main. Assume port is enabled.
    # If there is "enabled" key and it's true, port is enabled
    # If there is "enabled" key and it's false, port is disabled
    if (not 'enabled' in port[1]) or ('enabled' in port[1] and port[1]['enabled']):
        return {
            "port_name": port[0],
            "port": port[1]['port'],
            "protocol": port[1]['protocol'] if 'protocol' in port[1] else "TCP",
            "status": "Active"
        }
    else:
        logger(f'Port <{port[0]}> of App: <{app_name}> is Disabled', "YELLOW")
        return {"port_name": port[0], "status": "port_dis"}
