#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define		pdir	DBIx
%define		pnam	SearchBuilder
Summary:	DBIx::SearchBuilder - easy SQL SELECT Statement generation
Summary(pl):	DBIx::SearchBuilder - �atwe generowanie polecenia SQL SELECT
Name:		perl-DBIx-SearchBuilder
Version:	1.16
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f0d84a67e4a30fc5d21cf0ce9c2948b5
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DBD-SQLite
BuildRequires:	perl-DBI
BuildRequires:	perl-Class-ReturnValue
BuildRequires:	perl-Cache-Simple-TimedExpiry
BuildRequires:	perl-Test-Pod >= 1.00
BuildRequires:	perl-Want
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBIx::SearchBuilder -- easy SQL SELECT Statement generation.

%description -l pl
DBIx::SearchBuilder -- �atwe generowanie polecenia SQL SELECT.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
