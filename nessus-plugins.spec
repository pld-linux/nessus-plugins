Summary:	Nessus plugins
Summary(pl):	Wtyczki do Nessusa
Name:		nessus-plugins
Version:	1.2.5
Release:	1
License:	GPL
Group:		Networking
Vendor:		Nessus Project
Source0:	ftp://ftp.nessus.org/pub/nessus/nessus-%{version}/src/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.nessus.org/
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugins for Nessus - a free, powerful, up-to-date and easy to use
remote security scanner.

%description -l pl
Biblioteki dla Nessusa - wolnego, pot�nego, aktualnego i �atwego w
u�yciu zdalnego skanera zabezpiecze�.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
aclocal
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

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
