%define upstream_name XML-Dumper
%define upstream_version 0.81

Name:		perl-%{upstream_name}
Version:	0.81
Release:	3
Summary:	Perl module for dumping Perl objects from/to XML
License:	GPL+
Group:		Development/Perl
Url:		https://metacpan.org/dist/XML-Dumper
Source0:	https://cpan.metacpan.org/authors/id/M/MI/MIKEWONG/XML-Dumper-0.81.tar.gz
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl(XML::Parser)
BuildArch:	noarch

%description
Perl module for dumping Perl objects from/to XML.

%prep
%setup -q -n XML-Dumper-0.81

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test || :

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/XML
%{_mandir}/man3/*
