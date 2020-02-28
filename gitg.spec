#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gitg
Version  : 3.32.1
Release  : 10
URL      : https://github.com/GNOME/gitg/archive/v3.32.1/gitg-3.32.1.tar.gz
Source0  : https://github.com/GNOME/gitg/archive/v3.32.1/gitg-3.32.1.tar.gz
Summary  : GNOME GUI client to view git repositories
Group    : Development/Tools
License  : GPL-2.0
Requires: gitg-bin = %{version}-%{release}
Requires: gitg-data = %{version}-%{release}
Requires: gitg-lib = %{version}-%{release}
Requires: gitg-license = %{version}-%{release}
Requires: gitg-locales = %{version}-%{release}
Requires: gitg-man = %{version}-%{release}
Requires: gitg-python = %{version}-%{release}
Requires: gitg-python3 = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : compat-gtksourceview-soname3-dev
BuildRequires : gtksourceview-dev
BuildRequires : gtkspell3-dev
BuildRequires : intltool
BuildRequires : libdazzle-dev
BuildRequires : libgee-dev
BuildRequires : libgit2-dev
BuildRequires : libgit2-glib
BuildRequires : libgit2-glib-dev
BuildRequires : libpeas-dev
BuildRequires : libsecret-dev
BuildRequires : libsoup-dev
BuildRequires : pkgconfig(libdazzle-1.0)
BuildRequires : pkgconfig(libpeas-1.0)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : vala

%description
To create the installer you need to follow the next steps:
- install the latest version of msys2: http://msys2.github.io/
- launch msys2_shell.bat and update it with pacman -Syu, you will need to
relaunch msys2_shell.bat after updating it
- install git: pacman -S git
- clone gedit: git clone git://git.gnome.org/gitg
- cd gitg/win32
- edit make-installer and set the right version of gitg
- ./make-installer.bat

%package bin
Summary: bin components for the gitg package.
Group: Binaries
Requires: gitg-data = %{version}-%{release}
Requires: gitg-license = %{version}-%{release}

%description bin
bin components for the gitg package.


%package data
Summary: data components for the gitg package.
Group: Data

%description data
data components for the gitg package.


%package dev
Summary: dev components for the gitg package.
Group: Development
Requires: gitg-lib = %{version}-%{release}
Requires: gitg-bin = %{version}-%{release}
Requires: gitg-data = %{version}-%{release}
Provides: gitg-devel = %{version}-%{release}
Requires: gitg = %{version}-%{release}
Requires: gitg = %{version}-%{release}

%description dev
dev components for the gitg package.


%package lib
Summary: lib components for the gitg package.
Group: Libraries
Requires: gitg-data = %{version}-%{release}
Requires: gitg-license = %{version}-%{release}

%description lib
lib components for the gitg package.


%package license
Summary: license components for the gitg package.
Group: Default

%description license
license components for the gitg package.


%package locales
Summary: locales components for the gitg package.
Group: Default

%description locales
locales components for the gitg package.


%package man
Summary: man components for the gitg package.
Group: Default

%description man
man components for the gitg package.


%package python
Summary: python components for the gitg package.
Group: Default
Requires: gitg-python3 = %{version}-%{release}

%description python
python components for the gitg package.


%package python3
Summary: python3 components for the gitg package.
Group: Default
Requires: python3-core

%description python3
python3 components for the gitg package.


%prep
%setup -q -n gitg-3.32.1
cd %{_builddir}/gitg-3.32.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582930143
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gitg
cp %{_builddir}/gitg-3.32.1/COPYING %{buildroot}/usr/share/package-licenses/gitg/881b050efe0ca3ad845b81debc6c1b4a1afa5a3e
cp %{_builddir}/gitg-3.32.1/win32/installer/COPYING.rtf %{buildroot}/usr/share/package-licenses/gitg/628dd34e8502d93640e1b43692527e4ea54ccf2e
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gitg

%files
%defattr(-,root,root,-)
/usr/lib64/gitg/plugins/diff.plugin
/usr/lib64/gitg/plugins/files.plugin

%files bin
%defattr(-,root,root,-)
/usr/bin/gitg

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Gitg-1.0.typelib
/usr/lib64/girepository-1.0/GitgExt-1.0.typelib
/usr/share/applications/org.gnome.gitg.desktop
/usr/share/gir-1.0/*.gir
/usr/share/gitg/icons/hicolor/scalable/actions/diff-symbolic.svg
/usr/share/glade/catalogs/gitg-glade.xml
/usr/share/glib-2.0/schemas/org.gnome.gitg.gschema.xml
/usr/share/icons/hicolor/16x16/apps/org.gnome.gitg.png
/usr/share/icons/hicolor/22x22/apps/org.gnome.gitg.png
/usr/share/icons/hicolor/24x24/apps/org.gnome.gitg.png
/usr/share/icons/hicolor/256x256/apps/org.gnome.gitg.png
/usr/share/icons/hicolor/32x32/apps/org.gnome.gitg.png
/usr/share/icons/hicolor/48x48/apps/org.gnome.gitg.png
/usr/share/icons/hicolor/scalable/apps/org.gnome.gitg-symbolic.svg
/usr/share/metainfo/org.gnome.gitg.appdata.xml
/usr/share/vala/vapi/libgitg-1.0.vapi
/usr/share/vala/vapi/libgitg-ext-1.0.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/libgitg-1.0/libgitg/libgitg.h
/usr/include/libgitg-ext-1.0/libgitg-ext/libgitg-ext.h
/usr/lib64/libgitg-1.0.so
/usr/lib64/libgitg-ext-1.0.so
/usr/lib64/pkgconfig/libgitg-1.0.pc
/usr/lib64/pkgconfig/libgitg-ext-1.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/gitg/plugins/libdiff.so
/usr/lib64/gitg/plugins/libfiles.so
/usr/lib64/libgitg-1.0.so.0
/usr/lib64/libgitg-1.0.so.0.0.0
/usr/lib64/libgitg-ext-1.0.so.0
/usr/lib64/libgitg-ext-1.0.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gitg/628dd34e8502d93640e1b43692527e4ea54ccf2e
/usr/share/package-licenses/gitg/881b050efe0ca3ad845b81debc6c1b4a1afa5a3e

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gitg.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f gitg.lang
%defattr(-,root,root,-)

