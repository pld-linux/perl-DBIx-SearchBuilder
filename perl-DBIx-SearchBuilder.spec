%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	SearchBuilder
Summary:	DBIx::SearchBuilder -- easy SQL SELECT Statement generation
Summary(pl):	DBIx::SearchBuilder -- ³atwe generowanie polecenia SQL SELECT
Name:		perl-%{pdir}-%{pnam}
Version:	0.92
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8827c5c1889489f7659ac4aad6e7dae4
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Class-DBI
BuildRequires:	perl-Class-ReturnValue
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBIx::SearchBuilder -- easy SQL SELECT Statement generation.

%description -l pl
DBIx::SearchBuilder -- ³atwe generowanie polecenia SQL SELECT.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
