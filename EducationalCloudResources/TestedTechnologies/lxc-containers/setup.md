# Installation and configuration of lxc/lcd on Ubuntu host
 ``sudo apt-get install lxc``
## Install and configure lxd 
``sudo apt install lxd`` 
configure networking and bridge management in lxd
``sudo dpkg-reconfigure -p medium lxd``
bridge created for lxd
``lxdbr0``
default subnet used by lxd containers
``10.124.71.1``
first dhcp address
``10.124.71.2``
last dhcp address
``10.124.71.254``
install ZFs: storage backend.
This includes per-container disk quotas, immediate snapshot/restore, optimized migration (send/receive) and instant container creation from an image.
``sudo apt install zfsutils-linux``
To configure LXD to use it, simply run:
``sudo lxd init``
### Create and launch GUI applications in an lxc container
+ [Stephen Grabber's website](https://stgraber.org/2014/02/09/lxc-1-0-gui-in-containers/)
### Known Issues and limitations
+ Pulseaudio not working in host machine when lxc service is running.
[https://unix.stackexchange.com/questions/416121/pulseaudio-got-problems-with-lxc-gui-container](https://unix.stackexchange.com/questions/416121/pulseaudio-got-problems-with-lxc-gui-container)
[https://unix.stackexchange.com/questions/416121/pulseaudio-got-problems-with-lxc-gui-container?rq=1](https://unix.stackexchange.com/questions/416121/pulseaudio-got-problems-with-lxc-gui-container?rq=1)
[https://github.com/lxc/lxc/issues/599](https://github.com/lxc/lxc/issues/599)
+ supports only OS **containers**(large image size problems) not application containers like docker. 
+ [volume storage options](https://github.com/lxc/lxd/issues/3389)
+ Isssues related to application portability.




