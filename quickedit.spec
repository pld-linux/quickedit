Name:      @PACKAGE@
Version:   @VERSION@
Release:   1
Summary:   Simple sound editor for GNOME
Copyright: GPL
Url:       http://www.penguin.cz/~slezak
Packager:  Ladislav Slezák <slezak@penguin.cz>
Group:     Applications/Multimedia
Source:    @PACKAGE@-@VERSION@.tar.gz
BuildRoot: %{_tmppath}/buildroot-@PACKAGE@-@VERSION@

%description
Quickedit is simple sound editor for GNOME, which can edit WAV and MP3 files.

For playing MP3 files is used external decoder mpg123, WAV files are
played directly. For exporting to MP3 file is used lame encoder, for
sound conversions sox utility. Quickedit is written in C++ and requires
C++ wrappers gtkmm and gnomemm, for signal system is used libsigc++.

Quickedit is released under GNU General Public Licence.
	        
%prep

%setup 
./configure --prefix=@prefix@

%build
make

%install
make install-strip prefix=$RPM_BUILD_ROOT@prefix@

%clean
rm -rf $RPM_BUILD_ROOT/*

%files
%defattr(-, root, root)
%doc README COPYING AUTHORS ChangeLog TODO
@prefix@/*
