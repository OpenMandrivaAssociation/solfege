Summary: 	An ear-training program
Name: 	 	solfege
Version: 	3.23.4
Release: 	1
License:	GPLv3+
Group:		Sound
URL:		https://www.gnu.org/software/solfege/solfege.html
Source0:	http://alpha.gnu.org/gnu/solfege/%{name}-%{version}.tar.gz
Patch1:		solfege-3.20.0-link.patch
Patch2:		solfege-fix-python-version-detection.patch
Patch3:		solfege-3.23.4-usrmove.patch
Patch4:		solfege-3.23.4-py3-webbrowser.patch
Patch5:		solfege-3.23.4-texinfo-non-utf8-input-fix.patch

BuildRequires:	desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:	gettext
BuildRequires:	swig
BuildRequires:	texinfo
BuildRequires:	txt2man
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(python3)
BuildRequires:  python-gobject3
BuildRequires:	python-gi
BuildRequires:	locales-extra-charsets

Requires:	python-gobject3
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
%autopatch -p1

%build
FILE=$(ls %_datadir/sgml/docbook/xsl-stylesheets-1.*/html/chunk.xsl)
%configure \
	--enable-docbook-stylesheet=$FILE

%make_build

%install
%makeinstall

# menu
desktop-file-install --vendor="" \
	--remove-category="Application" \
	--add-category="GTK" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%files -f %{name}.lang
%doc README COPYING AUTHORS FAQ 
%config(noreplace) %{_sysconfdir}/sol*
%{_bindir}/*
%{_libdir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.svg
%{_datadir}/%{name}
%{_mandir}/man1/*

