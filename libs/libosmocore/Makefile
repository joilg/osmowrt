#
# Copyright (C) 2010-2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=libosmocore
PKG_VERSION:=0.9.6
PKG_RELEASE:=2

PKG_SOURCE_PROTO:=git
PKG_SOURCE_URL=https://git.osmocom.org/$(PKG_NAME)
PKG_SOURCE_DATE:=2017-03-05
PKG_SOURCE_VERSION:=f74cfd35acadbebe7ccd9fc02d05920958f43ad3
#PKG_SOURCE_VERSION:=acd08feb8f75827555a9ef38b890870fed3388ea
PKG_VERSION:=$(PKG_SOURCE_VERSION)-$(PKG_VERSION)

PKG_MAINTAINER:=Johannes Ilg johilg@users.noreply.github.com
PKG_LICENSE:=GPL-2.0

PKG_FIXUP:=autoreconf
PKG_INSTALL:=1
# PKG_BUILD_PARALLEL:=0

include $(INCLUDE_DIR)/package.mk

define Package/$(PKG_NAME)
  SECTION:=libs
  CATEGORY:=Libraries
  SUBMENU:=Osmocom
  TITLE:=Common library for all Osmocom projects
  URL:=http://www.osmocom.org
  DEPENDS:=+libtalloc +libpcsclite
endef

TARGET_CFLAGS += -I$(STAGING_DIR)/usr/include
# -ffunction-sections -nostartfiles -nodefaultlibs 
TARGET_LDFLAGS += "-ltalloc"

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
	
#	$(INSTALL_DIR) $(1)/usr/include/osmocom/codec
#	$(INSTALL_DIR) $(1)/usr/include/osmocom/core
#	$(INSTALL_DIR) $(1)/usr/include/osmocom/crypt
#	$(INSTALL_DIR) $(1)/usr/include/osmocom/ctrl
#	$(INSTALL_DIR) $(1)/usr/include/osmocom/gprs
#	$(INSTALL_DIR) $(1)/usr/include/osmocom/gsm
#	$(INSTALL_DIR) $(1)/usr/include/osmocom/sim
#	$(INSTALL_DIR) $(1)/usr/include/osmocom/vty
#	$(INSTALL_DIR) $(1)/usr/include/osmocom/gsm/protocol
#	$(INSTALL_DIR) $(1)/usr/include/osmocom/gprs/protocol

	
#	$(SED) 's,-I$$$${includedir},,g' $(1)/usr/lib/pkgconfig/*.pc
#	$(SED) 's,-L$$$${libdir},-L,g' $(1)/usr/lib/pkgconfig/*.pc
#	$(SED) 's,UNKNOWN,$(VERSION),g' $(1)/usr/lib/pkgconfig/*.pc



define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/include/osmocom
	$(CP) $(PKG_INSTALL_DIR)/usr/include/osmocom/* $(1)/usr/include/osmocom/
	$(INSTALL_DIR) $(1)/usr/lib/pkgconfig
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/pkgconfig/*.pc $(1)/usr/lib/pkgconfig/
	$(SED) 's,-L$$$${libdir},-L,g' $(1)/usr/lib/pkgconfig/libosmoctrl.pc
	$(SED) 's,-L$$$${libdir},-L,g' $(1)/usr/lib/pkgconfig/libosmocore.pc
	$(SED) 's,-L$$$${libdir},-L,g' $(1)/usr/lib/pkgconfig/libosmoctrl.pc
	$(SED) 's,-L$$$${libdir},-L,g' $(1)/usr/lib/pkgconfig/libosmogb.pc
	$(SED) 's,-L$$$${libdir},-L,g' $(1)/usr/lib/pkgconfig/libosmogsm.pc
	$(SED) 's,-L$$$${libdir},-L,g' $(1)/usr/lib/pkgconfig/libosmovty.pc
	$(INSTALL_DIR) $(1)/usr/lib
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/*.la $(1)/usr/lib/
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/libosmovty.la $(1)/usr/lib/
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/libosmoctrl.la $(1)/usr/lib/
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/libosmogb.la $(1)/usr/lib/
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/libosmocore.la $(1)/usr/lib/
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/libosmogsm.la $(1)/usr/lib/
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/libosmosim.la $(1)/usr/lib/
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/libosmocodec.la $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/* $(1)/
	
endef

define Package/$(PKG_NAME)/install
	$(INSTALL_DIR) $(1)/usr/{bin,lib}
	$(INSTALL_BIN) $(PKG_INSTALL_DIR)/usr/bin/* $(1)/usr/bin/
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/*.so* $(1)/usr/lib/
endef

$(eval $(call BuildPackage,$(PKG_NAME)))