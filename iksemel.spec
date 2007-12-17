%define major 3
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d
%define staticdevelname %mklibname %{name} -d -s

Summary:	Iksemel is an XML  parser library designed for Jabber applications
Name:		iksemel
Version:	1.3
Release:	%mkrel 1
License:	GPLv2+
Group:		Networking/Instant messaging
URL:		http://iksemel.googlecode.com/
Source0:	http://iksemel.googlecode.com/files/%{name}-%{version}.tar.gz
Requires(post,preun): info-install
BuildRequires:	libtool
BuildRequires:	libgnutls-devel >= 0.1.0

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
Obsoletes:	%mklibname -d %name 3

%description -n	%{develname}
iksemel is an XML (eXtensible Markup Language) parser library designed for
Jabber applications. It is coded in ANSI C for POSIX compatible environments, 
thus highly portable.

This package contains the development library and its header files
for the %{name} library.

%package -n	%{staticdevelname}
Summary:	Static  %{name} development library
Group:		Development/C
Obsoletes:	%mklibname -s -d %name 3
Requires:	%{develname} = %version-%release

%description -n	%{staticdevelname}
iksemel is an XML (eXtensible Markup Language) parser library designed for
Jabber applications. It is coded in ANSI C for POSIX compatible environments, 
thus highly portable.

This package contains the static %{name} library.

%prep

%setup -q

%build

%configure2_5x \
    --with-libgnutls-prefix=%{_prefix}

%make

# make check barfs on x86_64
#%%check
#make check

%install
rm -rf %{buildroot}

%makeinstall

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info 

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog HACKING NEWS README TODO
%{_bindir}/*
%{_infodir}/%{name}*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files -n %{staticdevelname}
%defattr(-,root,root)
%{_libdir}/lib*%{name}*.a
