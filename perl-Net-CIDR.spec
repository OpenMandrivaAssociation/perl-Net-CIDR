%define modname	Net-CIDR
Summary:	Manipulate IPv4/IPv6 netblocks in CIDR notation
Name:		perl-%{modname}
Version:	0.27
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{modname}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Net/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-devel

%description
With this module, you can manipulate IPv4/IPv6 netblocks in CIDR notation.

%prep
%setup -qn %{modname}-%{version}

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

