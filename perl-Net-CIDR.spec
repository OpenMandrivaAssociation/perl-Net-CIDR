%define upstream_name	 Net-CIDR
%define upstream_version 0.14

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Manipulate IPv4/IPv6 netblocks in CIDR notation
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
With this module, you can manipulate IPv4/IPv6 netblocks in CIDR notation.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{_mandir}/*/*


%changelog
* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-1mdv2011.0
+ Revision: 552425
- update to 0.14

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2010.0
+ Revision: 404063
- rebuild using %%perl_convert_version

* Tue Jan 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-1mdv2009.1
+ Revision: 331588
- update to new version 0.13

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.11-6mdv2009.0
+ Revision: 257957
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.11-5mdv2009.0
+ Revision: 246035
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.11-3mdv2008.1
+ Revision: 140692
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-3mdv2008.0
+ Revision: 86681
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-2mdv2007.0
- Rebuild

* Tue Apr 18 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdk
- contributed by Cedric Devillers <brancaleone@altern.org>

