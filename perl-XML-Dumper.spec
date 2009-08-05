%define	upstream_name	 XML-Dumper
%define	upstream_version 0.81

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl module for dumping Perl objects from/to XML
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl(XML::Parser)
BuildArch: 	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Perl module for dumping Perl objects from/to XML.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
