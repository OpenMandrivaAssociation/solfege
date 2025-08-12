Summary: 	An ear-training program
Name: 	 	solfege
Version: 	3.23.4
Release: 	2
License:	GPLv3+
Group:		Sound
Url:		https://www.gnu.org/software/solfege/solfege.html
Source0:	http://alpha.gnu.org/gnu/solfege/%{name}-%{version}.tar.gz
Patch1:		solfege-3.20.0-link.patch
Patch2:		solfege-fix-python-version-detection.patch
Patch3:		solfege-3.23.4-usrmove.patch
Patch4:		solfege-3.23.4-py3-webbrowser.patch
Patch5:		solfege-3.23.4-texinfo-non-utf8-input-fix.patch
Patch6:		solfege-3.23.4-fix-invalid-python-escape-sequences.patch
Patch7:		solfege-3.23.4-dont-decode-strings.patch
Patch8:		solfege-3.23.4-fix-mpd-engravers.patch
BuildRequires:	desktop-file-utils
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext
BuildRequires:	locales-extra-charsets
BuildRequires:	swig
BuildRequires:	texinfo
BuildRequires:	txt2man
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(python3)
BuildRequires:python-gobject3
BuildRequires:	python-gi
Requires:	python-gobject3
Requires:	swig
Requires:	TiMidity++

%description
GNU Solfege is an ear-training program. These are the exercises written so far:
* Recognise melodic and harmonic intervals.
* Compare interval sizes.
* Sing the intervals the computer asks for.
* Identify chords.
* Sing chords.
* Scales.
* Dictation.
* Remembering rhythmic patterns.

%files -f %{name}.lang
%doc README COPYING AUTHORS FAQ 
%config(noreplace) %{_sysconfdir}/%{name}
%{_bindir}/%{name}
%{_libdir}/%{name}/*.so
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
FILE=$(ls %_datadir/sgml/docbook/xsl-stylesheets-1.*/html/chunk.xsl)
%configure --enable-docbook-stylesheet=$FILE

%make_build


%install
%make_install

# Fix .desktop file
desktop-file-edit \
	--remove-category="Application" \
	--add-category="GTK" \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

# Fix perms
chmod +x %{buildroot}%{_datadir}/%{name}/%{name}/parsetree.py
chmod +x %{buildroot}%{_datadir}/%{name}/%{name}/presetup.py

%find_lang %{name}
