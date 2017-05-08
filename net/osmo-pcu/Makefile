#
# Copyright (C) 2010-2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=osmo-pcu
PKG_VERSION:=0.2
PKG_RELEASE:=2

PKG_SOURCE_URL=https://git.osmocom.org/$(PKG_NAME)
PKG_SOURCE_PROTO:=git
PKG_SOURCE_VERSION:=333d7e634551a7341e9a953d38d5ebbafc091787
#1275a3f91a744e011b0dba82b09124d249c7abb5

PKG_MAINTAINER:=Johannes Ilg johilg@users.noreply.github.com
PKG_LICENSE:=GPL-2.0

PKG_FIXUP:=autoreconf
PKG_INSTALL:=1
# PKG_BUILD_PARALLEL:=0

include $(INCLUDE_DIR)/package.mk

define Package/$(PKG_NAME)
  SECTION:=net
  CATEGORY:=Network
  SUBMENU:=Osmocom
  TITLE:=Osmocom PCU code (RLC/MAC/PCU) for OsmoBTS
  URL:=http://www.osmocom.org
  DEPENDS:=+libosmocore
endef


TARGET_CFLAGS += -I. -I$(STAGING_DIR)/usr/include -L. 
TARGET_LDFLAGS += -ltalloc 

CONFIGURE_VARS += \
	CC="$(TARGET_CROSS)gcc" \
	LIBOSMOCORE_LIBS="-L$(STAGING_DIR)/usr/lib -losmocore" \
	LIBOSMOGB_LIBS="-L$(STAGING_DIR)/usr/lib -losmogb" \
	LIBOSMOGSM_LIBS="-L$(STAGING_DIR)/usr/lib -losmogsm" \
	LIBOSMOVTY_LIBS="-L$(STAGING_DIR)/usr/lib -losmovty" \
	LIBOSMOCTRL_LIBS="-L$(STAGING_DIR)/usr/lib -losmoctrl" \
	LIBOSMOGB_LIBS="-L$(STAGING_DIR)/usr/lib -losmogb" \
	
#CONFIGURE_ARGS += \
#	--host=$(GNU_TARGET_NAME) \
	
MAKE_ARGS += \
	CC="$(TARGET_CC)" \
	CROSS_INST_PREFIX="$(PKG_BUILD_DIR)" \
	CROSS_HOST="$(TARGET_CROSS)" \

		
define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/include/{def_list,def_frame}
	$(CP) $(PKG_INSTALL_DIR)/usr/include/* $(1)/usr/include/
	$(INSTALL_DIR) $(1)/usr/lib/pkgconfig
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/*.la $(1)/usr/lib/
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/pkgconfig/*  $(1)/usr/lib/pkgconfig/
endef

define Package/$(PKG_NAME)/install
	$(INSTALL_DIR) $(1)/usr/bin
	$(INSTALL_BIN) $(PKG_INSTALL_DIR)/usr/bin/* $(1)/usr/bin/
endef

$(eval $(call BuildPackage,$(PKG_NAME)))
