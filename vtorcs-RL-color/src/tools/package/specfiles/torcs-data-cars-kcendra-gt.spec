Summary: TORCS - K/Cendra Grand Tourisme Cars Pack
Name: TORCS-data-cars-kcendra-gt
Version: 1.3.1
Release: 1
Epoch: 1
Source: TORCS-%{version}-data-cars-kcendra-gt.tgz
Group: Amusements/Games
BuildRoot: %{_tmppath}/%{name}-buildroot
Copyright: K/Cendra
BuildArch: noarch
URL: http://torcs.org
Packager: Eric Espi� <Eric.Espie@free.fr>
Requires: TORCS

%description
K/Cendra Grand Tourisme Car Packs for TORCS.
PLEASE, these files may NOT BE EDITED or COPIED in any way.
http://www.kcendra.com

%prep
%setup -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/share/games/torcs
cp -r * $RPM_BUILD_ROOT/%{_prefix}/share/games/torcs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_prefix}/share/games/torcs/*

%changelog
* Mon Aug 25 2003 Eric Espi� <Eric.Espie@free.fr> 1.2.2
- initial RPM
