%define	name	eiciel
%define	version	0.9.6.1
%define	release	%mkrel 2

Name:		%name
Version:	%version
Release:	%release
Summary:	Graphical access control list (ACL) editor
Group:		Graphical desktop/GNOME
License:	GPL
URL:		http://rofi.roger-ferrer.org/eiciel/
Source0:	http://rofi.roger-ferrer.org/eiciel/download/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	libgnomeui2-devel gtkmm2.4-devel gnome-vfs2-devel nautilus-devel
BuildRequires:	libattr-devel libacl-devel gettext-devel
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
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*%{name}*
%{_datadir}/gnome/help/%{name}
%{_mandir}/man1/%{name}*
%{_libdir}/nautilus/extensions-2.0/lib%{name}*
%exclude %{_libdir}/nautilus/extensions-2.0/*.a
%exclude %{_libdir}/nautilus/extensions-2.0/*.la


