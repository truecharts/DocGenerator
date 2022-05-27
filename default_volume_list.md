
# Mounted Volumes

This document lists the mounted volumes for each App.
The intro needs improvement ;)
## Core

| App | Volume Name | Type | Host Path | Mount Path | Mode | Status | Note |
|:----|:-----------:|:----:|:---------:|:----------:|:----:|:------:|:----:|
|amd-gpu-plugin  |-              |-       |-       |-        |Read/Write|Persistence not Defined|-   |
|external-service|-              |-       |-       |-        |Read/Write|Persistence not Defined|-   |
|k8s-gateway     |-              |-       |-       |-        |Read/Write|Persistence not Defined|-   |
|metallb         |-              |-       |-       |-        |Read/Write|Persistence not Defined|-   |
|prometheus      |-              |-       |-       |-        |Read/Write|Persistence not Defined|-   |
|traefik         |-              |-       |-       |-        |Read/Write|Persistence not Defined|-   |
|docker-compose  |varrun         |emptyDir|-       |-        |Read/Write|Persistence is Disabled|-   |
|docker-compose  |mnt            |hostPath|/mnt    |/mnt     |Read/Write|Enabled                |-   |
|docker-compose  |root           |hostPath|/root   |/root    |Read/Write|Enabled                |-   |
|docker-compose  |cluster        |hostPath|/cluster|/cluster |Read/Write|Enabled                |-   |
|docker-compose  |docker-certs-ca|PVC     |-       |/config  |Read/Write|Enabled                |-   |

## Stable

