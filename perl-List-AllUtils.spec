%define upstream_name    List-AllUtils
%define upstream_version 0.14
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Combines List::Util and List::MoreUtils in one bite-sized package

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/List/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::Warnings)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
Are you sick of trying to remember whether a particular helper is defined
in 'List::Util' or 'List::MoreUtils'? I sure am. Now you don't have to
remember. This module will export all of the functions that either of those
two modules defines.

%prep
%autosetup -p1 -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make test

%install
%make_install

%files
%doc META.yml Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/*
