def get_conflicts(ports):
    """
    Returns a list of lists with ports/apps that have conflicts
    """
    conflicts = []
    for port in ports:
        # For each port... if the port is a number (It's not "-")
        if isinstance(port['port'], int):
            # Generate a list of port numbers(0 position holds the port numbers)
            conflicts = [conflict[0] for conflict in conflicts]
            # If the port number is in the... list
            if port['port'] in conflicts:
                # Get the index of the port number in the conflicts list
                index = conflicts.index(port['port'])
                # If the protocol of the port is the same as on the port in the mentioned index (1 position holds protocol)
                if port['protocol'] == conflicts[index][1]:
                    # Then append the app name to the to the list in posistion 2
                    conflicts[index][2].append(port['app_name'])
            else:
                # If the port number is in NOT the... list
                # Create it
                # Save, port number, protocol and app name
                conflicts.append(
                    [port['port'], port['protocol'], [port['app_name']]])
    # Get the real conflicts, by keeping only the ports that have more than one app in list in position 2
    conflicts = [c for c in conflicts if len(c[2]) > 1]
    # TODO: Add those conflicts to the notes column of the port list file
    print(conflicts)

# """
# Walk the port list
# if port number and protocol exists, increment (also save the name)
# if port number and protocol does not, set to 1 (also save the name)


# """