| App | Volume Name | Type | Host Path | Mount Path | Mode | Status | Note |
|:----|:-----------:|:----:|:---------:|:----------:|:----:|:------:|:----:|
|amcrest2mqtt              |-              |-        |-           |-                                   |Read/Write|Persistence not Defined|-   |
|apache-musicindex         |-              |-        |-           |-                                   |Read/Write|Persistence not Defined|-   |
|collabora-online          |-              |-        |-           |-                                   |Read/Write|Persistence not Defined|-   |
|custom-app                |-              |-        |-           |-                                   |Read/Write|Persistence not Defined|-   |
|cyberchef                 |-              |-        |-           |-                                   |Read/Write|Persistence not Defined|-   |
|doplarr                   |-              |-        |-           |-                                   |Read/Write|Persistence not Defined|-   |
|drawio                    |-              |-        |-           |-                                   |Read/Write|Persistence not Defined|-   |
|fluidd                    |-              |-        |-           |-                                   |Read/Write|Persistence not Defined|-   |
|guacd                     |-              |-        |-           |-                                   |Read/Write|Persistence not Defined|-   |
|kms                       |-              |-        |-           |-                                   |Read/Write|Persistence not Defined|-   |
|kutt                      |-              |-        |-           |-                                   |Read/Write|Persistence not Defined|-   |
|leaf2mqtt                 |-              |-        |-           |-                                   |Read/Write|Persistence not Defined|-   |
|leantime                  |-              |-        |-           |-                                   |Read/Write|Persistence not Defined|-   |
|littlelink                |-              |-        |-           |-                                   |Read/Write|Persistence not Defined|-   |
|onlyoffice-document-server|-              |-        |-           |-                                   |Read/Write|Persistence not Defined|-   |
|outline                   |-              |-        |-           |-                                   |Read/Write|Persistence not Defined|-   |
|pretend-youre-xyzzy       |-              |-        |-           |-                                   |Read/Write|Persistence not Defined|-   |
|promcord                  |-              |-        |-           |-                                   |Read/Write|Persistence not Defined|-   |
|rsshub                    |-              |-        |-           |-                                   |Read/Write|Persistence not Defined|-   |
|shlink                    |-              |-        |-           |-                                   |Read/Write|Persistence not Defined|-   |
|shlink-web-client         |-              |-        |-           |-                                   |Read/Write|Persistence not Defined|-   |
|speedtest-exporter        |-              |-        |-           |-                                   |Read/Write|Persistence not Defined|-   |
|spotweb                   |-              |-        |-           |-                                   |Read/Write|Persistence not Defined|-   |
|unpoller                  |-              |-        |-           |-                                   |Read/Write|Persistence not Defined|-   |
|uptimerobot-prometheus    |-              |-        |-           |-                                   |Read/Write|Persistence not Defined|-   |
|openldap                  |varrun         |emptyDir |-           |-                                   |Read/Write|Persistence is Disabled|-   |
|phpldapadmin              |varrun         |emptyDir |-           |-                                   |Read/Write|Persistence is Disabled|-   |
|anonaddy                  |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|appdaemon                 |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|aria2                     |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|audacity                  |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|babybuddy                 |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|beets                     |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|boinc                     |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|bookstack                 |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|budge                     |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|calibre                   |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|clarkson                  |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|cloud9                    |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|couchpotato               |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|darktable                 |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|davos                     |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|ddclient                  |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|deluge                    |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|digikam                   |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|dillinger                 |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|domoticz                  |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|doublecommander           |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|duckdns                   |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|embystat                  |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|emulatorjs                |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|endlessh                  |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|filezilla                 |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|firefox                   |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|fleet                     |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|foldingathome             |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|fossil                    |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|friendica                 |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|golinks                   |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|grav                      |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|habridge                  |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|headphones                |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|hedgedoc                  |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|htpcmanager               |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|kodi-headless             |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|lazylibrarian             |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|libreoffice               |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|medusa                    |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|minio-console             |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|minisatip                 |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|mstream                   |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|muximux                   |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|mylar                     |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|mysql-workbench           |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|nano-wallet               |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|ngircd                    |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|nntp2nntp                 |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|novnc                     |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|octoprint                 |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|openvscode-server         |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|oscam                     |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|papermerge                |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|photoshow                 |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|pidgin                    |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|pixapop                   |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|projectsend               |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|pwndrop                   |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|pyload                    |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|pylon                     |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|quassel-core              |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|quassel-web               |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|remmina                   |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|requestrr                 |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|resilio-sync              |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|rsnapshot                 |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|scrutiny                  |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|shiori                    |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|shorturl                  |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|sickchill                 |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|sickgear                  |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|sqlitebrowser             |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|static                    |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|synclounge                |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|syslog-ng                 |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|tdarr                     |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|tdarr-node                |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|tvheadend                 |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|twtxt                     |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|ubooquity                 |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|unmanic                   |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|webgrabplus               |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|wireshark                 |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|znc                       |varrun         |emptyDir |-           |/var/run                            |Read/Write|Mount Path not Defined |-   |
|airdcpp-webclient         |config         |PVC      |-           |/.airdcpp                           |Read/Write|Enabled                |-   |
|airsonic                  |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|airsonic-advanced         |config         |PVC      |-           |/airsonic                           |Read/Write|Enabled                |-   |
|airsonic-advanced         |music          |PVC      |-           |/music                              |Read/Write|Enabled                |-   |
|airsonic-advanced         |podcasts       |PVC      |-           |/podcasts                           |Read/Write|Enabled                |-   |
|airsonic-advanced         |playlists      |PVC      |-           |/playlists                          |Read/Write|Enabled                |-   |
|alist                     |data           |PVC      |-           |/opt/alist/data                     |Read/Write|Enabled                |-   |
|anonaddy                  |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|appdaemon                 |conf           |PVC      |-           |/conf                               |Read/Write|Enabled                |-   |
|aria2                     |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|audacity                  |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|audiobookshelf            |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|audiobookshelf            |audiobooks     |PVC      |-           |/audiobooks                         |Read/Write|Enabled                |-   |
|audiobookshelf            |metadata       |PVC      |-           |/metadata                           |Read/Write|Enabled                |-   |
|authelia                  |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|automatic-music-downloader|config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|automatic-music-downloader|data           |PVC      |-           |/downloads-amd                      |Read/Write|Enabled                |-   |
|babybuddy                 |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|bazarr                    |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|beets                     |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|blog                      |data           |PVC      |-           |/var/www/html/data                  |Read/Write|Enabled                |-   |
|boinc                     |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|booksonic-air             |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|bookstack                 |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|browserless-chrome        |downloads      |PVC      |-           |/downloads                          |Read/Write|Enabled                |-   |
|browserless-chrome        |metrics        |PVC      |-           |/metrics                            |Read/Write|Enabled                |-   |
|budge                     |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|calibre                   |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|calibre-web               |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|chevereto                 |storage        |PVC      |-           |/var/www/html/images/               |Read/Write|Enabled                |-   |
|chevereto                 |content        |PVC      |-           |/var/www/html/content/              |Read/Write|Enabled                |-   |
|clamav                    |sigdatabase    |PVC      |-           |/var/lib/clamav                     |Read/Write|Enabled                |-   |
|clamav                    |scandir        |PVC      |-           |/scandir                            |Read Only |Enabled                |-   |
|clamav                    |logs           |PVC      |-           |/logs                               |Read/Write|Enabled                |-   |
|cloud9                    |code           |PVC      |-           |/code                               |Read/Write|Enabled                |-   |
|code-server               |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|couchpotato               |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|cryptofolio               |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|darktable                 |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|davos                     |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|ddclient                  |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|ddns-go                   |data           |PVC      |-           |/root                               |Read/Write|Enabled                |-   |
|ddns-updater              |data           |PVC      |-           |/updater/data                       |Read/Write|Enabled                |-   |
|deconz                    |config         |PVC      |-           |/opt/deCONZ                         |Read/Write|Enabled                |-   |
|deemix                    |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|deemix                    |data           |PVC      |-           |/downloads                          |Read/Write|Enabled                |-   |
|deepstack                 |data           |PVC      |-           |/datastore                          |Read/Write|Enabled                |-   |
|deepstack                 |modelstore     |PVC      |-           |/modelstore/detection               |Read/Write|Enabled                |-   |
|deluge                    |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|digikam                   |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|dillinger                 |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|dizquetv                  |config         |PVC      |-           |/home/node/app/.dizquetv            |Read/Write|Enabled                |-   |
|dokuwiki                  |config         |PVC      |-           |/bitnami/dokuwiki                   |Read/Write|Enabled                |-   |
|domoticz                  |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|double-take               |data           |PVC      |-           |/.storage                           |Read/Write|Enabled                |-   |
|doublecommander           |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|dsmr-reader               |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|duckdns                   |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|duplicati                 |config         |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|emby                      |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|embystat                  |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|emulatorjs                |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|endlessh                  |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|esphome                   |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|esphome                   |platformio     |PVC      |-           |/.platformio                        |Read/Write|Enabled                |-   |
|etherpad                  |data           |PVC      |-           |/opt/etherpad-lite/var              |Read/Write|Enabled                |-   |
|etherpad                  |app            |PVC      |-           |/opt/etherpad-lite/app              |Read/Write|Enabled                |-   |
|ferdi-server              |data           |PVC      |-           |/app/data                           |Read/Write|Enabled                |-   |
|ferdi-server              |recipes        |PVC      |-           |/app/recipes                        |Read/Write|Enabled                |-   |
|filebrowser               |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|filebrowser               |database       |PVC      |-           |/database                           |Read/Write|Enabled                |-   |
|filebrowser               |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|filezilla                 |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|fireflyiii                |data           |PVC      |-           |/var/www/html/storage/upload        |Read/Write|Enabled                |-   |
|firefox                   |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|firefox-syncserver        |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|flaresolverr              |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|fleet                     |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|flexget                   |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|flexget                   |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|flood                     |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|focalboard                |uploads        |PVC      |-           |/uploads                            |Read/Write|Enabled                |-   |
|foldingathome             |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|freeradius                |config         |PVC      |-           |/etc/raddb                          |Read/Write|Enabled                |-   |
|freshrss                  |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|friendica                 |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|friendica                 |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|gaps                      |data           |PVC      |-           |/usr/data                           |Read/Write|Enabled                |-   |
|gitea                     |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|gitea                     |temp           |emptyDir |-           |/tmp                                |Read/Write|Enabled                |-   |
|gitea                     |varlib         |emptyDir |-           |/var/lib/gitea                      |Read/Write|Enabled                |-   |
|golinks                   |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|gonic                     |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|gotify                    |data           |PVC      |-           |/app/data                           |Read/Write|Enabled                |-   |
|grafana                   |config         |PVC      |-           |/opt/bitnami/grafana/data           |Read/Write|Enabled                |-   |
|grav                      |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|grist                     |persist        |PVC      |-           |/persist                            |Read/Write|Enabled                |-   |
|grocy                     |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|guacamole-client          |initdbdata     |PVC      |-           |/initdbdata                         |Read/Write|Enabled                |-   |
|guacamole-client          |temphack       |PVC      |-           |/opt/guacamole/postgresql-hack      |Read/Write|Enabled                |-   |
|guacamole-client          |temphackalso   |PVC      |-           |/opt/guacamole/postgresql           |Read/Write|Enabled                |-   |
|habridge                  |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|hammond                   |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|hammond                   |assets         |PVC      |-           |/assets                             |Read/Write|Enabled                |-   |
|handbrake                 |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|handbrake                 |storage        |PVC      |-           |/storage                            |Read/Write|Enabled                |-   |
|handbrake                 |output         |PVC      |-           |/output                             |Read/Write|Enabled                |-   |
|haste-server              |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|headphones                |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|healthchecks              |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|heimdall                  |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|home-assistant            |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|homer                     |config         |PVC      |-           |/www/assets                         |Read/Write|Enabled                |-   |
|htpcmanager               |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|hyperion-ng               |config         |PVC      |-           |/root/.hyperion                     |Read/Write|Enabled                |-   |
|icantbelieveitsnotvaletudo|config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|icinga2                   |config         |PVC      |-           |/etc/icinga2                        |Read/Write|Enabled                |-   |
|icinga2                   |data           |PVC      |-           |/var/lib/icinga2                    |Read/Write|Enabled                |-   |
|icinga2                   |web            |PVC      |-           |/etc/icingaweb2                     |Read/Write|Enabled                |-   |
|icinga2                   |ssmtp          |PVC      |-           |/etc/ssmtp                          |Read/Write|Enabled                |-   |
|ipfs                      |data           |PVC      |-           |/data/ipfs                          |Read/Write|Enabled                |-   |
|ipfs                      |staging        |PVC      |-           |/export                             |Read/Write|Enabled                |-   |
|ipfs                      |ipfs           |PVC      |-           |/ipfs                               |Read/Write|Enabled                |-   |
|ipfs                      |ipns           |PVC      |-           |/ipns                               |Read/Write|Enabled                |-   |
|ispy-agent-dvr            |config         |PVC      |-           |/agent/Media/XML                    |Read/Write|Enabled                |-   |
|ispy-agent-dvr            |media          |PVC      |-           |/agent/Media/WebServerRoot/Media    |Read/Write|Enabled                |-   |
|ispy-agent-dvr            |commands       |PVC      |-           |/agent/Commands                     |Read/Write|Enabled                |-   |
|iyuuplus                  |config         |PVC      |-           |/IYUU/db                            |Read/Write|Enabled                |-   |
|iyuuplus                  |torrents       |PVC      |-           |/torrents                           |Read/Write|Enabled                |-   |
|iyuuplus                  |btbackup       |PVC      |-           |/BT_backup                          |Read/Write|Enabled                |-   |
|jackett                   |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|jdownloader2              |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|jdownloader2              |output         |PVC      |-           |/output                             |Read/Write|Enabled                |-   |
|jellyfin                  |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|jellyfin                  |cache          |emptyDir |-           |/cache                              |Read/Write|Enabled                |-   |
|joplin-server             |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|kanboard                  |data           |PVC      |-           |/var/www/app/data                   |Read/Write|Enabled                |-   |
|kanboard                  |ssl            |PVC      |-           |/etc/nginx/ssl                      |Read/Write|Enabled                |-   |
|kavita                    |config         |PVC      |-           |/kavita/config                      |Read/Write|Enabled                |-   |
|kavita                    |manga          |PVC      |-           |/manga                              |Read/Write|Enabled                |-   |
|kimai                     |data           |PVC      |-           |/opt/kimai/var/data                 |Read/Write|Enabled                |-   |
|kimai                     |plugins        |PVC      |-           |/opt/kimai/var/plugins              |Read/Write|Enabled                |-   |
|kodi-headless             |config         |PVC      |-           |/config/.kodi                       |Read/Write|Enabled                |-   |
|koel                      |music          |PVC      |-           |/music                              |Read/Write|Enabled                |-   |
|koel                      |covers         |PVC      |-           |/var/www/html/public/img/covers     |Read/Write|Enabled                |-   |
|koel                      |searchindex    |PVC      |-           |/var/www/html/storage/search-indexes|Read/Write|Enabled                |-   |
|komga                     |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|komga                     |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|lanraragi                 |config         |PVC      |-           |/home/koyomi/lanraragi/database     |Read/Write|Enabled                |-   |
|lanraragi                 |content        |PVC      |-           |/home/koyomi/lanraragi/content      |Read/Write|Enabled                |-   |
|lazylibrarian             |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|libreoffice               |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|librephotos               |media          |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|librephotos               |protected-media|PVC      |-           |/protected_media                    |Read/Write|Enabled                |-   |
|librephotos               |logs           |PVC      |-           |/logs                               |Read/Write|Enabled                |-   |
|librephotos               |cache          |PVC      |-           |/root/.cache                        |Read/Write|Enabled                |-   |
|librespeed                |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|lidarr                    |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|linkace                   |app            |PVC      |-           |/app                                |Read/Write|Enabled                |-   |
|linkace                   |logs           |PVC      |-           |/app/storage/logs                   |Read/Write|Enabled                |-   |
|linkace                   |backups        |PVC      |-           |/app/storage/app/backups            |Read/Write|Enabled                |-   |
|linkding                  |data           |PVC      |-           |/etc/linkding/data                  |Read/Write|Enabled                |-   |
|logitech-media-server     |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|loki                      |config         |secret   |-           |/etc/loki                           |Read/Write|Enabled                |-   |
|lychee                    |conf           |PVC      |-           |/conf                               |Read/Write|Enabled                |-   |
|lychee                    |sym            |PVC      |-           |/sym                                |Read/Write|Enabled                |-   |
|lychee                    |uploads        |PVC      |-           |/uploads                            |Read/Write|Enabled                |-   |
|makemkv                   |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|makemkv                   |storage        |PVC      |-           |/storage                            |Read/Write|Enabled                |-   |
|makemkv                   |output         |PVC      |-           |/output                             |Read/Write|Enabled                |-   |
|matomo                    |data           |PVC      |-           |/bitnami/matomo                     |Read/Write|Enabled                |-   |
|mealie                    |config         |PVC      |-           |/app/data                           |Read/Write|Enabled                |-   |
|medusa                    |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|metube                    |downloads      |PVC      |-           |/downloads                          |Read/Write|Enabled                |-   |
|miniflux                  |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|minio                     |config         |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|minio-console             |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|minisatip                 |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|mkvtoolnix                |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|mkvtoolnix                |storage        |PVC      |-           |/storage                            |Read/Write|Enabled                |-   |
|ml-workspace              |workspace      |PVC      |-           |/workspace                          |Read/Write|Enabled                |-   |
|ml-workspace              |shm            |emptyDir |-           |/dev/shm                            |Read/Write|Enabled                |-   |
|monica                    |config         |PVC      |-           |/var/www/html/storage               |Read/Write|Enabled                |-   |
|mosdns                    |data           |PVC      |-           |/etc/mosdns                         |Read/Write|Enabled                |-   |
|mosquitto                 |data           |PVC      |-           |/mosquitto/data                     |Read/Write|Enabled                |-   |
|mosquitto                 |configinc      |PVC      |-           |/mosquitto/configinc                |Read/Write|Enabled                |-   |
|mstream                   |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|muximux                   |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|mylar                     |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|mysql-workbench           |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|n8n                       |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|navidrome                 |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|nextcloud                 |data           |PVC      |-           |/var/www/html                       |Read/Write|Enabled                |-   |
|nextpvr                   |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|nextpvr                   |recordings     |PVC      |-           |/recordings                         |Read/Write|Enabled                |-   |
|nextpvr                   |buffer         |PVC      |-           |/buffer                             |Read/Write|Enabled                |-   |
|ngircd                    |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|nntp2nntp                 |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|nocodb                    |data           |PVC      |-           |/usr/app/data                       |Read/Write|Enabled                |-   |
|node-red                  |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|ntfy                      |config         |PVC      |-           |/etc/ntfy                           |Read/Write|Enabled                |-   |
|ntfy                      |cache          |PVC      |-           |/var/cache/ntfy                     |Read/Write|Enabled                |-   |
|nullserv                  |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|nzbget                    |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|nzbhydra                  |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|octoprint                 |data           |PVC      |-           |/octoprint                          |Read/Write|Enabled                |-   |
|odoo                      |odoo           |PVC      |-           |/var/lib/odoo                       |Read/Write|Enabled                |-   |
|odoo                      |addons         |PVC      |-           |/mnt/extra-addons                   |Read/Write|Enabled                |-   |
|omada-controller          |data           |PVC      |-           |/opt/tplink/EAPController/data      |Read/Write|Enabled                |-   |
|omada-controller          |work           |PVC      |-           |/opt/tplink/EAPController/work      |Read/Write|Enabled                |-   |
|ombi                      |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|openhab                   |config         |PVC      |-           |/openhab/conf                       |Read/Write|Enabled                |-   |
|openhab                   |addons         |PVC      |-           |/openhab/addons                     |Read/Write|Enabled                |-   |
|openhab                   |userdata       |PVC      |-           |/openhab/userdata                   |Read/Write|Enabled                |-   |
|openkm                    |config         |PVC      |-           |/opt/tomcat/repository              |Read/Write|Enabled                |-   |
|openvscode-server         |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|organizr                  |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|organizr                  |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|oscam                     |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|overseerr                 |config         |PVC      |-           |/app/config                         |Read/Write|Enabled                |-   |
|owncast                   |config         |PVC      |-           |/app/data                           |Read/Write|Enabled                |-   |
|owncloud-ocis             |data           |PVC      |-           |/var/lib/ocis                       |Read/Write|Enabled                |-   |
|paperless-ng              |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|paperless-ng              |consume        |PVC      |-           |/consume                            |Read/Write|Enabled                |-   |
|paperless-ng              |media          |PVC      |-           |/media                              |Read/Write|Enabled                |-   |
|papermerge                |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|pgadmin                   |config         |PVC      |-           |/var/lib/pgadmin                    |Read/Write|Enabled                |-   |
|photoprism                |storage        |PVC      |-           |/assets                             |Read/Write|Enabled                |-   |
|photoprism                |temp           |emptyDir |-           |/photoprism/temp                    |Read/Write|Enabled                |-   |
|photoshow                 |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|photoview                 |cache          |PVC      |-           |/cache                              |Read/Write|Enabled                |-   |
|photoview                 |photos         |PVC      |-           |/photos                             |Read/Write|Enabled                |-   |
|piaware                   |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|picoshare                 |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|pidgin                    |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|pihole                    |config         |PVC      |-           |/etc/pihole                         |Read/Write|Enabled                |-   |
|pihole                    |dnsmasq        |PVC      |-           |/etc/dnsmasq.d                      |Read/Write|Enabled                |-   |
|pinry                     |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|pixapop                   |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|plex                      |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|podgrab                   |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|projectsend               |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|projectsend               |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|protonmail-bridge         |config         |PVC      |-           |/root                               |Read/Write|Enabled                |-   |
|prowlarr                  |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|pwndrop                   |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|pydio-cells               |cells          |PVC      |-           |/cells                              |Read/Write|Enabled                |-   |
|pydio-cells               |data           |PVC      |-           |/cells/data                         |Read/Write|Enabled                |-   |
|pydio-cells               |logs           |PVC      |-           |/cells/logs                         |Read/Write|Enabled                |-   |
|pydio-cells               |services       |PVC      |-           |/cells/services                     |Read/Write|Enabled                |-   |
|pyload                    |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|pylon                     |code           |PVC      |-           |/code                               |Read/Write|Enabled                |-   |
|qbittorrent               |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|qinglong                  |data           |PVC      |-           |/ql/data                            |Read/Write|Enabled                |-   |
|quassel-web               |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|radarr                    |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|readarr                   |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|recipes                   |media          |PVC      |-           |/opt/recipes/mediafiles             |Read/Write|Enabled                |-   |
|recipes                   |static         |emptyDir |-           |/opt/recipes/staticfiles            |Read/Write|Enabled                |-   |
|redmine                   |data           |PVC      |-           |/usr/src/redmine/files              |Read/Write|Enabled                |-   |
|reg                       |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|remmina                   |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|requestrr                 |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|resilio-sync              |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|rsnapshot                 |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|rss-bridge                |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|sabnzbd                   |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|scrutiny                  |config         |PVC      |-           |/scrutiny/config                    |Read/Write|Enabled                |-   |
|scrutiny                  |data           |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|scrutiny                  |udev           |hostPath |/run/udev   |/run/udev                           |Read Only |Enabled                |-   |
|ser2sock                  |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|shiori                    |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|shorturl                  |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|sickchill                 |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|sickgear                  |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|smokeping                 |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|smokeping                 |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|snapdrop                  |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|snipe-it                  |logs           |PVC      |-           |/var/www/html/storage/logs          |Read/Write|Enabled                |-   |
|snipe-it                  |data           |PVC      |-           |/var/lib/snipeit/data               |Read/Write|Enabled                |-   |
|snipe-it                  |backups        |PVC      |-           |/var/lib/snipeit/dumps              |Read/Write|Enabled                |-   |
|sonarr                    |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|sqlitebrowser             |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|stash                     |config         |PVC      |-           |/root/.stash                        |Read/Write|Enabled                |-   |
|static                    |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|statping                  |data           |PVC      |-           |/app                                |Read/Write|Enabled                |-   |
|storj-node                |identity       |PVC      |-           |/app/identity                       |Read/Write|Enabled                |-   |
|storj-node                |storage        |PVC      |-           |/app/config                         |Read/Write|Enabled                |-   |
|strapi                    |data           |PVC      |-           |/srv/app                            |Read/Write|Enabled                |-   |
|synapse                   |config         |configMap|-           |/data                               |Read/Write|Enabled                |-   |
|synapse                   |secret         |secret   |-           |/data/secret                        |Read/Write|Enabled                |-   |
|synapse                   |key            |PVC      |-           |/data/keys                          |Read/Write|Enabled                |-   |
|synapse                   |media          |PVC      |-           |/data/media_store                   |Read/Write|Enabled                |-   |
|synapse                   |uploads        |PVC      |-           |/uploads                            |Read/Write|Enabled                |-   |
|syncthing                 |config         |PVC      |-           |/var/syncthing                      |Read/Write|Enabled                |-   |
|syslog-ng                 |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|tautulli                  |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|tdarr                     |configs        |PVC      |-           |/app/configs                        |Read/Write|Enabled                |-   |
|tdarr                     |server         |PVC      |-           |/app/server                         |Read/Write|Enabled                |-   |
|tdarr                     |logs           |PVC      |-           |/app/logs                           |Read/Write|Enabled                |-   |
|tdarr                     |transcode-cache|PVC      |-           |/temp                               |Read/Write|Enabled                |-   |
|tdarr                     |media          |PVC      |-           |/media                              |Read/Write|Enabled                |-   |
|tdarr-node                |configs        |PVC      |-           |/app/configs                        |Read/Write|Enabled                |-   |
|tdarr-node                |logs           |PVC      |-           |/app/logs                           |Read/Write|Enabled                |-   |
|tdarr-node                |transcode-cache|PVC      |-           |/temp                               |Read/Write|Enabled                |-   |
|tdarr-node                |media          |PVC      |-           |/media                              |Read/Write|Enabled                |-   |
|teamspeak3                |data           |PVC      |-           |/var/ts3server                      |Read/Write|Enabled                |-   |
|teedy                     |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|thelounge                 |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|tinymediamanager          |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|tinymediamanager          |movies         |PVC      |-           |/media/movies                       |Read/Write|Enabled                |-   |
|tinymediamanager          |tvshows        |PVC      |-           |/media/tvshows                      |Read/Write|Enabled                |-   |
|traccar                   |data           |PVC      |-           |/opt/traccar/data                   |Read/Write|Enabled                |-   |
|transmission              |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|trilium-notes             |config         |PVC      |-           |/trilium-data                       |Read/Write|Enabled                |-   |
|truecommand               |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|tt-rss                    |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|tvheadend                 |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|twtxt                     |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|twtxt                     |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|typecho                   |config         |PVC      |-           |/app/usr                            |Read/Write|Enabled                |-   |
|ubooquity                 |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|ubooquity                 |books          |PVC      |-           |/books                              |Read/Write|Enabled                |-   |
|ubooquity                 |comics         |PVC      |-           |/comics                             |Read/Write|Enabled                |-   |
|ubooquity                 |files          |PVC      |-           |/files                              |Read/Write|Enabled                |-   |
|unifi                     |config         |PVC      |-           |/unifi                              |Read/Write|Enabled                |-   |
|unmanic                   |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|unmanic                   |library        |PVC      |-           |/library                            |Read/Write|Enabled                |-   |
|unmanic                   |remote         |PVC      |-           |/tmp/unmanic/remote_library         |Read/Write|Enabled                |-   |
|unmanic                   |cache          |emptyDir |-           |/tmp/unmanic                        |Read/Write|Enabled                |-   |
|unpackerr                 |downloads      |PVC      |-           |/downloads                          |Read/Write|Enabled                |-   |
|uptime-kuma               |config         |PVC      |-           |/app/data                           |Read/Write|Enabled                |-   |
|vaultwarden               |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|verysync                  |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|verysync                  |sync           |PVC      |-           |/Sync                               |Read/Write|Enabled                |-   |
|vikunja                   |files          |PVC      |-           |/app/vikunja/files                  |Read/Write|Enabled                |-   |
|webgrabplus               |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|webgrabplus               |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|weblate                   |config         |PVC      |-           |/app/data                           |Read/Write|Enabled                |-   |
|weblate                   |cache          |emptyDir |-           |/app/cache                          |Read/Write|Enabled                |-   |
|website-shot              |screenshots    |PVC      |-           |/usr/src/website-shot/screenshots   |Read/Write|Enabled                |-   |
|wekan                     |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|whoogle                   |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|wikijs                    |wikicache      |emptyDir |-           |/wiki/data/                         |Read/Write|Enabled                |-   |
|wireshark                 |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|xbackbone                 |config         |PVC      |-           |/app/config                         |Read/Write|Enabled                |-   |
|xteve                     |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|xwiki                     |config         |PVC      |-           |/usr/local/xwiki                    |Read/Write|Enabled                |-   |
|zerotier                  |config         |PVC      |-           |/var/lib/zerotier-one               |Read/Write|Enabled                |-   |
|zerotier                  |tun            |hostPath |/dev/net/tun|/dev/net/tun                        |Read/Write|Enabled                |-   |
|zigbee2mqtt               |data           |PVC      |-           |/data                               |Read/Write|Enabled                |-   |
|znc                       |config         |PVC      |-           |/config                             |Read/Write|Enabled                |-   |
|zwavejs2mqtt              |config         |PVC      |-           |/usr/src/app/store                  |Read/Write|Enabled                |-   |

