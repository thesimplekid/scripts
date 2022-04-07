#!/bin/bash
# Script to select random wireguard config from /etc/wireguard/
# Enables wireguard tunnel by calling wg-quick up on random file

conf_file=$(ls /etc/wireguard/ | shuf -n1)

# echo "${conf_file%.*}"
wg-quick up ${conf_file%.*}
exit 0
