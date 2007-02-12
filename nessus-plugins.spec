Summary:	Nessus plugins
Summary(pl.UTF-8):   Wtyczki do Nessusa
Name:		nessus-plugins
Version:	2.2.7
Release:	1
License:	GPL
Group:		Networking
Vendor:		Nessus Project
Source0:	ftp://ftp.nessus.org/pub/nessus/nessus-%{version}/src/%{name}-GPL-%{version}.tar.gz
# Source0-md5:	2e51f5ad96dd55888e835382a61de585
URL:		http://www.nessus.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	nessus-devel >= %{version}
BuildRequires:	nessus-libs-devel >= %{version}
Requires:	nessusd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# needed to use correct paths
%define		_localstatedir		/var/lib

%description
Plugins for Nessus - a free, powerful, up-to-date and easy to use
remote security scanner.

%description -l pl.UTF-8
Wtyczki do Nessusa - darmowego, potężnego, aktualnego i łatwego w
użyciu zdalnego skanera zabezpieczeń.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--enable-install=`whoami`
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# let strip succeed
chmod 755 $RPM_BUILD_ROOT%{_libdir}/nessus/plugins/*.nes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_libdir}/nessus/plugins/*.inc
%{_libdir}/nessus/plugins/*.nasl
%attr(755,root,root) %{_libdir}/nessus/plugins/*.nes
%{_libdir}/nessus/plugins_factory
%{_mandir}/man?/*
