Name:		texlive-europecv
Version:	64037
Release:	1
Summary:	Unofficial class for European curricula vitae
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/europecv
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/europecv.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/europecv.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The europecv class is an unofficial LaTeX implementation of the
standard model for curricula vitae (the "Europass CV") as
recommended by the European Commission. Although primarily
intended for users in the European Union, the class is flexible
enough to be used for any kind of curriculum vitae. The class
has localisations for all the official languages of the EU
(plus Catalan), as well as options permitting input in UTF-8
and koi8-r.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/europecv
%doc %{_texmfdistdir}/doc/latex/europecv

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
