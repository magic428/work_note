# Win10 重新安装应用商店  

为了重新装回来试了很多办法，终于找到一个真正有用的：   

http://www.thewindowsclub.com/windows-store-app-missing-windows-10  

具体办法如下：

```bash
Get-AppXPackage *WindowsStore* -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}
```

