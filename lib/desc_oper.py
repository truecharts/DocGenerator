from lib import file_oper
from pathlib import Path
import setup
import copy


def get_description(app):
    """
    Returns the Description of an app
    """
    data = file_oper.get_values(Path.joinpath(app, "Chart.yaml"))
    clean_data = clean_strings(data['description'])

    return clean_data if 'description' in data else None


def get_home_url(app):
    """
    Returns the Home of an app
    """
    data = file_oper.get_values(Path.joinpath(app, "Chart.yaml"))

    return data['home'] if 'home' in data else setup.FALLBACK_URL


def get_icon(app):
    """
    Returns the Icon of an app
    """
    data = file_oper.get_values(Path.joinpath(app, "Chart.yaml"))

    return data['icon'] if 'icon' in data else setup.FALLBACK_URL


def clean_strings(string):
    """
    Some descriptions have line breaks, so we clean them here
    """
    return string \
        .replace('\n', " ") \
        .replace('\r', " ") \
        .replace('\\', " ") \
        .replace('\*', "*")


def get_descriptions_list(apps, train):
    """
    Returns a LIST of dicts
    Each Dict has the APP name and the DESCRIPTION
    """
    description_list = []
    for app in apps:
        description = get_description(app)
        home_url = get_home_url(app)
        icon = get_icon(app)
        if not description is None:
            description_list.append(create_row(
                app_name=app.stem, description=description, home_url=home_url, icon=icon, train=train))
        else:
            description_list.append(create_row(
                app_name=app.stem, description=False, home_url=home_url, icon=icon, train=train))
    return description_list


def create_row(app_name, description, home_url, icon, train):
    """
    Creates a row for the processed description list
    """
    if not description:
        description = setup.Status.NO_DESC
    return {
        "app_name": f'![]({icon})[{app_name}]({home_url})',
        "description": description,
        "train": train
    }


def create_description_list_content(description_list, train):
    """
    Creates and returns content to the description list file
    """
    content = ""
    filtered_list = copy.deepcopy(description_list)
    filtered_list = filter(lambda item: item['train'] == train, filtered_list)

    sorted_list = sorted(filtered_list, key=lambda item: item['app_name'])
    for x in sorted_list:
        del x['train']

    content += f'## {train.capitalize()}'
    content += '\n\n'
    content += "| App | Description |"
    content += '\n'
    content += "|:----|:------------|"
    content += '\n'
    # Check that table has data
    if sorted_list:
        content += file_oper.create_table(sorted_list)
        content += '\n\n'

    return content
