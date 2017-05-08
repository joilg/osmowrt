#
# Copyright (C) 2010-2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=osmo-iuh
PKG_VERSION:=201703
PKG_RELEASE:=1

PKG_SOURCE_PROTO:=git
PKG_SOURCE_URL=https://git.osmocom.org/$(PKG_NAME)
#PKG_SOURCE_VERSION:=09ed4b4adc7d36c83d821a1dfa22156e76be461f
PKG_SOURCE_VERSION:=46fea15afc38fb995baf4100f4de1d6a3565899f
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
  TITLE:=Osmocom code for the Iuh interface (HNBAP, RUA, RANAP)
  URL:=http://www.osmocom.org
  DEPENDS:=+libosmocore +libosmo-sccp +libasn1c
endef


TARGET_CFLAGS += -I$(STAGING_DIR)/usr/include
TARGET_LDFLAGS += "-ltalloc"

CONFIGURE_VARS+= \
	TALLOC_CFLAGS="$(TARGET_CFLAGS) $(TARGET_CPPFLAGS) $(FPIC)" \
	TALLOC_LIBS="$(STAGING_DIR)/usr/lib" \
	OSMOCORE_LIBS=$(STAGING_DIR)/usr/lib/libosmocore.so \
	OSMOCTRL_LIBS=$(STAGING_DIR)/usr/lib/libosmoctrl.so \
	ASN1C_LIBS=$(STAGING_DIR)/usr/lib/libasn1c.so \
	OSMOGSM_LIBS=$(STAGING_DIR)/usr/lib/libosmogsm.so \
	OSMONETIF_LIBS=$(STAGING_DIR)/usr/lib/libosmonetif.so \
	OSMOSIGTRAN_LIBS=$(STAGING_DIR)/usr/lib/libosmo-sigtran.so \
	OSMOVTY_LIBS=$(STAGING_DIR)/usr/lib/libosmovty.so \


define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/include/osmocom
	$(CP) $(PKG_INSTALL_DIR)/usr/include/osmocom/* $(1)/usr/include/osmocom/

	$(INSTALL_DIR) $(1)/usr/lib
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/*.la $(1)/usr/lib/

	$(INSTALL_DIR) $(1)/usr/lib/pkgconfig
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/pkgconfig/*.pc $(1)/usr/lib/pkgconfig/
	$(SED) 's,-I$$$${includedir},,g' $(1)/usr/lib/pkgconfig/*.pc
#	$(SED) 's,-L$$$${libdir},-L,g' $(1)/usr/lib/pkgconfig/*.pc
#	$(SED) 's,UNKNOWN,$(VERSION),g' $(1)/usr/lib/pkgconfig/*.pc
endef

define Package/$(PKG_NAME)/install
	$(INSTALL_DIR) $(1)/usr/{bin,lib}
	$(INSTALL_BIN) $(PKG_INSTALL_DIR)/usr/bin/* $(1)/usr/bin/
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/*.so* $(1)/usr/lib/
endef

$(eval $(call BuildPackage,$(PKG_NAME)))