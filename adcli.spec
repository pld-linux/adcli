# TODO: verify heimdal patch
#
# Conditional build:
%bcond_with	krb5	# use MIT KRB5 instead of Heimdal Kerberos
%bcond_with	selinux	# SELinux support (requires policy sources)
#
Summary:	Helper library and tools for Active Directory client operations
Summary(pl.UTF-8):	Biblioteka pomocnicza i narzędzia do operacji klienckich usługi Active Directory
Name:		adcli
Version:	0.9.3.1
Release:	1
License:	LGPL v2+
Group:		Applications/System
#Source0Download: https://gitlab.freedesktop.org/realmd/adcli/-/releases
Source0:	https://gitlab.freedesktop.org/-/project/1196/uploads/5a1c55410c0965835b81fbd28d820d46/%{name}-%{version}.tar.gz
# Source0-md5:	0826e7b6cac1df6dd1b6509507b384ed
Patch0:		%{name}-heimdal.patch
URL:		https://www.freedesktop.org/software/realmd/adcli/
BuildRequires:	cyrus-sasl-devel
%{!?with_krb5:BuildRequires:	heimdal-devel}
%{?with_krb5:BuildRequires:	krb5-devel}
BuildRequires:	libxslt-progs
BuildRequires:	openldap-devel
BuildRequires:	xmlto
%if %{with selinux}
BuildRequires:	libselinux-devel
# policy sources (/usr/share/selinux/devel/Makefile)
BuildRequires:	selinux-policy-???
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Helper library and tools for Active Directory client operations.

%description -l pl.UTF-8
Biblioteka pomocnicza i narzędzia do operacji klienckich usługi Active
Directory.

%prep
%setup -q
%{!?with_krb5:%patch -P0 -p1}

%build
%configure \
	%{!?with_selinux:--disable-selinux-support} \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_sbindir}/adcli
%{_mandir}/man8/adcli.8*
%{_docdir}/adcli
