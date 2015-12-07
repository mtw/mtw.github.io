---
layout: post
title: "Tivoli Storage Manager under Debian 7 wheezy"
date: 2013-12-18 22:41:38 +0100
comments: true
categories: 
---
I recently had to install _IBM's Tivoli Storage Manager (TSM)_ client under _Debian 7_. The task seemed straightforward: Download and install the binaries from [IBM's Website](http://service.boulder.ibm.com/storage/tivoli-storage-management/maintenance/client/) and you're done. The problem here is that IBM does not provide pre-built debian packages, they just offer rpms of the TSM client. One could of course start to fiddle around with `rpm2cpio`, but I'm not comfortable with that. I'd rather use [these pre-built binary debian packages](http://www.univie.ac.at/vsi/backup/tsm-ubuntu.tar.gz) (based on TSM client 6.4.0). 
```
mkdir -p ~/Download/TSM
cd ~/Download/TSM
wget http://www.univie.ac.at/vsi/backup/tsm-ubuntu.tar.gz
```
Those .deb packages have an awkward dependency, the i386 version of libstdc++5. If your machine is based on an x86_64 architecture, you might want to add support for i386 architectures by issuing: 
```
dpkg --add-architecture i386
```
The remaining installation procedure is straightforward:
```
sudo apt-get install libstdc++5:i386 ksh
ls -l | awk '/64/||/BA-/||/BAc/ {print $9}' | xargs -I %s sudo dpkg -i %s
```
The TSM client executable is installed in `/opt/tivoli/tsm/client/ba/bin`. You might want to copy two config files and edit them to fit your requirements.
```
cd /opt/tivoli/tsm/client/ba/bin/
cp dsm.sys.smp dsm.sys
cp dsm.opt.smp dsm.opt
```
My `dsm.sys` and `dsm.opt` look like this:
{% gist 8031289  %}

See also the German version of the [Linux TSM client documentation](https://zid.univie.ac.at/support/anleitungen/server-backup/backup/) at the University of Vienna Computer Center's website.