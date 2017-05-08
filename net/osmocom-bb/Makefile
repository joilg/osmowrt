#
# Copyright (C) 2010-2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=osmocom-bb
PKG_RELEASE:=2

PKG_SOURCE_URL=https://git.osmocom.org/osmocom-bb
PKG_SOURCE_PROTO:=git
PKG_SOURCE_DATE:=2017-03-05
PKG_SOURCE_VERSION:=0cdf4b0a6821a0e970194ed5b122d3d6270c9814

PKG_MAINTAINER:=Johannes Ilg johilg@users.noreply.github.com
PKG_LICENSE:=GPL-2.0

PKG_FIXUP:=autoreconf
PKG_INSTALL:=1
# PKG_BUILD_PARALLEL:=0

include $(INCLUDE_DIR)/package.mk

define Package/osmocom-bb
  SECTION:=net
  CATEGORY:=Network
  SUBMENU:=Osmocom
  TITLE:=OsmocomBB MS-side GSM Protocol stack (L1, L2, L3) including firmware
  URL:=http://www.osmocom.org
  DEPENDS:=+libosmocore
endef

define Build/Prepare
	$(call Build/Prepare/Default)
	# $(CP) ./src/* $(PKG_BUILD_DIR)
	mkdir -p $(PKG_BUILD_DIR)/src/include/site/
	ln -sf $(STAGING_DIR) $(PKG_BUILD_DIR)/src/include/site/linux
endef


CONFIGURE_VARS += \
	CC="$(TARGET_CROSS)gcc" \

CONFIGURE_ARGS += \
	--enable-shared \
	--enable-static \
	--enable-iu \

TARGET_CFLAGS += -I$(STAGING_DIR)/usr/include

MAKE_ARGS += \
	CC="$(TARGET_CC)" \
	CROSS_INST_PREFIX="$(PKG_BUILD_DIR)" \
	CROSS_HOST="$(TARGET_CROSS)" \
	



#TARGET_LDFLAGS += "-ltalloc"

#CONFIGURE_ARGS += \
#		--exec-prefix=/usr \
#		--prefix=/usr / \

#CONFIGURE_VARS += \
#	TALLOC_CFLAGS="$(TARGET_CFLAGS) $(TARGET_CPPFLAGS) $(FPIC)" \
#	TALLOC_LIBS="$(STAGING_DIR)/usr/lib" \
		
MAKE_PATH=src
		
define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/lib/pkgconfig
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/*.la $(1)/usr/lib/
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/pkgconfig/*  $(1)/usr/lib/pkgconfig/
endef

define Package/osmocom-bb/install
	$(INSTALL_DIR) $(1)/usr/{bin,lib}
	$(INSTALL_BIN) $(PKG_INSTALL_DIR)/usr/bin/* $(1)/usr/bin/
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/*.so* $(1)/usr/lib/
endef


$(eval $(call BuildPackage,osmocom-bb))
