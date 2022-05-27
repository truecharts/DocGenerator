# Path where trains are stored
TRAINS_PATH = "./charts"

# Name and path of the default port list file
PORT_LIST_FILE = "./default_port_list.md"

# Name and path of the default volume list file
VOLUME_LIST_FILE = "./default_volume_list.md"

# Print Verbose Output
VERBOSE = True

# Exclude specific trains
EXCLUDE_TRAINS = [
    "dev",
]

# Exclude specific apps
EXCLUDE_APPS = [
    "traefik",
]

# This ordered will be used,
# any trains not listed here and not excluded
# will be added automatically to the end
# Any trains not existing in file system will be ignored
TRAIN_ORDER_FOR_FILES = [
    "core",
    "stable",
    "games"
    "test_non_existing_train"
]


class Status:
    PORT_DIS = "Port is Disabled"
    PORT_UND = "Port not Defined"
    SVC_DIS = "Service is Disabled"
    SVC_UND = "Service not Defined"
    ACTIVE = "Active"


# VOLUME_LIST_INTRO="""INTRO"""
# VOLUME_LIST_OUTRO="""OUTRO"""

# OFFICIAL_APPS:[
#     {}
# ]
PORT_CONFLICT_NOTE = "Potential conflict with: "
PORT_LIST_INTRO = """
# Default Ports

This document lists the default ports used by Apps.
These defaults can of course be changed, but as we guarantee "sane, working defaults",
they should provide no or minimal conflicts without being changed
"""


PORT_LIST_OUTRO = """
## Official Apps

### Please keep mind that this list is not updated automatically like the rest of this doc.

| App        |   Service   | Port  |                   Note                    |
| :--------- | :---------: | :---: | :---------------------------------------: |
| chia       |    main     | 8444  |                                           |
| chia       | farmerPort  | 8447  |                                           |
| minio      |    main     | 9000  |      Potential conflict with traefik      |
| nextcloud  |    main     | 9001  |                                           |
| minio      | consolePort | 9002  |                                           |
| machinaris |    main     | 9003  |                                           |
| ipfs       |  swarmPort  | 9401  |                                           |
| ipfs       |   apiPort   | 9501  |                                           |
| ipfs       | gatewayPort | 9880  |                                           |
| collabora  |    main     | 9980  |                                           |
| plex       |    main     | 32400 | Potential conflict with plex (Truecharts) |

## TrueNAS Scale Services

### Please mind that this list is not updated automatically like the rest of this doc.

| Service | Port | Protocol | Note |
| :------ | :--: | :------: | :--: |
| ssh     |  22  |   TCP    |      |
| webui   |  80  |   HTTP   |      |
| webui   | 443  |  HTTPS   |      |

## Ports that are blocked in major web browsers

### Please mind that this list is not updated automatically like the rest of this doc.

| Port  |            Used by (example)             |
| :---: | :--------------------------------------: |
|   1   |                  tcpmux                  |
|   7   |                   echo                   |
|   9   |                 discard                  |
|  11   |                  systat                  |
|  13   |                 daytime                  |
|  15   |                 netstat                  |
|  17   |                   qotd                   |
|  19   |                 chargen                  |
|  20   |                 ftp data                 |
|  21   |                ftp access                |
|  22   |                   ssh                    |
|  23   |                  telnet                  |
|  25   |                   smtp                   |
|  37   |                   time                   |
|  42   |                   name                   |
|  43   |                 nicname                  |
|  53   |                  domain                  |
|  69   |                   tftp                   |
|  77   |                 priv-rjs                 |
|  79   |                  finger                  |
|  87   |                 ttylink                  |
|  95   |                  supdup                  |
|  101  |                hostriame                 |
|  102  |                 iso-tsap                 |
|  103  |                 gppitnp                  |
|  104  |                 acr-nema                 |
|  109  |                   pop2                   |
|  110  |                   pop3                   |
|  111  |                  sunrpc                  |
|  113  |                   auth                   |
|  115  |                   sftp                   |
|  117  |                uucp-path                 |
|  119  |                   nntp                   |
|  123  |                   NTP                    |
|  135  |              loc-srv /epmap              |
|  137  |                 netbios                  |
|  139  |                 netbios                  |
|  143  |                  imap2                   |
|  161  |                   snmp                   |
|  179  |                   BGP                    |
|  389  |                   ldap                   |
|  427  | SLP (Also used by Apple Filing Protocol) |
|  465  |                 smtp+ssl                 |
|  512  |               print / exec               |
|  513  |                  login                   |
|  514  |                  shell                   |
|  515  |                 printer                  |
|  526  |                  tempo                   |
|  530  |                 courier                  |
|  531  |                   chat                   |
|  532  |                 netnews                  |
|  540  |                   uucp                   |
|  548  |       AFP (Apple Filing Protocol)        |
|  554  |                   rtsp                   |
|  556  |                 remotefs                 |
|  563  |                 nntp+ssl                 |
|  587  |              smtp (rfc6409)              |
|  601  |          syslog-conn (rfc3195)           |
|  636  |                 ldap+ssl                 |
|  989  |                ftps-data                 |
|  990  |                   ftps                   |
|  993  |                 ldap+ssl                 |
|  995  |                 pop3+ssl                 |
| 1719  |               h323gatestat               |
| 1720  |               h323hostcall               |
| 1723  |                   pptp                   |
| 2049  |                   nfs                    |
| 3659  |       apple-sasl / PasswordServer        |
| 4045  |                  lockd                   |
| 5060  |                   sip                    |
| 5061  |                   sips                   |
| 6000  |                   X11                    |
| 6566  |                sane-port                 |
| 6665  |      Alternate IRC [Apple addition]      |
| 6666  |      Alternate IRC [Apple addition]      |
| 6667  |      Standard IRC [Apple addition]       |
| 6668  |      Alternate IRC [Apple addition]      |
| 6669  |      Alternate IRC [Apple addition]      |
| 6697  |                IRC + TLS                 |
| 10080 |                  Amanda                  |

# Note: TCP and UDP ports that are the same in some Apps, are not by mistake.

# If you notice a port conflict, please notify us so we can resolve it (when possible).
"""
