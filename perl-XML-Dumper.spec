%define	upstream_name	 XML-Dumper
%define	upstream_version 0.81

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    6

Summary:	Perl module for dumping Perl objects from/to XML
License:	GPL
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

Buildrequires:	perl-devel
BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl(XML::Parser)
BuildArch: 	noarch

%description
Perl module for dumping Perl objects from/to XML.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/XML


%changelog
* Wed Aug 05 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.810.0-1mdv2010.0
+ Revision: 410100
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.81-5mdv2009.0
+ Revision: 242199
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.81-3mdv2008.0
+ Revision: 23518
- rebuild


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.81-2mdk
- Fix According to perl Policy
	- BuildRequires

* Sat Apr 08 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.81-1mdk
- New release 0.81
- spec cleanup
- %%mkrel

* Mon Sep 26 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.79-1mdk
- 0.79

* Fri Jul 15 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.76-1mdk
- 0.76

* Mon Jun 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.74-1mdk
- 0.74

* Thu Jun 03 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.71-1mdk
- 0.71
- drop prefix and distribution tag
- drop redundant requires
- cosmetics

* Fri Dec 19 2003 Michael Scherer <misc@mandrake.org> 0.67-3mdk
- Fix BuildRequires ( perl-Compress-Zlib )

* Mon Sep 01 2003 François Pons <fpons@mandrakesoft.com> 0.67-2mdk
- fixed requires on /usr/local/bin/perl.
- using %%makeinstall_std.

* Wed Aug 27 2003 François Pons <fpons@mandrakesoft.com> 0.67-1mdk
- 0.67.

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.4-6mdk
- rebuild for new auto{prov,req}

