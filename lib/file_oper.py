from markdownTable import markdownTable
from pathlib import Path
from helpers import setup

port_file = Path(setup.PORT_LIST_FILE)
volume_file = Path(setup.VOLUME_LIST_FILE)


def delete_file(file):
    """
    Delets port file, so it gets recreated clean
    """
    if Path(file).exists():
        Path(file).unlink()


def add_text_to_file(file, intro):
    """
    Prints text to the file
    """
    with Path(file).open(mode='a', encoding='utf_8') as file:
        file.write(intro)


def create_table(port_list):
    """
    Returns a markdown list
    """
    # Generates a nice table with spacing
    table = markdownTable(port_list).setParams(
        padding_weight='right', row_sep='markdown', quote=False).getMarkdown()
    # Removes the first 2 lines (headers) as it uses the key from the dict which is not nice

    return table.split("\n", 2)[2]


def create_port_list_file(port_list, train):
    """
    Creates and prints content to the port list file
    """
    if port_file.exists():
        table = []
        svc_und_table = []
        svc_dis_table = []
        port_und_table = []
        port_dis_table = []
        active_table = []
        # Sort by name
        sorted_list = sorted(port_list, key=lambda item: item['app_name'])
        # Then sort by port number
        sorted_list = sorted(sorted_list, key=lambda item: item['port'])
        for port in sorted_list:
            # When there was no port, we have set port to 0
            # That was to be easier to sort the list
            # Before we print it, we make it "-"
            if not port['port']:
                port['port'] = "-"
            if port['status'] == setup.Status.SVC_UND:
                svc_und_table.append(port)
            if port['status'] == setup.Status.SVC_DIS:
                svc_dis_table.append(port)
            if port['status'] == setup.Status.PORT_UND:
                port_und_table.append(port)
            if port['status'] == setup.Status.PORT_DIS:
                port_dis_table.append(port)
            if port['status'] == setup.Status.ACTIVE:
                active_table.append(port)
        table = svc_und_table + svc_dis_table + \
            port_und_table+port_dis_table + active_table
        with port_file.open(mode='a', encoding='utf_8') as file:
            file.write(f'## {train.capitalize()}')
            file.write('\n\n')
            file.write(
                "| App | Service | Port Name | Port | Protocol | Status | Note |")
            file.write('\n')
            file.write(
                "|:----|:-------:|:---------:|:----:|:--------:|:------:|:----:|")
            file.write('\n')
            # Check that table has data
            if table:
                file.write(create_table(table))
                file.write('\n\n')
