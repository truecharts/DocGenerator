from lib import apps_oper
from lib import services_oper


def main():
    trains = apps_oper.get_trains()
    services_list = []
    # Later we can add a volumes_list etc
    # volumes_list = []
    for train in trains:
        apps = apps_oper.get_apps(train)
        # Add the list that is returned to the services_list,
        # can't append is we will end up with a list of lists
        raw_services_list = (services_oper.get_raw_services_list(apps))
        services_list += services_oper.get_processed_services_list(
            raw_services_list)

    # TODO: Sorting based on trainorder, status, and port number and print to md file
    print(services_list)


if __name__ == "__main__":
    main()
