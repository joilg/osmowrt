#
# Copyright (C) 2010-2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=libsua
PKG_RELEASE:=2

PKG_SOURCE_URL=https://git.osmocom.org/$(PKG_NAME)
PKG_SOURCE_PROTO:=git
PKG_SOURCE_DATE:=2017-03-07
PKG_SOURCE_VERSION:=283f8ffe840b3eba9d55e6bf5affdf6fd9d998e1

PKG_MAINTAINER:=Johannes Ilg johilg@users.noreply.github.com
PKG_LICENSE:=GPL-2.0

PKG_FIXUP:=autoreconf
PKG_INSTALL:=1
# PKG_BUILD_PARALLEL:=0

PKG_CONFIG_DEPENDS := \
	CONFIG_PACKAGE_libosmocore \


include $(INCLUDE_DIR)/package.mk

define Package/$(PKG_NAME)
  SECTION:=libs
  CATEGORY:=Libraries
  TITLE:=Osmocom Import of the sctp.be sualibrary for SCCP User Adatption (SUA)
  URL:=http://www.osmocom.org
  DEPENDS:=+libosmocore +libosmo-abis 
endef


TARGET_CFLAGS += -I$(STAGING_DIR)/usr/include
CONFIGURE_VARS += \
	CC="$(TARGET_CROSS)gcc" \
	TALLOC_CFLAGS="$(TARGET_CFLAGS) $(TARGET_CPPFLAGS) $(FPIC)" \
	TALLOC_LIBS="$(STAGING_DIR)/usr/lib" \

CONFIGURE_ARGS += \
	--host=$(GNU_TARGET_NAME) \
	
MAKE_ARGS += \
	CC="$(TARGET_CC)" \
	CROSS_INST_PREFIX="$(PKG_BUILD_DIR)" \
	CROSS_HOST="$(TARGET_CROSS)" \

define Build/Compile
	$(call Build/Compile/Default, \
			DESTDIR="$(PKG_INSTALL_DIR)" \
			CC="$(TARGET_CC)" \
			all \
	)
endef	
		
define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/include/osmocom/core
	$(INSTALL_DIR) $(1)/usr/lib/pkgconfig
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/include/osmocom/core/* $(1)/usr/include/osmocom/core/
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/*.la $(1)/usr/lib/
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/pkgconfig/*  $(1)/usr/lib/pkgconfig/
endef

define Package/$(PKG_NAME)/install
	$(INSTALL_DIR) $(1)/usr/{bin,lib}
	$(INSTALL_BIN) $(PKG_INSTALL_DIR)/usr/bin/* $(1)/usr/bin/
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/*.so* $(1)/usr/lib/
endef

$(eval $(call BuildPackage,$(PKG_NAME)))