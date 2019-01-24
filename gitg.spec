#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gitg
Version  : 3.30.1
Release  : 1
URL      : https://github.com/GNOME/gitg/archive/v3.30.1.tar.gz
Source0  : https://github.com/GNOME/gitg/archive/v3.30.1.tar.gz
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
BuildRequires : libgee-dev
BuildRequires : libgit2-dev
BuildRequires : libgit2-glib
BuildRequires : libgit2-glib-dev
BuildRequires : libpeas-dev
BuildRequires : libsecret-dev
BuildRequires : libsoup-dev
BuildRequires : vala
Patch1: build.patch

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
Requires: gitg-man = %{version}-%{release}

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
%setup -q -n gitg-3.30.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1548352305
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gitg
cp COPYING %{buildroot}/usr/share/package-licenses/gitg/COPYING
cp win32/installer/COPYING.rtf %{buildroot}/usr/share/package-licenses/gitg/win32_installer_COPYING.rtf
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
/usr/share/applications/gitg.desktop
/usr/share/gitg/icons/hicolor/scalable/actions/diff-symbolic.svg
/usr/share/glade/catalogs/gitg-glade.xml
/usr/share/glib-2.0/schemas/org.gnome.gitg.gschema.xml
/usr/share/icons/hicolor/16x16/apps/gitg.png
/usr/share/icons/hicolor/22x22/apps/gitg.png
/usr/share/icons/hicolor/24x24/apps/gitg.png
/usr/share/icons/hicolor/256x256/apps/gitg.png
/usr/share/icons/hicolor/32x32/apps/gitg.png
/usr/share/icons/hicolor/48x48/apps/gitg.png
/usr/share/icons/hicolor/scalable/apps/gitg-symbolic.svg
/usr/share/metainfo/gitg.appdata.xml

%files dev
%defattr(-,root,root,-)
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
/usr/share/package-licenses/gitg/COPYING
/usr/share/package-licenses/gitg/win32_installer_COPYING.rtf

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

