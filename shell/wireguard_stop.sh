#!/bin/bash
# Script to get current wire guard interface and stop it



interface=$(wg | grep "interface:")
interface_no_whitespace="$(echo -e "${interface#*:}" | tr -d '[:space:]')"
echo "${interface_no_whitespace}"

wg-quick down ${interface_no_whitespace}
exit 0
