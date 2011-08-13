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
