#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-CDDB-File
Version  : 1.05
Release  : 30
URL      : https://cpan.metacpan.org/authors/id/T/TM/TMTM/CDDB-File-1.05.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TM/TMTM/CDDB-File-1.05.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libc/libcddb-file-perl/libcddb-file-perl_1.05-2.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: perl-CDDB-File-license = %{version}-%{release}
Requires: perl-CDDB-File-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
CDDB::File - Parse a CDDB/freedb data file
SYNOPSIS
my $disc = CDDB::File->new("rock/f4109511");

%package dev
Summary: dev components for the perl-CDDB-File package.
Group: Development
Provides: perl-CDDB-File-devel = %{version}-%{release}
Requires: perl-CDDB-File = %{version}-%{release}

%description dev
dev components for the perl-CDDB-File package.


%package license
Summary: license components for the perl-CDDB-File package.
Group: Default

%description license
license components for the perl-CDDB-File package.


%package perl
Summary: perl components for the perl-CDDB-File package.
Group: Default
Requires: perl-CDDB-File = %{version}-%{release}

%description perl
perl components for the perl-CDDB-File package.


%prep
%setup -q -n CDDB-File-1.05
cd %{_builddir}
tar xf %{_sourcedir}/libcddb-file-perl_1.05-2.debian.tar.xz
cd %{_builddir}/CDDB-File-1.05
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/CDDB-File-1.05/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-CDDB-File
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-CDDB-File/a3c85b1af07e6347dd1506c652b212f7f7c3f562 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/CDDB::File.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-CDDB-File/a3c85b1af07e6347dd1506c652b212f7f7c3f562

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
