%define modname	Net-CIDR
%define modver	0.17

Summary:	Manipulate IPv4/IPv6 netblocks in CIDR notation
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	5
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Net/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
With this module, you can manipulate IPv4/IPv6 netblocks in CIDR notation.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Net
%{_mandir}/man3/*

