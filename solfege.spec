%define name	solfege
%define version 3.20.1
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	An ear-training program
Version: 	%{version}
Release: 	%{release}
Source:		http://download.sourceforge.net/solfege/%{name}-%{version}.tar.gz
Source1: 	%{name}48.png
Source2: 	%{name}32.png
Source3: 	%{name}16.png
Patch1:		solfege-3.20.0-link.patch
URL:		http://www.solfege.org/
License:	GPLv3+
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	swig python-devel
BuildRequires:	txt2man
BuildRequires:	pkgconfig gettext texinfo
BuildRequires:  gnome-python
BuildRequires:  docbook-style-xsl libxslt-proc
BuildRequires:  pygtk2.0-devel desktop-file-utils
Requires:	pygtk2.0 swig
Requires:	gnome-python gnome-python-gtkhtml2 gnome-python-gnomevfs
Requires:	TiMidity++

%description
GNU Solfege is an ear-training program. These are the exercises written so far:
    * Recognise melodic and harmonic intervals
    * Compare interval sizes
    * Sing the intervals the computer asks for
    * Identify chords
    * Sing chords
    * Scales
    * Dictation
    * Remembering rhythmic patterns

%prep
%setup -q
%patch1 -p0

%build
FILE=$(ls %_datadir/sgml/docbook/xsl-stylesheets-1.*/html/chunk.xsl)
%configure2_5x --enable-docbook-stylesheet=$FILE
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# menu

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

# icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
cat %SOURCE1 > $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
cat %SOURCE2 > $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
cat %SOURCE3 > $RPM_BUILD_ROOT/%_miconsdir/%name.png

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %name.lang
%defattr(-,root root)
%doc README COPYING AUTHORS ChangeLog FAQ 
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/sol*
%{_mandir}/man1/*
%{_libdir}/%name
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.svg
%{_datadir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png


%changelog
* Sat Aug 13 2011 Funda Wang <fwang@mandriva.org> 3.20.1-1mdv2012.0
+ Revision: 694380
- new version 3.20.1

* Sun Jun 19 2011 Funda Wang <fwang@mandriva.org> 3.20.0-1
+ Revision: 686004
- rediff patch
- update to new version 3.20.0

* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 3.19.5-1
+ Revision: 645427
- update to new version 3.19.5

* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 3.18.6-2mdv2011.0
+ Revision: 590081
- rebuild for python 2.7

* Mon Oct 25 2010 Funda Wang <fwang@mandriva.org> 3.18.6-1mdv2011.0
+ Revision: 589247
- new version 3.18.6

* Mon Oct 25 2010 Funda Wang <fwang@mandriva.org> 3.18.5-1mdv2011.0
+ Revision: 589224
- update to new version 3.18.5
- fix desktop file categories

* Thu Oct 14 2010 Funda Wang <fwang@mandriva.org> 3.18.4-1mdv2011.0
+ Revision: 585525
- New version 3.18.4

* Sun Aug 29 2010 Funda Wang <fwang@mandriva.org> 3.16.4-1mdv2011.0
+ Revision: 574073
- update to new version 3.16.4

* Fri Apr 23 2010 Funda Wang <fwang@mandriva.org> 3.16.1-1mdv2010.1
+ Revision: 538052
- new version 3.16.1

* Thu Apr 01 2010 Funda Wang <fwang@mandriva.org> 3.16.0-1mdv2010.1
+ Revision: 530612
- update to new version 3.16.0

* Wed Mar 10 2010 Sandro Cazzaniga <kharec@mandriva.org> 3.15.8-2mdv2010.1
+ Revision: 517487
- Drop patch applied upstream (thanks misc)

* Wed Mar 10 2010 Sandro Cazzaniga <kharec@mandriva.org> 3.15.8-1mdv2010.1
+ Revision: 517275
- update to 3.15.8
- stop use patch1 because it breaks build but keep it.

* Wed Feb 10 2010 Frederik Himpe <fhimpe@mandriva.org> 3.14.11-1mdv2010.1
+ Revision: 503968
- update to new version 3.14.11

* Sun Dec 27 2009 Funda Wang <fwang@mandriva.org> 3.14.10-1mdv2010.1
+ Revision: 482670
- new version 3.14.10

* Wed Nov 11 2009 Funda Wang <fwang@mandriva.org> 3.14.9-1mdv2010.1
+ Revision: 464573
- new version 3.14.9

* Wed Sep 30 2009 Frederik Himpe <fhimpe@mandriva.org> 3.14.8-1mdv2010.0
+ Revision: 451841
- update to new version 3.14.8

* Wed Aug 19 2009 Frederik Himpe <fhimpe@mandriva.org> 3.14.7-1mdv2010.0
+ Revision: 417892
- update to new version 3.14.7

* Sat Aug 08 2009 Frederik Himpe <fhimpe@mandriva.org> 3.14.6-1mdv2010.0
+ Revision: 411513
- update to new version 3.14.6

* Mon Jun 29 2009 Funda Wang <fwang@mandriva.org> 3.14.5-1mdv2010.0
+ Revision: 390499
- New version 3.14.5

* Tue Jun 09 2009 Funda Wang <fwang@mandriva.org> 3.14.4-1mdv2010.0
+ Revision: 384464
- New version 3.14.4

* Tue Jun 09 2009 Funda Wang <fwang@mandriva.org> 3.14.3-2mdv2010.0
+ Revision: 384428
- use timidity as midi player by default, as most sound cards do not contain hard wavetable

* Tue Jun 02 2009 Funda Wang <fwang@mandriva.org> 3.14.3-1mdv2010.0
+ Revision: 382084
- New version 3.14.3

* Mon Jan 19 2009 Funda Wang <fwang@mandriva.org> 3.12.1-1mdv2009.1
+ Revision: 331082
- new version 3.12.1

* Mon Dec 01 2008 Funda Wang <fwang@mandriva.org> 3.12.0-1mdv2009.1
+ Revision: 308738
- fix BR and license
- New version 3.12.0

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 3.10.4-3mdv2009.0
+ Revision: 269341
- rebuild early 2009.0 package (before pixel changes)
- swig-devel doesn't exist

  + Austin Acton <austin@mandriva.org>
    - requires TiMidity++ (Maxim Heijndijk)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jun 11 2008 Austin Acton <austin@mandriva.org> 3.10.4-1mdv2009.0
+ Revision: 217844
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Dec 14 2007 Thierry Vignaud <tv@mandriva.org> 3.6.5-2mdv2008.1
+ Revision: 119925
- patch 0: fix desktop entry so that desktop-file-install doesn't delete it
- rebuild b/c of missing subpackage on ia32

* Sat Apr 21 2007 Pascal Terjan <pterjan@mandriva.org> 3.6.5-1mdv2008.0
+ Revision: 16598
- 3.6.5
- BuildRequires libxslt-proc


* Tue Sep 12 2006 Emmanuel Andry <eandry@mandriva.org> 3.0.6-3mdv2007.0
- add buildrequires desktop-file-utils

* Tue Sep 12 2006 Emmanuel Andry <eandry@mandriva.org> 3.0.6-2mdv2007.0
- fix requires
- xdg menu

* Wed May 03 2006 Emmanuel Andry <eandry@free.fr> 3.0.6-1mdk
- 3.0.6
- removed pygtk-devel as it now use pygtk2.0-devel
- removed pygnome-devel because not available anymore

* Wed Oct 19 2005 Nicolas L�cureuil <neoclust@mandriva.org> 2.9.1-2mdk
- Fix BuildRequires
- %%mkrel

* Thu Jun 16 2005 Lenny Cartier <lenny@mandriva.com> 2.9.1-1mdk
- 2.9.1

* Mon Sep 13 2004 Austin Acton <austin@mandriva.org> 2.4.0-1mdk
- 2.4.0
- requires gnome-python-gnomevfs (Simon Oplatka Wenger)
- configure 2.5
- fudge date since nobody wants to fix it (s/b Thu May 26 2005)

* Mon Sep 13 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.0.6-1mdk
- 2.0.6

* Thu Jun 10 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.0.5-1mdk
- 2.0.5

* Sun May 16 2004 Michael Scherer <misc@mandrake.org> 2.0.4-2mdk 
- add Requires
- xsl stylesheet autodetection

* Sun Feb 29 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.0.4-1mdk
- 2.0.4
- Own dir

