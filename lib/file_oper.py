from markdownTable import markdownTable
from pathlib import Path
from helpers import setup

port_file = Path(setup.PORT_LIST_FILE)


def recreate_port_file():
    if port_file.exists():
        port_file.unlink()


def add_intro_port_file():
    with port_file.open(mode='a', encoding='utf_8') as file:
        file.write(setup.PORT_LIST_INTRO)


def add_closure_port_file():
    if port_file.exists():
        with port_file.open(mode='a', encoding='utf_8') as file:
            file.write(setup.PORT_LIST_CLOSURE)


def create_table(list):
    # Generates a nice table with spacing
    table = markdownTable(list).setParams(
        padding_weight='right', row_sep='markdown', quote=False).getMarkdown()
    # Removes the first 2 lines (headers) as it uses the key from the dict which is not nice

    # print(table.split("\n", 2)[2])
    return table.split("\n", 2)[2]


def create_port_list(port_list, train):
    if port_file.exists():
        with port_file.open(mode='a', encoding='utf_8') as file:
            file.write(f'## {train.capitalize()}')
            file.write('\n\n')
            file.write(
                "| App | Service | Port Name | Port | Protocol | Status | Note |")
            file.write('\n')
            file.write(
                "|:----|:-------:|:---------:|:----:|:--------:|:------:|:----:|")
            file.write('\n')

            for port in port_list:
                if port['status'] == setup.Status.SVC_UND:
                    table.append(port)
            for port in port_list:
                if port['status'] == setup.Status.SVC_DIS:
                    table.append(port)
            for port in port_list:
                if port['status'] == setup.Status.PORT_UND:
                    table.append(port)
            for port in port_list:
                if port['status'] == setup.Status.PORT_DIS:
                    table.append(port)
            for port in port_file:
                if port['stauts'] == setup.Status.ACTIVE:

            if table:
                file.write(create_table(table))
