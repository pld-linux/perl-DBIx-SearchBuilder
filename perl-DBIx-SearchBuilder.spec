%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	SearchBuilder
Summary:	DBIx::SearchBuilder -- easy SQL SELECT Statement generation
Summary(pl):	DBIx::SearchBuilder -- ³atwe generowanie polecenia SQL SELECT
Name:		perl-%{pdir}-%{pnam}
Version:	0.73
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBIx::SearchBuilder -- easy SQL SELECT Statement generation.

%description -l pl
DBIx::SearchBuilder -- ³atwe generowanie polecenia SQL SELECT.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{perl_sitelib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
