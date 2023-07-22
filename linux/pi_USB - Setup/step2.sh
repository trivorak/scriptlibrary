#!/bin/bash
# Container
sudo dd bs=1M if=/dev/zero of=/piusb.bin count=4096
sudo mkdosfs /piusb.bin -F 32 -I
sudo mkdir /mnt/usb_share
echo '/piusb.bin /mnt/usb_share vfat users,umask=000 0 2' | sudo tee -a /etc/fstab
sudo mount -a
# Install Samba & setup 
sudo apt update
sudo apt install samba winbind -y
sudo bash -c "cat sambasettings.txt >> /etc/samba/smb.conf"
sudo systemctl restart smbd.service
# Watchdog
sudo pip3 install watchdog
sudo cp usb_share.py /usr/local/share/usb_share.py
sudo chmod +x /usr/local/share/usb_share.py
sudo touch /etc/systemd/system/usbshare.service
sudo bash -c "cat servicesetup.txt >> /etc/systemd/system/usbshare.service"
# Restart services
sudo systemctl daemon-reload
sudo systemctl enable usbshare.service
sudo systemctl start usbshare.service