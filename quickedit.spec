Summary:	Simple sound editor for GNOME
Summary(pl):	Prosty edytor d�wi�ku dla GNOME
Name:		quickedit
Version:	0.3
Release:	1
License:	GPL
Group:		X11/Applications/Sound
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

%description -l pl
Quickedit to prosty edytor d�wi�ku dla GNOME, potrafi�cy modyfikowa�
pliki WAV i MP3.

Do odtwarzania plik�w MP3 jest u�ywany zewn�trzny mpg123, pliki WAV s�
odtwarzane bezpo�rednio. Do zapisu plik�w MP3 jest u�ywany koder lame,
do konwersji d�wi�ku sox. Quickedit jest napisany w C++ z u�yciem
gtkmm, gnomemm i libsigc++.

%prep
%setup -q

%build
%{__gettextize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT/*

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
