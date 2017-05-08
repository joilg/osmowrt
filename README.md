# osmowrt
Port of Osmocom  Packages for OpenWRT/LEDE


## How to build

To build these packages, add the following line to the feeds.conf
in the OpenWrt/LEDE buildroot:

```
$ echo 'src-git osmocomwrt https://github.com/joilg/osmowrt.git' >> feeds.conf
```

To install all its package definitions, run:

```
./scripts/feeds update osmowrt
./scripts/feeds install -a -p osmowrt
```

The osmowrt packages should now appear in menuconfig.


## How to install openbsc into your openwrt router

```
$ opkg update
$ opkg install openbsc
```


## How to config openbsc





## How to run openbsc on your openwrt router