%define name	solfege
%define version 3.0.6
%define release %mkrel 3

Name: 	 	%{name}
Summary: 	An ear-training program
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/solfege/%{name}-%{version}.tar.bz2
Source1: 	%{name}48.png
Source2: 	%{name}32.png
Source3: 	%{name}16.png
URL:		http://solfege.sourceforge.net
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	swig-devel python-devel
BuildRequires:	pkgconfig gettext texinfo
BuildRequires:  gnome-python
BuildRequires:  docbook-style-xsl
BuildRequires:  pygtk2.0-devel desktop-file-utils
Requires:	pygtk2.0 swig
Requires:	gnome-python gnome-python-gtkhtml2 gnome-python-gnomevfs

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

%build
FILE=$(ls %_datadir/sgml/docbook/xsl-stylesheets-1.*/html/chunk.xsl)
%configure2_5x --enable-docbook-stylesheet=$FILE
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

# menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="Solfege" longtitle="Ear Training" section="Multimedia/Sound" xdg="true"
EOF

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="AudioVideo;Audio" \
  --add-category="X-MandrivaLinux-Multimedia-Sound" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

# icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
cat %SOURCE1 > $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
cat %SOURCE2 > $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
cat %SOURCE3 > $RPM_BUILD_ROOT/%_miconsdir/%name.png

%find_lang %name
%find_lang %name-intervallnames
cat %name-intervallnames.lang >> %name.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files -f %name.lang
%defattr(-,root,root)
%doc README COPYING AUTHORS ChangeLog FAQ 
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/sol*
%{_mandir}/man1/*
%{_menudir}/%name
%{_libdir}/%name
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_datadir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

