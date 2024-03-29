Summary:	Khttrack is a front-end to Httrack
Summary(pl.UTF-8):	Graficzna nakładka na Httrack
Name:		khttrack
Version:	0.10
Release:	1
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
BuildRequires:	sed >= 4.0
Requires:	hicolor-icon-theme
Requires:	httrack
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Khttrack is a front-end to Httrack, used as library, for Kde.

%description -l pl.UTF-8
Khttrack jest graficzną nakładka na Httrack opartą na bibliotece qt.

%prep
%setup -q

%build
#locolor --> hicolor
sed -i -e 's/locolor/hicolor/g' khttrack/*
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
%{_iconsdir}/hicolor/*x*/apps/khttrack.png
%{_pixmapsdir}/%{name}.png
