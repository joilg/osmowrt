#
# Copyright (C) 2010-2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=libasn1c
PKG_VERSION:=16.09
PKG_RELEASE:=2

PKG_SOURCE_URL=https://git.osmocom.org/$(PKG_NAME)
PKG_SOURCE_PROTO:=git
PKG_SOURCE_DATE:=2017-03-05
PKG_SOURCE_VERSION:=20d668cbd3c14ef32fcbd09617fbd3c8e6856ec0

PKG_MAINTAINER:=Johannes Ilg johilg@users.noreply.github.com
PKG_LICENSE:=GPL-2.0

PKG_FIXUP:=autoreconf
PKG_INSTALL:=1
# PKG_BUILD_PARALLEL:=0

include $(INCLUDE_DIR)/package.mk

define Package/$(PKG_NAME)
  SECTION:=libs
  CATEGORY:=Libraries
  TITLE:=asn1c runtime code as shared library
  URL:=http://www.osmocom.org
  DEPENDS:=+libtalloc
endef


#TARGET_CFLAGS += -I$(STAGING_DIR)/usr/include
# -ffunction-sections -nostartfiles -nodefaultlibs 
#TARGET_LDFLAGS += "-ltalloc"

#CONFIGURE_VARS += \
#	CC="$(TARGET_CROSS)gcc" \
#	TALLOC_CFLAGS="$(TARGET_CFLAGS) $(TARGET_CPPFLAGS) $(FPIC)" \
#	TALLOC_LIBS="$(STAGING_DIR)/usr/lib" \

#CONFIGURE_ARGS += \
#	--host=$(GNU_TARGET_NAME) \
	
#MAKE_ARGS += \
#	CC="$(TARGET_CC)" \
#	CROSS_INST_PREFIX="$(PKG_BUILD_DIR)" \
#	CROSS_HOST="$(TARGET_CROSS)" \

#define Build/Compile
#	$(call Build/Compile/Default, \
#			DESTDIR="$(PKG_INSTALL_DIR)" \
#			CC="$(TARGET_CC)" \
#			all \
#	)
#endef	
	
define Build/InstallDev
	$(CP) $(PKG_INSTALL_DIR)/* $(1)/
#	$(INSTALL_DIR) $(1)/usr/include/asn1c
#	$(CP) $(PKG_INSTALL_DIR)/usr/include/asn1c/* $(1)/usr/include/asn1c/
#	$(INSTALL_DIR) $(1)/usr/lib/pkgconfig
#	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/pkgconfig/*.pc $(1)/usr/lib/pkgconfig/
#	$(INSTALL_DIR) $(1)/usr/lib
#	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/*.la $(1)/usr/lib/
endef

define Package/$(PKG_NAME)/install
	$(INSTALL_DIR) $(1)/usr/lib
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/*.so* $(1)/usr/lib/
endef

$(eval $(call BuildPackage,$(PKG_NAME)))