## Incubator

| App | Volume Name | Type | Host Path | Mount Path | Mode | Status | Note |
|:----|:-----------:|:----:|:---------:|:----------:|:----:|:------:|:----:|
|piwigo               |varrun        |emptyDir|-              |/var/run                                |Read/Write|Mount Path not Defined|-   |
|adguard-home         |config        |PVC     |-              |/opt/adguardhome/conf                   |Read/Write|Enabled               |-   |
|adguard-home         |data          |PVC     |-              |/opt/adguardhome/work                   |Read/Write|Enabled               |-   |
|appsmith             |appsmithstacks|PVC     |-              |/appsmith-stacks                        |Read/Write|Enabled               |-   |
|authentik            |media         |PVC     |-              |/media                                  |Read/Write|Enabled               |-   |
|authentik            |templates     |PVC     |-              |/templates                              |Read/Write|Enabled               |-   |
|authentik            |certs         |PVC     |-              |/certs                                  |Read/Write|Enabled               |-   |
|authentik            |geoip         |PVC     |-              |/geoip                                  |Read/Write|Enabled               |-   |
|baserow              |data          |PVC     |-              |/baserow/data                           |Read/Write|Enabled               |-   |
|cups-server          |config        |PVC     |-              |/etc/cups                               |Read/Write|Enabled               |-   |
|cups-server          |dbus          |hostPath|/var/run/dbus  |/var/run/dbus                           |Read/Write|Enabled               |-   |
|filerun              |config        |PVC     |-              |/var/www/html                           |Read/Write|Enabled               |-   |
|filerun              |userfile      |PVC     |-              |/user-files                             |Read/Write|Enabled               |-   |
|frigate              |cache         |emptyDir|-              |/tmp/cache                              |Read/Write|Enabled               |-   |
|frigate              |shm           |emptyDir|-              |/dev/shm                                |Read/Write|Enabled               |-   |
|frigate              |media         |PVC     |-              |/media                                  |Read/Write|Enabled               |-   |
|ghost                |content       |PVC     |-              |/var/lib/ghost/content                  |Read/Write|Enabled               |-   |
|homebridge           |config        |PVC     |-              |/homebridge                             |Read/Write|Enabled               |-   |
|inventree            |data          |PVC     |-              |/home/inventree/data                    |Read/Write|Enabled               |-   |
|kopia                |config        |PVC     |-              |/app/config                             |Read/Write|Enabled               |-   |
|kopia                |cache         |PVC     |-              |/app/cache                              |Read/Write|Enabled               |-   |
|kopia                |logs          |PVC     |-              |/app/logs                               |Read/Write|Enabled               |-   |
|kopia                |rclone        |PVC     |-              |/app/rclone                             |Read/Write|Enabled               |-   |
|meshcentral          |data          |PVC     |-              |/home/node/meshcentral/meshcentral-data |Read/Write|Enabled               |-   |
|meshcentral          |files         |PVC     |-              |/home/node/meshcentral/meshcentral-files|Read/Write|Enabled               |-   |
|netdata              |config        |PVC     |-              |/etc/netdata                            |Read/Write|Enabled               |-   |
|netdata              |lib           |PVC     |-              |/var/lib/netdata                        |Read/Write|Enabled               |-   |
|netdata              |cache         |PVC     |-              |/var/cache/netdata                      |Read/Write|Enabled               |-   |
|netdata              |passwd        |hostPath|/etc/passwd    |/host/etc/passwd                        |Read Only |Enabled               |-   |
|netdata              |group         |hostPath|/etc/group     |/host/etc/group                         |Read Only |Enabled               |-   |
|netdata              |proc          |hostPath|/proc          |/host/proc                              |Read Only |Enabled               |-   |
|netdata              |dev           |hostPath|/dev           |/host/dev                               |Read Only |Enabled               |-   |
|netdata              |sys           |hostPath|/sys           |/host/sys                               |Read Only |Enabled               |-   |
|netdata              |os            |hostPath|/etc/os-release|/host/etc/os-release                    |Read Only |Enabled               |-   |
|piwigo               |config        |PVC     |-              |/config                                 |Read/Write|Enabled               |-   |
|self-service-password|config        |PVC     |-              |/assets/custom                          |Read/Write|Enabled               |-   |
|self-service-password|logs          |PVC     |-              |/www/logs                               |Read/Write|Enabled               |-   |
|technitium           |config        |PVC     |-              |/etc/dns/config                         |Read/Write|Enabled               |-   |
|zabbix-server        |snmptraps     |PVC     |-              |/var/lib/zabbix/snmptraps               |Read/Write|Enabled               |-   |

