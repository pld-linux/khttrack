Summary:	Khttrack is a front-end to Httrack
Summary(pl):	Graficzna nak³adka na Httrack
Name:		khttrack
Version:	0.10
Release:	0.1
License:	GPL
Group:		X11/Applications/Networking	
Source0:	http://ftp.gnu.org/savannah/files/khttrack/stable.pkg/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	1193cd59d7a56d499551a077423f539c
Source1:	%{name}.png
Source2:	%{name}.desktop
URL:		http://savannah.nongnu.org/projects/khttrack/
BuildRequires:	httrack-devel
BuildRequires:	kdelibs-devel
BuildRequires:	openssl-devel >= 0.9.7d
Requires:	httrack
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Khttrack is a front-end to Httrack, used as library, for Kde.

%description -l pl
Khttrack jest graficzn± nak³adka na Httrack opart± na bibliotece qt.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/%{name}
%{_desktopdir}/%{name}.desktop
# XXX: use hicolor, locolor no longer exists
#%{_iconsdir}/locolor/16x16/apps/khttrack.png
#%{_iconsdir}/locolor/32x32/apps/khttrack.png
%{_pixmapsdir}/%{name}.png
