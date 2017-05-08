#
# Copyright (C) 2010-2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=osmo-hlr
PKG_VERSION:=0.0.2
PKG_RELEASE:=2

PKG_SOURCE_URL=https://git.osmocom.org/$(PKG_NAME)
PKG_SOURCE_PROTO:=git
# PKG_SOURCE_DATE:=2017-03-05
PKG_SOURCE_VERSION:=7f39468c75605077f8811557c9da6791fcbdbfe5
PKG_MAINTAINER:=Johannes Ilg johilg@users.noreply.github.com
PKG_LICENSE:=GPL-2.0

PKG_FIXUP:=autoreconf patch-libtool
# PKG_INSTALL:=1
# PKG_BUILD_PARALLEL:=0

include $(INCLUDE_DIR)/package.mk

define Package/$(PKG_NAME)
  SECTION:=net
  CATEGORY:=Network
  SUBMENU:=Osmocom
  TITLE:=Osmocom HLR for GSUP protocol towards OsmoSGSN and OsmoCSCN
  URL:=http://www.osmocom.org
  DEPENDS:=+libtalloc +libosmocore +libosmogsm +sqlite3 
endef


#TARGET_CFLAGS += -I$(STAGING_DIR)/usr/include
#TARGET_LDFLAGS = 
#LDFLAGS=
#CONFIGURE_ARGS += \
#		--exec-prefix=/xusr \
#		--prefix=/xusr  \

#MAKE_ARGS += \
#	CC="$(TARGET_CC)" \
#	CROSS_HOST="$(TARGET_CROSS)" \

#define Build/Compile
#	#echo > **********************************
#	#echo MAKE_ARGS $(MAKE_ARGS)
#	#echo MAKE_VARS $(MAKE_VARS)
#	#echo T $(LIBTOOL) 
#	#echo TF $(LIBTOOLFLAGS)
#	#echo LF $(LDFLAGS)
#	#echo CF $(CFLAGS) 
#	#echo CCLD $(CCLD) 
#	#echo CC $(TARGET_CC)
#	#echo $(AM_LDFLAGS)) 
#	#echo $(AM_V_lt) 
#	#echo $(AM_LIBTOOLFLAGS)) 
#	#echo < **********************************
#	$(call Build/Compile/Default, \
#			DESTDIR="$(PKG_INSTALL_DIR)" \
#			CC="$(TARGET_CC)" \
#			V=1 \
#	)
#e#ndef	


define Package/$(PKG_NAME)/install
	$(INSTALL_DIR) $(1)/usr/bin
	$(INSTALL_BIN) $(PKG_INSTALL_DIR)/usr/bin/* $(1)/usr/bin/
endef

$(eval $(call BuildPackage,$(PKG_NAME)))