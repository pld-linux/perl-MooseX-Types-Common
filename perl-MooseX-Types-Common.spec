#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	MooseX
%define		pnam	Types-Common
%include	/usr/lib/rpm/macros.perl
Summary:	MooseX::Types::Common - A library of commonly used type constraints
#Summary(pl.UTF-8):	
Name:		perl-MooseX-Types-Common
Version:	0.001004
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7e6ac09fc14143362a8b1d1e66cd9543
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/MooseX-Types-Common/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Moose >= 0.39
BuildRequires:	perl-MooseX-Types >= 0.04
BuildRequires:	perl-Test-Fatal
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of commonly-used type constraints that do not ship with Moose by default.



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MooseX/Types/*.pm
%{perl_vendorlib}/MooseX/Types/Common
%{_mandir}/man3/*
