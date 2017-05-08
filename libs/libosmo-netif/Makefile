#
# Copyright (C) 2010-2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=libosmo-netif
PKG_VERSION:=0.1.5

PKG_SOURCE_PROTO:=git
PKG_SOURCE_URL=https://git.osmocom.org/$(PKG_NAME)
PKG_SOURCE_DATE:=2017-03-07
# sysmocom/sctp
PKG_SOURCE_VERSION:=ff41201a61713587119e44e45b9dd4e0001d54ea
# Master
#PKG_SOURCE_VERSION:=5fd93e02f818aecfc73db66e8064858442122959
PKG_VERSION:=$(PKG_SOURCE_VERSION)-$(PKG_VERSION)

PKG_MAINTAINER:=Johannes Ilg johilg@users.noreply.github.com
PKG_LICENSE:=GPL-2.0

PKG_FIXUP:=autoreconf
PKG_INSTALL:=1

PKG_CONFIG_DEPENDS := \
	CONFIG_PACKAGE_libosmocore \
	CONFIG_PACKAGE_libsctp \

include $(INCLUDE_DIR)/package.mk

define Package/$(PKG_NAME)
  SECTION:=libs
  CATEGORY:=Libraries
  SUBMENU:=Osmocom
  TITLE:=Osmocom library for muxed audio
  URL:=http://www.osmocom.org
  DEPENDS:=+libosmocore +libosmo-abis +libsctp
endef


TARGET_CFLAGS += -I$(STAGING_DIR)/usr/include
CONFIGURE_VARS += \
	CC="$(TARGET_CROSS)gcc" \

CONFIGURE_ARGS += \
	--host=$(GNU_TARGET_NAME) \
	
MAKE_ARGS += \
	CC="$(TARGET_CC)" \


define Build/Compile
	$(call Build/Compile/Default, \
			DESTDIR="$(PKG_INSTALL_DIR)" \
			CC="$(TARGET_CC)" \
			all \
	)
endef	
		
define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/include/osmocom/netif/channel
	$(CP) $(PKG_INSTALL_DIR)/usr/include/* $(1)/usr/include/
#	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/include/osmocom/netif/* $(1)/usr/include/osmocom/netif/
	$(INSTALL_DIR) $(1)/usr/lib
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/*.{a,la} $(1)/usr/lib/
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/*.so* $(1)/usr/lib/
	$(INSTALL_DIR) $(1)/usr/lib/pkgconfig
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/pkgconfig/*  $(1)/usr/lib/pkgconfig/
endef

define Package/$(PKG_NAME)/install
	$(INSTALL_DIR) $(1)/usr/lib
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/*.so* $(1)/usr/lib/
endef

$(eval $(call BuildPackage,$(PKG_NAME)))