## Dev

| App | Volume Name | Type | Host Path | Mount Path | Mode | Status | Note |
|:----|:-----------:|:----:|:---------:|:----------:|:----:|:------:|:----:|
|adminer                |-                        |-   |-       |-                         |Read/Write|Persistence not Defined|-   |
|android-8-0            |-                        |-   |-       |-                         |Read/Write|Persistence not Defined|-   |
|androiddebugbridge     |-                        |-   |-       |-                         |Read/Write|Persistence not Defined|-   |
|aurora-files           |-                        |-   |-       |-                         |Read/Write|Persistence not Defined|-   |
|bwapp                  |-                        |-   |-       |-                         |Read/Write|Persistence not Defined|-   |
|acestream              |acestreamcache           |PVC |-       |/srv/acestream/.ACEStream |Read/Write|Enabled                |-   |
|adguard-home           |workingdirectory         |PVC |-       |/opt/adguardhome/conf     |Read/Write|Enabled                |-   |
|adguardhome-sync       |config                   |PVC |-       |/config                   |Read/Write|Enabled                |-   |
|alienswarm             |serverfiles              |PVC |-       |/serverdata/serverfiles   |Read/Write|Enabled                |-   |
|alienswarm             |steamcmd                 |PVC |-       |/serverdata/steamcmd      |Read/Write|Enabled                |-   |
|alienswarm-reactivedrop|serverfiles              |PVC |-       |/serverdata/serverfiles   |Read/Write|Enabled                |-   |
|alienswarm-reactivedrop|steamcmd                 |PVC |-       |/serverdata/steamcmd      |Read/Write|Enabled                |-   |
|altitude               |serverfiles              |PVC |-       |/altitude                 |Read/Write|Enabled                |-   |
|ama                    |config                   |PVC |-       |/config                   |Read/Write|Enabled                |-   |
|ama                    |hostpathfordownloads-ama |PVC |-       |/downloads-ama            |Read/Write|Enabled                |-   |
|ambd                   |config                   |PVC |-       |/config                   |Read/Write|Enabled                |-   |
|ambd                   |hostpathfordownloads-ambd|PVC |-       |/downloads-ambd           |Read/Write|Enabled                |-   |
|ambd                   |hostpathforlibrary-ambd  |PVC |-       |/library-ambd             |Read/Write|Enabled                |-   |
|americasarmy-pg        |serverfiles              |PVC |-       |/serverdata/serverfiles   |Read/Write|Enabled                |-   |
|americasarmy-pg        |steamcmd                 |PVC |-       |/serverdata/steamcmd      |Read/Write|Enabled                |-   |
|amtd                   |config                   |PVC |-       |/config                   |Read/Write|Enabled                |-   |
|amule                  |storagecomplete          |PVC |-       |/incoming                 |Read/Write|Enabled                |-   |
|amule                  |storageconfig            |PVC |-       |/home/amule/.aMule        |Read/Write|Enabled                |-   |
|amule                  |storageincomplete        |PVC |-       |/temp                     |Read/Write|Enabled                |-   |
|amvd                   |config                   |PVC |-       |/config                   |Read/Write|Enabled                |-   |
|amvd                   |hostpathfordownloads-amvd|PVC |-       |/downloads-amvd           |Read/Write|Enabled                |-   |
|anope                  |datapath                 |PVC |-       |/anope                    |Read/Write|Enabled                |-   |
|apache-webdav          |config                   |PVC |-       |/var/lib/dav              |Read/Write|Enabled                |-   |
|apache-webdav          |data                     |PVC |-       |/var/lib/dav/data         |Read/Write|Enabled                |-   |
|apprise-api            |config                   |PVC |-       |/config                   |Read/Write|Enabled                |-   |
|apt-cacher-ng          |apt-cacher-ng            |PVC |-       |/var/cache/apt-cacher-ng  |Read/Write|Enabled                |-   |
|archiveteam-warrior    |appdata                  |PVC |-       |/var/run/docker.sock      |Read/Write|Enabled                |-   |
|arksurvivalevolved     |serverfiles              |PVC |-       |/serverdata/serverfiles   |Read/Write|Enabled                |-   |
|arksurvivalevolved     |steamcmd                 |PVC |-       |/serverdata/steamcmd      |Read/Write|Enabled                |-   |
|arma3                  |profiles                 |PVC |-       |/serverdata/.local/share  |Read/Write|Enabled                |-   |
|arma3                  |serverfiles              |PVC |-       |/serverdata/serverfiles   |Read/Write|Enabled                |-   |
|arma3                  |steamcmd                 |PVC |-       |/serverdata/steamcmd      |Read/Write|Enabled                |-   |
|arma3exilemod          |profiles                 |PVC |-       |/serverdata/.local/share  |Read/Write|Enabled                |-   |
|arma3exilemod          |serverfiles              |PVC |-       |/serverdata/serverfiles   |Read/Write|Enabled                |-   |
|arma3exilemod          |steamcmd                 |PVC |-       |/serverdata/steamcmd      |Read/Write|Enabled                |-   |
|artifactory-oss        |varoptjfrogartifactory   |PVC |-       |/var/opt/jfrog/artifactory|Read/Write|Enabled                |-   |
|assettocorsa           |serverfiles              |PVC |-       |/serverdata/serverfiles   |Read/Write|Enabled                |-   |
|assettocorsa           |steamcmd                 |PVC |-       |/serverdata/steamcmd      |Read/Write|Enabled                |-   |
|atd                    |config                   |PVC |-       |/config                   |Read/Write|Enabled                |-   |
|atd                    |hostpathfordownloads-atd |PVC |-       |/downloads-atd            |Read/Write|Enabled                |-   |
|auto-yt-dl             |data                     |PVC |-       |/app/data                 |Read/Write|Enabled                |-   |
|auto-yt-dl             |hostpath1                |PVC |-       |/app/Downloads            |Read/Write|Enabled                |-   |
|autoscan               |config                   |PVC |-       |/config                   |Read/Write|Enabled                |-   |
|avorion                |serverfiles              |PVC |-       |/serverdata/serverfiles   |Read/Write|Enabled                |-   |
|avorion                |steamcmd                 |PVC |-       |/serverdata/steamcmd      |Read/Write|Enabled                |-   |
|backuppc               |backuplocation           |PVC |-       |/var/lib/backuppc         |Read/Write|Enabled                |-   |
|backuppc               |configurationfiles       |PVC |-       |/etc/backuppc             |Read/Write|Enabled                |-   |
|backuppc               |homedirectory            |PVC |-       |/home/backuppc            |Read/Write|Enabled                |-   |
|backuppc               |logs                     |PVC |-       |/www/logs                 |Read/Write|Enabled                |-   |
|baikal                 |config                   |PVC |-       |/var/www/baikal/config    |Read/Write|Enabled                |-   |
|baikal                 |specific                 |PVC |-       |/var/www/baikal/Specific  |Read/Write|Enabled                |-   |
|barcodebuddy           |config                   |PVC |-       |/config                   |Read/Write|Enabled                |-   |
|barotrauma             |serverfiles              |PVC |-       |/serverdata/serverfiles   |Read/Write|Enabled                |-   |
|barotrauma             |steamcmd                 |PVC |-       |/serverdata/steamcmd      |Read/Write|Enabled                |-   |
|bitcoin-node           |blockhainstorage         |PVC |-       |/bitcoin/.bitcoin         |Read/Write|Enabled                |-   |
|bitcoind               |data                     |PVC |-       |/root/.bitcoin/           |Read/Write|Enabled                |-   |
|bitcoinunlimited       |data                     |PVC |-       |/data                     |Read/Write|Enabled                |-   |
|bitcoinwalletgui       |bitcoinblockchainpath    |PVC |-       |/headless/.bitcoin/       |Read/Write|Enabled                |-   |
|blender                |config                   |PVC |-       |/config                   |Read/Write|Enabled                |-   |
|blender-desktop-g3     |internalshare            |PVC |-       |/UNRAID_SHARE             |Read/Write|Enabled                |-   |
|blender-desktop-g3     |storageprojects          |PVC |-       |/srv/projects             |Read/Write|Enabled                |-   |
|breitbandmessung-de    |config                   |PVC |-       |/usr/src/app/config       |Read/Write|Enabled                |-   |
|breitbandmessung-de    |messurementlogs          |PVC |-       |/export/                  |Read/Write|Enabled                |-   |
|btdex                  |btdex                    |PVC |-       |/opt/btdex/cache          |Read/Write|Enabled                |-   |
|server-7daystodie      |serverfiles              |PVC |-       |/serverdata/serverfiles   |Read/Write|Enabled                |-   |
|server-7daystodie      |steamcmd                 |PVC |-       |/serverdata/steamcmd      |Read/Write|Enabled                |-   |

