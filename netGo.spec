Summary:	An application which allows changing network-settings quickly
Summary(pl.UTF-8):	Aplikacja pozwalająca szybko zmienić ustawienia sieciowe
Name:		netgo
Version:	0.5
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://netgo.hjolug.org/files/v0.5/%{name}-%{version}.tar.gz
# Source0-md5:	fe62a4035e6449db9761f8724d26d458
Source1:	%{name}.desktop
URL:		http://netgo.hjolug.org
BuildRequires:	kdebase-devel
BuildRequires:	qt-devel >= 3.2
BuildRequires:	sed >= 4.0
Requires:	net-tools
Requires:	wireless-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
netGo is an application which allows changing network-settings quickly
and simply for certain networks. It is specially directed towards
laptop-owners who often need to change network-settings when
relocating to school, work, home, etc. netGo allows setting "profiles"
that contain the network settings such as the IP, netmask, gateway,
nameservers, etc... After creating a profile the user can execute its
network settings with a single click!

%description -l pl.UTF-8
netGo jest aplikacją pozwalającą na zmianę pewnych parametrów
sieciowych w prosty i szybki sposób. Przede wszystkim jest dedykowana
dla użytkowników komputerów przenośnych, którzy często zmieniają
ustawienia sieciowe. NetGo pozwala na tworzenie profili zawierających
takie dane jak IP, maska podsieci etc.. Po stworzeniu profili
użytkownicy mogą przełączać się między nimi pojedynczym kliknięciem.

%prep
%setup -q

rm -f netgo-bin
sed -i -e 's,/usr/share/netgo/netgo-bin,%{_libdir}/netgo/netgo-bin,' netgo

%build
export QTDIR=%{_prefix}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name},%{_desktopdir},%{_iconsdir}/hicolor/32x32/apps}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install icons/satelite_32x32.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install netgo-bin $RPM_BUILD_ROOT%{_libdir}/%{name}
install netgo $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README TODO
%attr (755,root,root) %{_bindir}/*
%attr (755,root,root) %{_libdir}/%{name}
%{_iconsdir}/hicolor/32x32/apps/*
%{_desktopdir}/%{name}.desktop
