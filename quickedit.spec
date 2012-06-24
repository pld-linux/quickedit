Summary:	Simple sound editor for GNOME
Name:		quickedit
Version:	0.3
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://www.penguin.cz/~slezak/%{name}-%{version}.tar.gz
URL:		http://www.penguin.cz/~slezak/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Quickedit is simple sound editor for GNOME, which can edit WAV and MP3
files.

For playing MP3 files is used external decoder mpg123, WAV files are
played directly. For exporting to MP3 file is used lame encoder, for
sound conversions sox utility. Quickedit is written in C++ and
requires C++ wrappers gtkmm and gnomemm, for signal system is used
libsigc++.

%prep
%setup -q

%build
gettextize --copy --force
aclocal -I macros
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README AUTHORS ChangeLog TODO

%clean
rm -rf $RPM_BUILD_ROOT/*

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
