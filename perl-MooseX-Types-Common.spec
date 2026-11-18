#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	MooseX
%define		pnam	Types-Common
Summary:	MooseX::Types::Common - A library of commonly used type constraints
Name:		perl-MooseX-Types-Common
Version:	0.001015
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/MooseX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	05e873b43913f4fbceb2a603ddcd93e3
URL:		http://search.cpan.org/dist/MooseX-Types-Common/
BuildRequires:	perl-Module-Build-Tiny >= 0.034
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Moose >= 0.39
BuildRequires:	perl-MooseX-Types >= 0.04
BuildRequires:	perl-Test-Deep
BuildRequires:	perl-Test-Warnings >= 0.005
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of commonly-used type constraints that do not ship with Moose by
default.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	--perl=%{__perl} \
	--installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MooseX/Types/*.pm
%{perl_vendorlib}/MooseX/Types/Common
%{_mandir}/man3/*
