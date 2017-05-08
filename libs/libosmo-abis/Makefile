#
# Copyright (C) 2010-2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=libosmo-abis
PKG_VERSION:=0.3.3
PKG_RELEASE:=2

PKG_SOURCE_PROTO:=git
PKG_SOURCE_URL=https://git.osmocom.org/$(PKG_NAME)
PKG_SOURCE_DATE:=2017-03-05
PKG_SOURCE_VERSION:=beb10ef02a10d73537a97f6f21aad36664c9b266
PKG_VERSION:=$(PKG_SOURCE_VERSION)-$(PKG_VERSION)

PKG_MAINTAINER:=Johannes Ilg johilg@users.noreply.github.com
PKG_LICENSE:=GPL-2.0

PKG_FIXUP:=autoreconf
PKG_INSTALL:=1
# PKG_BUILD_PARALLEL:=0
PKG_BUILD_DEPENDS:=libosmocore

include $(INCLUDE_DIR)/package.mk

define Package/$(PKG_NAME)
  SECTION:=libs
  CATEGORY:=Libraries
  TITLE:=Osmocom library for A-bis interface
  URL:=http://www.osmocom.org
  DEPENDS:=+osmoggsm +libosmocore +libortp 
endef

TARGET_CFLAGS += -I$(STAGING_DIR)/usr/include 
TARGET_LDFLAGS += "-L$(STAGING_DIR)/usr/lib"

CONFIGURE_VARS += \
	CC="$(TARGET_CROSS)gcc" \

CONFIGURE_ARGS += \
	--host=$(GNU_TARGET_NAME) \

define Build/Compile
	$(call Build/Compile/Default, \
			DESTDIR="$(PKG_INSTALL_DIR)" \
			CC="$(TARGET_CC)" \
			all \
	)
endef	
	
define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/include/osmocom/{abis,trau}
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/include/osmocom/abis/* $(1)/usr/include/osmocom/abis/
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/include/osmocom/trau/* $(1)/usr/include/osmocom/trau/
	$(INSTALL_DIR) $(1)/usr/lib/pkgconfig
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/*.so* $(1)/usr/lib/
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/pkgconfig/* $(1)/usr/lib/pkgconfig/
endef

define Package/$(PKG_NAME)/install
	$(INSTALL_DIR) $(1)/usr/lib
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/*.so* $(1)/usr/lib/
endef

$(eval $(call BuildPackage,$(PKG_NAME)))