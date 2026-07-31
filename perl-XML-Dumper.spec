%define	upstream_name	 XML-Dumper
%define upstream_version 0.81
Name:       perl-%{upstream_name}
Version:	0.81
Release:	14

Summary:	Perl module for dumping Perl objects from/to XML
License:	GPL
Group:		Development/Perl
Url:		https://metacpan.org/dist/XML-Dumper
Source0:	https://cpan.metacpan.org/authors/id/M/MI/MIKEWONG/XML-Dumper-0.81.tar.gz

BuildRequires:	make
Buildrequires:	perl-devel
BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl(XML::Parser)
BuildArch: 	noarch

%description
Perl module for dumping Perl objects from/to XML.

%prep
%setup -q -n XML-Dumper-0.81

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/XML


