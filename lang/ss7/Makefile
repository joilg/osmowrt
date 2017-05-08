#
# Copyright (C) 2010-2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=ss7
PKG_RELEASE:=2

PKG_SOURCE_URL=https://git.osmocom.org/asn1/$(PKG_NAME)
PKG_SOURCE_PROTO:=git
PKG_SOURCE_DATE:=2017-03-05
PKG_SOURCE_VERSION:=f1facaa8af5726a5986c157c51fa8283b1eb611b

PKG_MAINTAINER:=Johannes Ilg johilg@users.noreply.github.com
PKG_LICENSE:=GPL-2.0

PKG_FIXUP:=autoreconf
PKG_INSTALL:=1
# PKG_BUILD_PARALLEL:=0

include $(INCLUDE_DIR)/package.mk

define Package/$(PKG_NAME)
  SECTION:=libs
  CATEGORY:=Libraries
  TITLE:=ITU/ETSI/3GPP ASN1 files for TCAP, ROS, MAP and CAP
  URL:=http://www.osmocom.org
  DEPENDS:=+libosmocore
endef


TARGET_CFLAGS += -I$(STAGING_DIR)/usr/include
TARGET_LDFLAGS += "-ltalloc"

CONFIGURE_ARGS += \
		--exec-prefix=/usr \
		--prefix=/usr / \

CONFIGURE_VARS += \
	TALLOC_CFLAGS="$(TARGET_CFLAGS) $(TARGET_CPPFLAGS) $(FPIC)" \
	TALLOC_LIBS="$(STAGING_DIR)/usr/lib" \
		
define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/include/{def_list,def_frame}
	$(CP) $(PKG_INSTALL_DIR)/usr/include/* $(1)/usr/include/
	$(INSTALL_DIR) $(1)/usr/lib/pkgconfig
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/*.la $(1)/usr/lib/
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/pkgconfig/*  $(1)/usr/lib/pkgconfig/
endef

define Package/$(PKG_NAME)/install
	$(INSTALL_DIR) $(1)/usr/lib
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/*.so* $(1)/usr/lib/
endef

$(eval $(call BuildPackage,$(PKG_NAME)))
