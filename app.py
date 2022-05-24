from lib import apps_oper
from lib import services_oper
from lib import file_oper
from helpers import setup


def main():
    trains = apps_oper.get_trains()
    # Later we can add a volumes_list etc
    # volumes_list = []
    file_oper.recreate_port_file()
    file_oper.add_intro_port_file()
    for train in trains:
        apps = apps_oper.get_apps(train)
        # Add the list that is returned to the services_list,
        # can't append is we will end up with a list of lists
        raw_services_list = (services_oper.get_raw_services_list(apps))
        ports_list = services_oper.get_processed_services_list(
            raw_services_list)
        file_oper.create_port_list(ports_list, train.stem)
    # TODO: Sorting based on trainorder, status, and port number and print to md file
    file_oper.add_closure_port_file()


if __name__ == "__main__":
    main()
