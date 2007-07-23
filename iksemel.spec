%define major 3
%define libname %mklibname %{name} %{major}

Summary:	Iksemel is an XML  parser library designed for Jabber applications
Name:		iksemel
Version:	1.2
Release:	%mkrel 2
License:	GPL
Group:		Networking/Instant messaging
URL:		http://iksemel.jabberstudio.org/
Source0:	%{name}-%{version}.tar.bz2
Requires(post):  install-info
Requires(preun): install-info
BuildRequires:	libtool
BuildRequires:	libgnutls-devel >= 0.1.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%package -n	%{libname}-devel
Summary:	Development files and headers for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{libname}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n	%{libname}-devel
iksemel is an XML (eXtensible Markup Language) parser library designed for
Jabber applications. It is coded in ANSI C for POSIX compatible environments, 
thus highly portable.

This package contains the development library and its header files
for the %{name} library.

%package -n	%{libname}-static-devel
Summary:	Static  %{name} development library
Group:		Development/C

%description -n	%{libname}-static-devel
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
%{_libdir}/lib*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files -n %{libname}-static-devel
%defattr(-,root,root)
%{_libdir}/lib*%{name}*.a
