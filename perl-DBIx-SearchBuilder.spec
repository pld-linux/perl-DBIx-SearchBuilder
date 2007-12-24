#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DBIx
%define		pnam	SearchBuilder
Summary:	DBIx::SearchBuilder - easy SQL SELECT Statement generation
Summary(pl.UTF-8):	DBIx::SearchBuilder - łatwe generowanie polecenia SQL SELECT
Name:		perl-DBIx-SearchBuilder
Version:	1.50
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DBIx/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	36d745d3469d7fd9318c393557eca6da
URL:		http://search.cpan.org/dist/DBIx-SearchBuilder/
BuildRequires:	perl-Cache-Simple-TimedExpiry
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-Class-ReturnValue
BuildRequires:	perl-Clone
BuildRequires:	perl-DBD-SQLite
BuildRequires:	perl-DBI
BuildRequires:	perl-DBIx-DBSchema
BuildRequires:	perl-Encode
BuildRequires:	perl-Want
BuildRequires:	perl-capitalization
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Pod >= 1.00
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(DBD::Oracle)'

%description
DBIx::SearchBuilder -- easy SQL SELECT Statement generation.

%description -l pl.UTF-8
DBIx::SearchBuilder -- łatwe generowanie polecenia SQL SELECT.

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
