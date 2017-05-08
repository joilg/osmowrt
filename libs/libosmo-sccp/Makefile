#
# Copyright (C) 2010-2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=libosmo-sccp
PKG_RELEASE:=2
PKG_VERSION:=0.7.1

PKG_SOURCE_PROTO:=git
PKG_SOURCE_URL=https://git.osmocom.org/$(PKG_NAME)
PKG_SOURCE_VERSION:=8e708d1f2da1b187f631bf08172a5194a85b1a23
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
  SUBMENU:==Osmocom
  TITLE:=Osmocom SCCP Library
  URL:=http://www.osmocom.org
  DEPENDS:= +libosmo-netif +libosmo-abis
endef

TARGET_CFLAGS+=  -DDLM3UA=-16 -DDLSUA=-15 -DDLSCCP=-14 -DDLSS7=-13 -DOSMO_NO_EVENT=0xFFFFFFFF -ltalloc -losmonetif 
TARGET_LDFLAGS+= -ltalloc -losmonetif -L$(STAGING_DIR)/usr/lib -L.

CONFIGURE_VARS+= \
	TALLOC_CFLAGS="$(TARGET_CFLAGS) $(TARGET_CPPFLAGS) $(FPIC)" \
	TALLOC_LIBS="$(STAGING_DIR)/usr/lib" \
	LIBOSMOCORE_LIBS=$(STAGING_DIR)/usr/lib/libosmocore.so \
	LIBSCTP_LIBS=$(STAGING_DIR)/usr/lib/libsctp.so \
	LIBOSMONETIF_LIBS=$(STAGING_DIR)/usr/lib/libosmonetif.so \

MAKE_ARGS+= \
	CC="$(TARGET_CC)" \
	V=$(V)
	
CONFIGURE_ARGS += \
	--host=$(GNU_TARGET_NAME) \
	--disable-werror \
	--disable-warnings-as-errors \

define Build/InstallDev
	$(CP) $(PKG_INSTALL_DIR)/* $(1)/
#	$(INSTALL_DIR) $(1)/usr/include/osmocom/core
#	$(INSTALL_DIR) $(1)/usr/lib/pkgconfig
#	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/include/osmocom/core/* $(1)/usr/include/osmocom/core/
#	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/*.la $(1)/usr/lib/
#	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/pkgconfig/*  $(1)/usr/lib/pkgconfig/
endef

define Package/$(PKG_NAME)/install
########################################################################################
	$(INSTALL_DIR) $(1)/usr/lib
#	$(INSTALL_BIN) $(PKG_INSTALL_DIR)/usr/bin/* $(1)/usr/bin/
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/*.so* $(1)/usr/lib/
endef

$(eval $(call BuildPackage,$(PKG_NAME)))
