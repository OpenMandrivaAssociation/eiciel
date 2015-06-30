Name:		eiciel
Version:	0.9.8.2
Release:	1
Summary:	Graphical access control list (ACL) editor
Group:		Graphical desktop/GNOME
License:	GPL
URL:		http://rofi.roger-ferrer.org/eiciel/
Source0:	http://rofi.roger-ferrer.org/eiciel/download/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	gnome-vfs2-devel
BuildRequires:	nautilus-devel
BuildRequires:	attr-devel
BuildRequires:	acl-devel
BuildRequires:	gettext-devel
BuildRequires:	autoconf2.5
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(gtkmm-3.0)

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
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*%{name}*
%{_datadir}/gnome/help/%{name}
%{_mandir}/man1/%{name}*
%{_libdir}/nautilus/extensions-2.0/lib%{name}*
