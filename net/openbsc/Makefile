#
# Copyright (C) 2010-2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=openbsc
PKG_VERSION:=0.15
PKG_RELEASE:=3

PKG_SOURCE_PROTO:=git
PKG_SOURCE_URL:=https://git.osmocom.org/$(PKG_NAME)
PKG_SOURCE_VERSION:=6d8e5198ad17e70f27010dbf7c86d25477de90e1
PKG_VERSION:=$(PKG_SOURCE_VERSION)-$(PKG_VERSION)

PKG_MAINTAINER:=Johannes Ilg johilg@users.noreply.github.com
PKG_LICENSE:=GPL-2.0

PKG_FIXUP:=autoreconf
PKG_INSTALL:=1
PKG_CONFIG_DEPENDS := \
	CONFIG_PACKAGE_libosmo-netif \

include $(INCLUDE_DIR)/package.mk

define Package/$(PKG_NAME)
  SECTION:=net
  CATEGORY:=Network
  SUBMENU:=Osmocom
  TITLE:=Osmocom OpenBSC, OsmoSGSN, OsmoBSC and other programs
  URL:=http://www.osmocom.org
  DEPENDS:=+libosmocore +libosmo-netif +libopenssl +libosmo-abis +libosmo-sccp \
	+libsmpp34 +asn1c +libasn1c +osmo-iuh +libdbi +libpcap 
endef

CONFIGURE_PATH = openbsc
MAKE_PATH = openbsc

TARGET_CFLAGS += -I$(STAGING_DIR)/usr/include
TARGET_LDFLAGS += -ltalloc

CONFIGURE_VARS += \
	CC="$(TARGET_CROSS)gcc" \
	LIBOSMOCORE_LIBS="-L$(STAGING_DIR)/usr/lib -losmocore" \
	LIBOSMOGB_LIBS="-L$(STAGING_DIR)/usr/lib -losmogb" \
	LIBOSMOGSM_LIBS="-L$(STAGING_DIR)/usr/lib -losmogsm" \
	LIBOSMOVTY_LIBS="-L$(STAGING_DIR)/usr/lib -losmovty" \
	LIBOSMOCTRL_LIBS="-L$(STAGING_DIR)/usr/lib -losmoctrl" \

define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/include 
	$(CP) $(PKG_INSTALL_DIR)/usr/include/* $(1)/usr/include/
	$(INSTALL_DIR) $(1)/usr/lib/pkgconfig
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/pkgconfig/*  $(1)/usr/lib/pkgconfig/
endef

define Package/$(PKG_NAME)/install
	$(INSTALL_DIR) $(1)/usr/bin
	$(INSTALL_BIN) $(PKG_INSTALL_DIR)/usr/bin/* $(1)/usr/bin/
	$(INSTALL_DIR) $(1)/usr/share
	$(CP) $(PKG_INSTALL_DIR)/usr/share/doc/openbsc/examples $(1)/usr/share/
endef

$(eval $(call BuildPackage,$(PKG_NAME)))
