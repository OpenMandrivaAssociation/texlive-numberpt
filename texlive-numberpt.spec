Name:		texlive-numberpt
Version:	51640
Release:	2
Summary:	Counters spelled out in Portuguese
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/numberpt
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numberpt.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numberpt.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numberpt.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This packages defines commands to display counters spelled out
in Portuguese. The styles are \numberpt for "all lowercase"
\Numberpt for "First word capitalized" \NumberPt for "All
Capitalized" \NUMBERPT for "ALL UPPERCASE" For example,
\renewcommand{\thechapter}{\NumberPt{chapter}} makes chapter
titles to be rendered as "Capitulo Um", "Capitulo Dois" etc.
Options are offered to select variations in the spelling of
"14", or Brazilian vs. European Portuguese forms in the
spelling of "16", "17", and "19". The package requires expl3
and xparse.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/numberpt
%{_texmfdistdir}/tex/latex/numberpt
%doc %{_texmfdistdir}/doc/latex/numberpt

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
