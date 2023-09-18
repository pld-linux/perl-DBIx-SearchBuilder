#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	DBIx
%define		pnam	SearchBuilder
Summary:	DBIx::SearchBuilder - easy SQL SELECT Statement generation
Summary(pl.UTF-8):	DBIx::SearchBuilder - łatwe generowanie polecenia SQL SELECT
Name:		perl-DBIx-SearchBuilder
Version:	1.78
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DBIx/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	61f8cb4bb9913913ffd90d64ebfeb623
URL:		http://search.cpan.org/dist/DBIx-SearchBuilder/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Cache::Simple::TimedExpiry) >= 0.21
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Class::ReturnValue) >= 0.4
BuildRequires:	perl(DBIx::DBSchema)
BuildRequires:	perl(Want)
BuildRequires:	perl-Clone
BuildRequires:	perl-DBD-SQLite
BuildRequires:	perl-DBI
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.42
BuildRequires:	perl-capitalization >= 0.03
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_perl		DBD::Oracle

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
%doc Changes README
%{perl_vendorlib}/DBIx/*.pm
%{perl_vendorlib}/DBIx/SearchBuilder
%{_mandir}/man3/*
