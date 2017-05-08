#
# Copyright (C) 2010-2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=openggsn
PKG_RELEASE:=2
PKG_SOURCE_VERSION:=0.93

PKG_SOURCE_PROTO:=git
PKG_SOURCE_URL=https://git.osmocom.org/$(PKG_NAME)
PKG_SOURCE_VERSION:=19e19e3609508d121ba46c165e5ed1502a3cf9da
#a81055db1dc2046f57f1c78f055f693b5a4e3308
#PKG_SOURCE_VERSION:=a8f71eb24e03488dd92810e386567b46893fe17a
PKG_VERSION:=$(PKG_SOURCE_VERSION)-$(PKG_VERSION)

PKG_MAINTAINER:=Johannes Ilg johilg@users.noreply.github.com
PKG_LICENSE:=GPL-2.0

PKG_FIXUP:=autoreconf
PKG_INSTALL:=1

include $(INCLUDE_DIR)/package.mk

define Package/$(PKG_NAME)
  SECTION:=net
  CATEGORY:=Network
  SUBMENU:=Osmocom
  TITLE:=OpenGGSN repository
  URL:=http://www.osmocom.org
  DEPENDS:=+libosmocore +libtalloc +libpcsclite +libmnl +libosmo-netif +libgtp
endef

TARGET_LDFLAGS+= -ltalloc -losmonetif -L$(STAGING_DIR)/usr/lib -L.

CONFIGURE_VARS+= \
	LIBOSMOCORE_LIBS=$(STAGING_DIR)/usr/lib/libosmocore.so \
	LIBOSMOCTRL_LIBS=$(STAGING_DIR)/usr/lib/libosmoctrl.so \
	LIBOSMOVTY_LIBS=$(STAGING_DIR)/usr/lib/libosmovty.so \

	
define Build/InstallDev
	$(CP) $(PKG_INSTALL_DIR)/* $(1)/
#	$(INSTALL_DIR) $(1)/usr/include/{def_list,def_frame}
#	$(CP) $(PKG_INSTALL_DIR)/usr/include/* $(1)/usr/include/
#	$(INSTALL_DIR) $(1)/usr/lib/pkgconfig
#	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/*.la $(1)/usr/lib/
#	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/pkgconfig/*  $(1)/usr/lib/pkgconfig/
endef

define Package/$(PKG_NAME)/install
	$(INSTALL_DIR) $(1)/usr/bin
	$(INSTALL_BIN) $(PKG_INSTALL_DIR)/usr/bin/* $(1)/usr/bin/
	$(INSTALL_DIR) $(1)/usr/lib
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/*.so* $(1)/usr/lib/
endef

$(eval $(call BuildPackage,$(PKG_NAME)))
