# Ubuntu 1804 - Dell G7 - Intel 9260 蓝牙驱动问题

Dell G7 7590 笔记本安装完成 ubuntu 1804 之后无法使用蓝牙模块, 并且 dmesg 会打印如下消息:  

```bash
Bluetooth: hci0: request failed to create LE connection: status 0x0c (Intel 9260)
```

这是内核中的一个 bug, bug 提交在这里: https://bugs.launchpad.net/ubuntu/+source/linux-firmware/+bug/1835449   

## 解决方案  

In order to determine the right hardware spec on your device, please attach `sudo lspci -vvnnk` output. It will contains subsystem ID that can be used to find the right iwlwifi model.  

1) 下载内核固件代码  

```bash
git clone https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git 

```

2) 替换 /lib/firmware/intel/ 目录中的内容. 例如:  

```bash
$ sudo mv /lib/firmware/intel /lib/firmware/intel.orig
$ sudo cp -a _git_cloned_firmwares_/intel /lib/firmware
```

3) 关机后等待 3 分钟之后再开机, 注意不是直接重启. 

关机三分钟是为了让蓝牙模块完全停止工作。  


4) 查看 dmesg 命令输出的信息中是否包含 Bluetooth|hci:  

```bash
$ dmesg | egrep -i 'blue|hci'
```

如果发现其中有类似下面这行输出, 则蓝牙驱动可以正常工作了:  

```bash
  Bluetooth: hci0: Found device firmware: intel/ibt-11-5.sfi
```

不要更改 /etc/bluetooth/main.conf 中的任何内容。  

## 参考资料  

https://bugs.launchpad.net/ubuntu/+source/linux-firmware/+bug/1835449

https://bugs.launchpad.net/ubuntu/+source/linux-firmware/+bug/1836467  


## 一个成功的 dmesg 示例  

```bash
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
```
