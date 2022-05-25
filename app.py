from lib import apps_oper
from lib import services_oper
from lib import file_oper
import setup
import test


def main():
    ordered_trains = apps_oper.get_ordered_trains(apps_oper.get_trains())
    file_oper.delete_file(setup.PORT_LIST_FILE)
    # file_oper.delete_file(setup.VOLUME_LIST_FILE)
    file_oper.add_text_to_file(setup.PORT_LIST_FILE, setup.PORT_LIST_INTRO)
    # file_oper.add_text_to_file(setup.VOLUME_LIST_FILE, setup.VOLUME_LIST_INTRO)
    all_ports = []
    for train in ordered_trains:
        apps = apps_oper.get_apps(train)
        # Add the list that is returned to the services_list,
        # can't append is we will end up with a list of lists
        raw_services_list = (services_oper.get_raw_services_list(apps))
        ports_list = services_oper.get_processed_services_list(
            raw_services_list)
        all_ports += ports_list
        file_oper.create_port_list_file(ports_list, train.stem)
        # Later we can add a volumes_list etc
        # file_oper.create_volume_list_file(volume_list, train.stem)

    file_oper.add_text_to_file(setup.PORT_LIST_FILE, setup.PORT_LIST_OUTRO)
    # file_oper.add_text_to_file(setup.VOLUME_LIST_FILE, setup.VOLUME_LIST_OUTRO)
    test.get_conflicts(all_ports)


# TODO: Find conflicts
# TODO: Create volume list file
if __name__ == "__main__":
    main()
