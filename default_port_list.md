
# Default Ports

This document lists the default ports used by Apps.
These defaults can of course be changed, but as we guarantee "sane, working defaults" they should provide no or minimal conflicts without being changed
## Incubator

| App | Service | Port Name | Port | Protocol | Status | Note |
|:----|:-------:|:---------:|:----:|:--------:|:------:|:----:|
## Core

| App | Service | Port Name | Port | Protocol | Status | Note |
|:----|:-------:|:---------:|:----:|:--------:|:------:|:----:|
|metallb       |-       |-        |-   |-       |Service not Defined|-   |
|amd-gpu-plugin|-       |-        |-   |-       |Service not Defined|-   |## Stable

| App | Service | Port Name | Port | Protocol | Status | Note |
|:----|:-------:|:---------:|:----:|:--------:|:------:|:----:|
|custom-app                |-       |-        |-   |-       |Service not Defined|-   |
|webgrabplus               |main    |-        |-   |-       |Service is Disabled|-   |
|leaf2mqtt                 |main    |-        |-   |-       |Service is Disabled|-   |
|protonmail-bridge         |main    |-        |-   |-       |Service is Disabled|-   |
|doplarr                   |main    |-        |-   |-       |Service is Disabled|-   |
|duckdns                   |main    |-        |-   |-       |Service is Disabled|-   |
|ddclient                  |main    |-        |-   |-       |Service is Disabled|-   |
|tdarr-node                |main    |-        |-   |-       |Service is Disabled|-   |
|rsnapshot                 |main    |-        |-   |-       |Service is Disabled|-   |
|automatic-music-downloader|main    |-        |-   |-       |Service is Disabled|-   |
|unpackerr                 |main    |-        |-   |-       |Service is Disabled|-   |
|amcrest2mqtt              |main    |-        |-   |-       |Service is Disabled|-   |
|unifi                     |stun    |-        |-   |-       |Port not Defined   |-   |
|unpoller                  |-       |-        |-   |-       |Port is Disabled   |-   |
|promcord                  |-       |-        |-   |-       |Port is Disabled   |-   |
|unifi                     |-       |-        |-   |-       |Port is Disabled   |-   |
|uptimerobot-prometheus    |-       |-        |-   |-       |Port is Disabled   |-   |
|speedtest-exporter        |-       |-        |-   |-       |Port is Disabled   |-   |## Dependency

| App | Service | Port Name | Port | Protocol | Status | Note |
|:----|:-------:|:---------:|:----:|:--------:|:------:|:----:|
## Games

| App | Service | Port Name | Port | Protocol | Status | Note |
|:----|:-------:|:---------:|:----:|:--------:|:------:|:----:|

## Official Apps

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

| Service | Port | Protocol | Note |
| :------ | :--: | :------: | :--: |
| ssh     |  22  |   TCP    |      |
| webui   |  80  |   HTTP   |      |
| webui   | 443  |  HTTPS   |      |

## Ports that are blocked in major web browsers

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

# Note: TCP and UDP ports that are the same in some Apps, are not by mistake.'

# If you notice a port conflict, please notify us so we can resolve it (when possible).
