%define major 3
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d
%define staticdevelname %mklibname %{name} -d -s

Summary:	XML  parser library designed for Jabber applications
Name:		iksemel
Version:	1.4
Release:	3
License:	GPLv2+
Group:		Networking/Instant messaging
URL:		http://iksemel.googlecode.com/
Source0:	http://iksemel.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		iksemel-1.3-gnutls-2.8.patch
BuildRequires:	libtool
BuildRequires:	pkgconfig(gnutls)

%description
iksemel is an XML (eXtensible Markup Language) parser library designed for
Jabber applications. It is coded in ANSI C for POSIX compatible environments, 
thus highly portable.
 
%package -n	%{libname}
Summary:	Shared Libraries for %{name}
Group:		System/Libraries

%description -n	%{libname}
iksemel is an XML (eXtensible Markup Language) parser library designed for
Jabber applications. It is coded in ANSI C for POSIX compatible environments, 
thus highly portable.

This package contains the shared %{name} library.

%package -n	%{develname}
Summary:	Development files and headers for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{libname}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname -d %{name} 3

%description -n	%{develname}
iksemel is an XML (eXtensible Markup Language) parser library designed for
Jabber applications. It is coded in ANSI C for POSIX compatible environments, 
thus highly portable.

This package contains the development library and its header files
for the %{name} library.

%package -n	%{staticdevelname}
Summary:	Static  %{name} development library
Group:		Development/C
Obsoletes:	%mklibname -s -d %{name} 3
Requires:	%{develname} = %{version}-%{release}

%description -n	%{staticdevelname}
iksemel is an XML (eXtensible Markup Language) parser library designed for
Jabber applications. It is coded in ANSI C for POSIX compatible environments, 
thus highly portable.

This package contains the static %{name} library.

%prep
%setup -q
%patch0 -p0

%build
autoreconf -fi
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%doc AUTHORS COPYING ChangeLog HACKING NEWS README TODO
%{_bindir}/*
%{_infodir}/%{name}*

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files -n %{staticdevelname}
%{_libdir}/lib*%{name}*.a
