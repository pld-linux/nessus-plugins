Summary:	Nessus plugins
Summary(pl):	Wtyczki do Nessusa
Name:		nessus-plugins
Version:	2.2.4
Release:	1
License:	GPL
Group:		Networking
Vendor:		Nessus Project
Source0:	ftp://ftp.nessus.org/pub/nessus/nessus-%{version}/src/%{name}-GPL-%{version}.tar.gz
# Source0-md5:	1e77107aa358ae9b9eba22154c1ca48d
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

%description -l pl
Wtyczki do Nessusa - darmowego, potê¿nego, aktualnego i ³atwego w
u¿yciu zdalnego skanera zabezpieczeñ.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_libdir}/nessus/plugins/*
%{_libdir}/nessus/plugins_factory
%{_mandir}/man?/*
