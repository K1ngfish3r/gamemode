#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v10
# autospec commit: 6fa3d52
#
Name     : gamemode
Version  : 1.8.1
Release  : 1
URL      : https://github.com/FeralInteractive/gamemode/archive/refs/tags/1.8.1.tar.gz
Source0  : https://github.com/FeralInteractive/gamemode/archive/refs/tags/1.8.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: gamemode-bin = %{version}-%{release}
Requires: gamemode-config = %{version}-%{release}
Requires: gamemode-data = %{version}-%{release}
Requires: gamemode-lib = %{version}-%{release}
Requires: gamemode-libexec = %{version}-%{release}
Requires: gamemode-man = %{version}-%{release}
Requires: gamemode-services = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : dbus-dev
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(inih)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(systemd)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# GameMode
**GameMode** is a daemon/lib combo for Linux that allows games to request a set of optimisations be temporarily applied to the host OS and/or a game process.

%package bin
Summary: bin components for the gamemode package.
Group: Binaries
Requires: gamemode-data = %{version}-%{release}
Requires: gamemode-libexec = %{version}-%{release}
Requires: gamemode-config = %{version}-%{release}
Requires: gamemode-services = %{version}-%{release}

%description bin
bin components for the gamemode package.


%package config
Summary: config components for the gamemode package.
Group: Default

%description config
config components for the gamemode package.


%package data
Summary: data components for the gamemode package.
Group: Data

%description data
data components for the gamemode package.


%package dev
Summary: dev components for the gamemode package.
Group: Development
Requires: gamemode-lib = %{version}-%{release}
Requires: gamemode-bin = %{version}-%{release}
Requires: gamemode-data = %{version}-%{release}
Provides: gamemode-devel = %{version}-%{release}
Requires: gamemode = %{version}-%{release}

%description dev
dev components for the gamemode package.


%package lib
Summary: lib components for the gamemode package.
Group: Libraries
Requires: gamemode-data = %{version}-%{release}
Requires: gamemode-libexec = %{version}-%{release}

%description lib
lib components for the gamemode package.


%package libexec
Summary: libexec components for the gamemode package.
Group: Default
Requires: gamemode-config = %{version}-%{release}

%description libexec
libexec components for the gamemode package.


%package man
Summary: man components for the gamemode package.
Group: Default

%description man
man components for the gamemode package.


%package services
Summary: services components for the gamemode package.
Group: Systemd services
Requires: systemd

%description services
services components for the gamemode package.


%prep
%setup -q -n gamemode-1.8.1
cd %{_builddir}/gamemode-1.8.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1716729433
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gamemode-simulate-game
/usr/bin/gamemoded
/usr/bin/gamemodelist
/usr/bin/gamemoderun

%files config
%defattr(-,root,root,-)
/usr/lib/sysusers.d/gamemode.conf

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/services/com.feralinteractive.GameMode.service
/usr/share/gamemode/gamemode.ini
/usr/share/metainfo/io.github.feralinteractive.gamemode.metainfo.xml
/usr/share/polkit-1/actions/com.feralinteractive.GameMode.policy
/usr/share/polkit-1/rules.d/gamemode.rules

%files dev
%defattr(-,root,root,-)
/usr/include/gamemode_client.h
/usr/lib64/libgamemode.so
/usr/lib64/libgamemodeauto.so
/usr/lib64/pkgconfig/gamemode.pc
/usr/lib64/pkgconfig/libgamemodeauto.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgamemode.so.0
/usr/lib64/libgamemode.so.0.0.0
/usr/lib64/libgamemodeauto.so.0
/usr/lib64/libgamemodeauto.so.0.0.0

%files libexec
%defattr(-,root,root,-)
/usr/libexec/cpucorectl
/usr/libexec/cpugovctl
/usr/libexec/gpuclockctl
/usr/libexec/procsysctl

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gamemode-simulate-game.1
/usr/share/man/man1/gamemodelist.1
/usr/share/man/man1/gamemoderun.1
/usr/share/man/man8/gamemoded.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/gamemoded.service
