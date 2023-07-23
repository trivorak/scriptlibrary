#!/bin/bash
sudo apt install git python3-pip
echo 'dtoverlay=dwc2' | sudo tee -a /boot/config.txt
echo 'dwc2' | sudo tee -a /etc/modules
sudo reboot
