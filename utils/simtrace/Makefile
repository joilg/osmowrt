#
# Copyright (C) 2010-2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=simtrace
PKG_RELEASE:=2

PKG_SOURCE_URL=https://git.osmocom.org/$(PKG_NAME)
PKG_SOURCE_PROTO:=git
PKG_SOURCE_DATE:=2017-03-05
PKG_SOURCE_VERSION:=197ed82a32459d6ff64d9f97b0dbc36ce8b72c67

PKG_MAINTAINER:=Johannes Ilg johilg@users.noreply.github.com
PKG_LICENSE:=GPL-2.0

PKG_FIXUP:=autoreconf
PKG_INSTALL:=1
# PKG_BUILD_PARALLEL:=0

include $(INCLUDE_DIR)/package.mk

define Package/$(PKG_NAME)
  SECTION:=utils
  CATEGORY:=Utilities
  TITLE:=SIM card APDU tracing
  URL:=http://www.osmocom.org
  DEPENDS:=+libosmocore
endef

TARGET_CFLAGS += \
  -I$(STAGING_DIR)/usr/include \
  -I$(STAGING_DIR)/usr/include/osmocom/core \
  -I$(STAGING_DIR)/usr/include/libusb-1.0

#TARGET_LDFLAGS += "-ltalloc"

MAKE_PATH=host	

define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/lib/pkgconfig
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/*.la $(1)/usr/lib/
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/pkgconfig/libosmocore.pc  $(1)/usr/lib/pkgconfig/
endef

define Package/$(PKG_NAME)/install
	$(INSTALL_DIR) $(1)/usr/{bin,lib}
	$(INSTALL_BIN) $(PKG_INSTALL_DIR)/usr/bin/* $(1)/usr/bin/
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/*.so* $(1)/usr/lib/
endef


$(eval $(call BuildPackage,$(PKG_NAME)))