## Dependency

| App | Volume Name | Type | Host Path | Mount Path | Mode | Status | Note |
|:----|:-----------:|:----:|:---------:|:----------:|:----:|:------:|:----:|
|mariadb   |-           |-       |-            |-            |Read/Write|Persistence not Defined|-   |
|memcached |-           |-       |-            |-            |Read/Write|Persistence not Defined|-   |
|mongodb   |-           |-       |-            |-            |Read/Write|Persistence not Defined|-   |
|postgresql|-           |-       |-            |-            |Read/Write|Persistence not Defined|-   |
|promtail  |containers  |hostPath|/mnt         |/mnt         |Read Only |Enabled                |-   |
|promtail  |pods        |hostPath|/var/log/pods|/var/log/pods|Read Only |Enabled                |-   |
|promtail  |run         |hostPath|/run/promtai |/run/promtail|Read/Write|Enabled                |-   |
|promtail  |config      |secret  |-            |/etc/promtail|Read/Write|Enabled                |-   |
|redis     |redis-health|custom  |-            |/health      |Read/Write|Enabled                |-   |

## Games

| App | Volume Name | Type | Host Path | Mount Path | Mode | Status | Note |
|:----|:-----------:|:----:|:---------:|:----------:|:----:|:------:|:----:|
|impostor-server  |-             |-       |-       |-                        |Read/Write|Persistence not Defined|-   |
|minetest         |varrun        |emptyDir|-       |/var/run                 |Read/Write|Mount Path not Defined |-   |
|acestream        |acestreamcache|PVC     |-       |/srv/acestream/.ACEStream|Read/Write|Enabled                |-   |
|minecraft-bedrock|config        |PVC     |-       |/data                    |Read/Write|Enabled                |-   |
|minecraft-java   |data          |PVC     |-       |/data                    |Read/Write|Enabled                |-   |
|minetest         |config        |PVC     |-       |/config/.minetest        |Read/Write|Enabled                |-   |
|satisfactory     |config        |PVC     |-       |/config                  |Read/Write|Enabled                |-   |
|valheim          |config        |PVC     |-       |/config                  |Read/Write|Enabled                |-   |
|valheim          |backups       |PVC     |-       |/backups                 |Read/Write|Enabled                |-   |

Some outro here