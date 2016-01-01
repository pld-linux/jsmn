Summary:	Minimalistic JSON parser library in C
Name:		jsmn
Version:	0.0.0
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		http://zserge.com/jsmn.html
Source0:	https://github.com/zserge/jsmn/archive/4a54ae6/%{name}-%{version}.tar.gz
# Source0-md5:	749dcd1163d005d9adba985308d9edb2
Source1:	CMakeLists.txt
BuildRequires:	cmake
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
jsmn (pronounced like 'jasmine') is a minimalistic JSON parser in C
with a focus on simplicity and efficiency.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
jsmn (pronounced like 'jasmine') is a minimalistic JSON parser in C
with a focus on simplicity and efficiency.

This package contains development files for %{name}.

%prep
%setup -qc
mv jsmn-*/* .
cp %{SOURCE1} .
rm Makefile

%build
%cmake \
	-DLIB_INSTALL_DIR=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_libdir}/libjsmn.so.*.*.*
%ghost %{_libdir}/libjsmn.so.0

%files devel
%defattr(644,root,root,755)
%doc LICENSE README.md example
%{_includedir}/jsmn.h
%{_libdir}/libjsmn.so
