%define upstream_name    List-AllUtils
%define upstream_version 0.04
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Combines List::Util and List::MoreUtils in one bite-sized package
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/List/List-AllUtils-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.20.0-2mdv2011.0
+ Revision: 653598
- rebuild for updated spec-helper

* Mon Aug 23 2010 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2011.0
+ Revision: 572190
- import perl-List-AllUtils


* Mon Aug 23 2010 cpan2dist 0.02-1mdv
- initial mdv release, generated with cpan2dist


