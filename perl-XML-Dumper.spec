%define	module	XML-Dumper
%define	name	perl-%{module}
%define	version	0.81
%define	release	%mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl module for dumping Perl objects from/to XML
License:	GPL
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl(Compress::Zlib)
BuildArch: 	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Perl module for dumping Perl objects from/to XML.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/XML

