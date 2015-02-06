%define	name	eiciel
%define	version	0.9.6.1
%define release	3

Name:		%name
Version:	%version
Release:	%release
Summary:	Graphical access control list (ACL) editor
Group:		Graphical desktop/GNOME
License:	GPL
URL:		http://rofi.roger-ferrer.org/eiciel/
Source0:	http://rofi.roger-ferrer.org/eiciel/download/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libgnomeui-2.0) gtkmm2.4-devel gnome-vfs2-devel nautilus-devel
BuildRequires:	attr-devel acl-devel gettext-devel
BuildRequires:	autoconf2.5
BuildRequires:	desktop-file-utils

%description
Graphical editor for access control lists (ACL) 
and extended attributes (XATTR), either as an 
extension within Nautilus, or as a standalone utility.

%prep
%setup -q
sed -i s/Version=.*/Version=1.0/ src/*.desktop.in

%build
#autoreconf -fi
%configure2_5x --with-nautilus-extensions-dir=%{_libdir}/nautilus/extensions-2.0
%make

%install
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*%{name}*
%{_datadir}/gnome/help/%{name}
%{_mandir}/man1/%{name}*
%{_libdir}/nautilus/extensions-2.0/lib%{name}*


%changelog
* Fri Feb 19 2010 Funda Wang <fwang@mandriva.org> 0.9.6.1-1mdv2010.1
+ Revision: 508307
- new version 0.9.6.1

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - rebuild

* Wed Jan 23 2008 Götz Waschk <waschk@mandriva.org> 0.9.5.1-3mdv2008.1
+ Revision: 157111
- fix nautilus extensions dir

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 17 2007 Funda Wang <fwang@mandriva.org> 0.9.5.1-2mdv2008.1
+ Revision: 109288
- rebuild for new lzma

* Wed Oct 31 2007 Pascal Terjan <pterjan@mandriva.org> 0.9.5.1-1mdv2008.1
+ Revision: 104231
- Fix desktop file
- 0.9.5.1


* Thu Nov 16 2006 Pascal Terjan <pterjan@mandriva.org> 0.9.4-1mdv2007.0
+ Revision: 84902
- 0.9.4
- Import eiciel

* Thu Sep 14 2006 Emmanuel Andry <eandry@mandriva.org> 0.9.2-4mdv2007.0
- reenable // build on cluster
- add buildrequires gettext-devel

* Mon Sep 11 2006 Emmanuel Andry <eandry@mandriva.org> 0.9.2-3mdv2007.0
- disable // build on cluster

* Fri Aug 04 2006 Frederic Crozat <fcrozat@mandriva.com> 0.9.2-2mdv2007.0
- Rebuild with latest dbus

* Sat Jul 15 2006 Pascal Terjan <pterjan@mandriva.org> 0.9.2-1mdv2007.0
- First Mandriva package

