Summary:	Nessus plugins
Summary(pl):	Wtyczki do Nessusa
Name:		nessus-plugins
Version:	2.0.1
Release:	1
License:	GPL
Group:		Networking
Vendor:		Nessus Project
Source0:	ftp://ftp.nessus.org/pub/nessus/nessus-%{version}/src/%{name}-%{version}.tar.gz
URL:		http://www.nessus.org/
Requires:		nessusd
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	nessus-devel
BuildRequires:	nessus-libs-devel
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugins for Nessus - a free, powerful, up-to-date and easy to use
remote security scanner.

%description -l pl
Wtyczki do Nessusa - wolnego, potê¿nego, aktualnego i ³atwego w
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
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/nessus
%{_mandir}/man?/*
