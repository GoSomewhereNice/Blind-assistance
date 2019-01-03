#!/bin/bash
sudo hciconfig hci0 noscan
sudo hciconfig hci0 leadv
sudo hcitool -i hci0 cmd 0x08 0x0008 1E 02 01 1A 1A FF 4C 00 02 15 8E 4B B3 30 D6 9F 11 E8 B5 68 08 00 20 0C 9A 66 00 00 00 00 C5 00
