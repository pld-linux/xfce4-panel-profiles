Summary:	Application to manage Xfce panel layouts
Name:		xfce4-panel-profiles
Version:	1.0.15
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/apps/xfce4-panel-profiles/1.0/%{name}-%{version}.tar.bz2
# Source0-md5:	296b39f316edd18a0213e406ae5673c4
URL:		https://git.xfce.org/apps/xfce4-panel-profiles/about/
BuildRequires:	python3
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	xfce4-panel-devel >= 4.16.0
Requires:	python3-pygobject3
Requires:	xfce4-panel >= 4.16.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xfce4 Panel Profiles (xfce4-panel-profiles, formerly known as
xfpanel-switch) is a simple application to manage Xfce panel layouts.

With the modular Xfce Panel, a multitude of panel layouts can be
created. This tool makes it possible to backup, restore, import, and
export these panel layouts.

%prep
%setup -q

# fix #!/usr/bin/env python3 -> #!/usr/bin/python3:
%{__sed} -i -e '1s,^#!.*python3,#!%{__python3},' xfce4-panel-profiles/*.py

%build
./configure \
	--prefix=%{_prefix}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{fa_IR,hye,ie}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hy}

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/xfce4-panel-profiles

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/xfce4-panel-profiles
%{_desktopdir}/org.xfce.PanelProfiles.desktop
%{_datadir}/metainfo/org.xfce.PanelProfiles.appdata.xml
%dir %{_datadir}/xfce4-panel-profiles
%{_datadir}/xfce4-panel-profiles/layouts
%dir %{_datadir}/xfce4-panel-profiles/xfce4-panel-profiles
%{_datadir}/xfce4-panel-profiles/xfce4-panel-profiles/info.py
%{_datadir}/xfce4-panel-profiles/xfce4-panel-profiles/panelconfig.py
%{_datadir}/xfce4-panel-profiles/xfce4-panel-profiles/xfce4-panel-profiles.glade
%{_datadir}/xfce4-panel-profiles/xfce4-panel-profiles/xfce4-panel-profiles.py
%{_iconsdir}/hicolor/*/apps/org.xfce.PanelProfiles.*
%{_mandir}/man1/xfce4-panel-profiles.1*
