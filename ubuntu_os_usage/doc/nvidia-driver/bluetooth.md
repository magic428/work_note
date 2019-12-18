Hi, @wjbarid,

In order to determine the right hardware spec on your device, please attach `sudo lspci -vvnnk` output. It will contains subsystem ID that can be used to find the right iwlwifi model.

For bluetooth firmware blob name, you should try:

1. clone https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git and replace the intel/ subdirectory. Something like:

  $ sudo mv /lib/firmware/intel /lib/firmware/intel.orig
  $ sudo cp -a _git_cloned_firmwares_/intel /lib/firmware

2. power off your machine completely and turn it on again *after* 3 minutes or so.

3. capture the dmesg output for Bluetooth|hci:

  $ dmesg | egrep -i 'blue|hci'

You should find something like:

  Bluetooth: hci0: Found device firmware: intel/ibt-11-5.sfi


三分钟是为了让蓝牙模块完全停止工作。  

不要更改 /etc/bluetooth/main.conf 中的任何内容。  


Hi @vincentbou, I'll need you to run `apport-collect 1835449` in the first boot after completely power off again. I need to know which firmware blob, probably in the name "intel/ibt-*", to be updated.

See also http://manpages.ubuntu.com/manpages/bionic/man1/apport-bug.1.html for log collecting with appor

it worked！！！

## 参考资料  

https://bugs.launchpad.net/ubuntu/+source/linux-firmware/+bug/1835449

https://bugs.launchpad.net/ubuntu/+source/linux-firmware/+bug/1836467  


BCD 编辑 

http://tieba.baidu.com/p/5003454493?pid=104792401528&cid=0&referer=www.cnblogs.com&pn=0&&red_tag=s0145650392

使用老毛桃的UEFI GPT 引导, 设置系统磁盘和引导所在磁盘.  


[    1.143254] usb usb2: Manufacturer: Linux 5.1.16-050116-generic xhci-hcd
[    1.479384] usb 1-1: new high-speed USB device number 2 using xhci_hcd
[    1.975522] usb 1-2: new full-speed USB device number 3 using xhci_hcd
[    2.259448] usb 1-5: new high-speed USB device number 4 using xhci_hcd
[    2.595639] usb 1-10: new full-speed USB device number 5 using xhci_hcd
[   11.152012] Bluetooth: Core ver 2.22
[   11.152026] Bluetooth: HCI device and connection manager initialized
[   11.152028] Bluetooth: HCI socket layer initialized
[   11.152030] Bluetooth: L2CAP socket layer initialized
[   11.152033] Bluetooth: SCO socket layer initialized
[   11.178282] Bluetooth: hci0: Bootloader revision 0.1 build 42 week 52 2015
[   11.179291] Bluetooth: hci0: Device revision is 2
[   11.179292] Bluetooth: hci0: Secure boot is enabled
[   11.179293] Bluetooth: hci0: OTP lock is enabled
[   11.179294] Bluetooth: hci0: API lock is enabled
[   11.179295] Bluetooth: hci0: Debug lock is disabled
[   11.179296] Bluetooth: hci0: Minimum firmware build 1 week 10 2014
[   11.182302] Bluetooth: hci0: Found device firmware: intel/ibt-17-16-1.sfi
[   12.268816] Bluetooth: BNEP (Ethernet Emulation) ver 1.3
[   12.268818] Bluetooth: BNEP filters: protocol multicast
[   12.268822] Bluetooth: BNEP socket layer initialized
[   12.660936] Bluetooth: hci0: Waiting for firmware download to complete
[   12.661268] Bluetooth: hci0: Firmware loaded in 1453259 usecs
[   12.661299] Bluetooth: hci0: Waiting for device to boot
[   12.674273] Bluetooth: hci0: Device booted in 12681 usecs
[   12.674554] Bluetooth: hci0: Found Intel DDC parameters: intel/ibt-17-16-1.ddc
[   12.677274] Bluetooth: hci0: Applying Intel DDC parameters completed
[   18.197154] Bluetooth: HIDP (Human Interface Emulation) ver 1.2
[   18.197163] Bluetooth: HIDP socket layer initialized
[   18.198166] input: Logitech K810 Keyboard as /devices/pci0000:00/0000:00:14.0/usb1/1-10/1-10:1.0/bluetooth/hci0/hci0:256/0005:046D:B319.0004/input/input27
[   18.198465] input: Logitech K810 Consumer Control as /devices/pci0000:00/0000:00:14.0/usb1/1-10/1-10:1.0/bluetooth/hci0/hci0:256/0005:046D:B319.0004/input/input28
[   18.198562] input: Logitech K810 System Control as /devices/pci0000:00/0000:00:14.0/usb1/1-10/1-10:1.0/bluetooth/hci0/hci0:256/0005:046D:B319.0004/input/input29
[   18.198644] hid-generic 0005:046D:B319.0004: input,hidraw3: BLUETOOTH HID v12.02 Keyboard [Logitech K810] on 00:bb:60:09:27:1a
[   22.803566] usb 1-1: reset high-speed USB device number 2 using xhci_hcd
[   25.819305] Bluetooth: RFCOMM TTY layer initialized
[   25.819311] Bluetooth: RFCOMM socket layer initialized
[   25.819318] Bluetooth: RFCOMM ver 1.11