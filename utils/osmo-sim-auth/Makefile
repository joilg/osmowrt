#
# Copyright (C) 2010-2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=osmo-sim-auth
PKG_VERSION:=17.3
PKG_SOURCE_URL=https://git.osmocom.org/$(PKG_NAME)
PKG_SOURCE_PROTO:=git
PKG_SOURCE_VERSION:=63752ce8eee7c765d90e4b0ef6686ada245dc74b    # master

PKG_MAINTAINER:=Johannes Ilg johilg@users.noreply.github.com
PKG_LICENSE:=GPL-2.0

PKG_BUILD_DEPENDS:=python python-setuptools

include $(INCLUDE_DIR)/package.mk
$(call include_mk, python-package.mk)

define Package/$(PKG_NAME)
  SECTION:=utils
  CATEGORY:=Utilities
  SUBMENU:=osmocom
  TITLE:=A command line tool for (U)SIM authentication
  URL:=http://osmocom.org/projects/osmo-sim-auth/wiki
  DEPENDS:= +python 
endef

define Build/Compile
endef

define Package/$(PKG_NAME)/install
	$(INSTALL_DIR) $(1)/usr/lib/python$(PYTHON_VERSION)/$(PKG_NAME)
	$(CP) ./* $(1)/usr/lib/python$(PYTHON_VERSION)/$(PKG_NAME)
#	$(INSTALL_DIR) $(1)/usr/bin
#	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/bin/* $(1)/usr/bin/
endef

$(eval $(call BuildPackage,$(PKG_NAME)))
