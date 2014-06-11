Summary: 	An ear-training program
Name: 	 	solfege
Version: 	3.22.2
Release: 	2
License:	GPLv3+
Group:		Sound
URL:		http://www.solfege.org/
Source0:	http://ftp.gnu.org/gnu/solfege/%{name}-%{version}.tar.gz
Patch1:		solfege-3.20.0-link.patch

BuildRequires:	desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:	gettext
BuildRequires:	swig
BuildRequires:	texinfo
BuildRequires:	txt2man
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(python)
BuildRequires:  pkgconfig(pygtk-2.0)

Requires:	pygtk2.0
Requires:	swig
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
%apply_patches

%build
FILE=$(ls %_datadir/sgml/docbook/xsl-stylesheets-1.*/html/chunk.xsl)
%configure2_5x \
	--enable-docbook-stylesheet=$FILE

%make

%install
%makeinstall_std

# menu
desktop-file-install --vendor="" \
	--remove-category="Application" \
	--add-category="GTK" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%files -f %{name}.lang
%doc README COPYING AUTHORS ChangeLog FAQ 
%config(noreplace) %{_sysconfdir}/sol*
%{_bindir}/*
%{_libdir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.svg
%{_datadir}/%{name}
%{_mandir}/man1/*

