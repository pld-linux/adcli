# TODO: verify heimdal patch
#
# Conditional build:
%bcond_with	krb5	# use MIT KRB5 instead of Heimdal Kerberos
#
Summary:	Helper library and tools for Active Directory client operations
Summary(pl.UTF-8):	Biblioteka pomocnicza i narzędzia do operacji klienckich usługi Active Directory
Name:		adcli
Version:	0.9.2
Release:	1
License:	LGPL v2+
Group:		Applications/System
#Source0Download: https://gitlab.freedesktop.org/realmd/adcli/-/releases
Source0:	https://gitlab.freedesktop.org/realmd/adcli/uploads/ea560656ac921b3fe0d455976aaae9be/%{name}-%{version}.tar.gz
# Source0-md5:	7f6ae35ac2c16632812641c724b32e30
Patch0:		%{name}-heimdal.patch
URL:		https://www.freedesktop.org/software/realmd/adcli/
BuildRequires:	cyrus-sasl-devel
%{!?with_krb5:BuildRequires:	heimdal-devel}
%{?with_krb5:BuildRequires:	krb5-devel}
BuildRequires:	libxslt-progs
BuildRequires:	openldap-devel
BuildRequires:	xmlto
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
