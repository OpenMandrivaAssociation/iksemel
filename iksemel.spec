%define major 3
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d
%define staticdevelname %mklibname %{name} -d -s

Summary:	XML  parser library designed for Jabber applications
Name:		iksemel
Version:	1.4
Release:	11
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
autoreconf -fiv
%configure2_5x --enable-static
%make

%install
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


%changelog
* Wed Jun 13 2012 Andrey Bondrov <abondrov@mandriva.org> 1.4-3
+ Revision: 805349
- Fix BuildRequires
- Drop some legacy junk

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4-2mdv2011.0
+ Revision: 611177
- rebuild

* Sun Nov 15 2009 Funda Wang <fwang@mandriva.org> 1.4-1mdv2010.1
+ Revision: 466179
- new version 1.4

* Wed Jun 03 2009 Funda Wang <fwang@mandriva.org> 1.3-5mdv2010.0
+ Revision: 382373
- rebuild for gnutls 2.8

* Wed Jul 09 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3-4mdv2009.0
+ Revision: 233037
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.3-3mdv2008.1
+ Revision: 170895
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Tue Jan 22 2008 Funda Wang <fwang@mandriva.org> 1.3-2mdv2008.1
+ Revision: 156358
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Dec 09 2007 Funda Wang <fwang@mandriva.org> 1.3-1mdv2008.1
+ Revision: 116648
- New version 1.3

* Sun Sep 16 2007 Funda Wang <fwang@mandriva.org> 1.2-3mdv2008.0
+ Revision: 87949
- fix bu#26905
- New devel package policy

* Mon Jul 23 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2-2mdv2008.0
+ Revision: 54741
- Import iksemel



* Mon Jun 19 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2-2mdv2007.0
- spec file attack

* Sun Dec 11 2005 Emmanuel Blindauer <blindauer@mandriva.org> 1.2-1mdk
- First Mandrakelinux release
