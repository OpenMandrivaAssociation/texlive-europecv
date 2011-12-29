# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/europecv
# catalog-date 2006-12-09 23:51:48 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-europecv
Version:	20061209
Release:	1
Summary:	Unofficial class for European curricula vitae
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/europecv
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/europecv.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/europecv.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/europecv/EuropeFlagBW.eps
%{_texmfdistdir}/tex/latex/europecv/EuropeFlagBW.pdf
%{_texmfdistdir}/tex/latex/europecv/EuropeFlagBlueCMYK.eps
%{_texmfdistdir}/tex/latex/europecv/EuropeFlagBlueCMYK.pdf
%{_texmfdistdir}/tex/latex/europecv/EuropeFlagCMYK.eps
%{_texmfdistdir}/tex/latex/europecv/EuropeFlagCMYK.pdf
%{_texmfdistdir}/tex/latex/europecv/EuropeFlagWB.eps
%{_texmfdistdir}/tex/latex/europecv/EuropeFlagWB.pdf
%{_texmfdistdir}/tex/latex/europecv/ecvbg.def
%{_texmfdistdir}/tex/latex/europecv/ecvca.def
%{_texmfdistdir}/tex/latex/europecv/ecvcs.def
%{_texmfdistdir}/tex/latex/europecv/ecvda.def
%{_texmfdistdir}/tex/latex/europecv/ecvde.def
%{_texmfdistdir}/tex/latex/europecv/ecven.def
%{_texmfdistdir}/tex/latex/europecv/ecves.def
%{_texmfdistdir}/tex/latex/europecv/ecvet.def
%{_texmfdistdir}/tex/latex/europecv/ecvfi.def
%{_texmfdistdir}/tex/latex/europecv/ecvfr.def
%{_texmfdistdir}/tex/latex/europecv/ecvgl.def
%{_texmfdistdir}/tex/latex/europecv/ecvgr.def
%{_texmfdistdir}/tex/latex/europecv/ecvhu.def
%{_texmfdistdir}/tex/latex/europecv/ecvis.def
%{_texmfdistdir}/tex/latex/europecv/ecvit.def
%{_texmfdistdir}/tex/latex/europecv/ecvlt.def
%{_texmfdistdir}/tex/latex/europecv/ecvlv.def
%{_texmfdistdir}/tex/latex/europecv/ecvmt.def
%{_texmfdistdir}/tex/latex/europecv/ecvnl.def
%{_texmfdistdir}/tex/latex/europecv/ecvno.def
%{_texmfdistdir}/tex/latex/europecv/ecvpl.def
%{_texmfdistdir}/tex/latex/europecv/ecvpt.def
%{_texmfdistdir}/tex/latex/europecv/ecvro.def
%{_texmfdistdir}/tex/latex/europecv/ecvsk.def
%{_texmfdistdir}/tex/latex/europecv/ecvsl.def
%{_texmfdistdir}/tex/latex/europecv/ecvsr.def
%{_texmfdistdir}/tex/latex/europecv/ecvsv.def
%{_texmfdistdir}/tex/latex/europecv/europasslogo.eps
%{_texmfdistdir}/tex/latex/europecv/europasslogo.pdf
%{_texmfdistdir}/tex/latex/europecv/europecv.cls
%doc %{_texmfdistdir}/doc/latex/europecv/europecv.pdf
%doc %{_texmfdistdir}/doc/latex/europecv/europecv.tex
%doc %{_texmfdistdir}/doc/latex/europecv/examples/at.pdf
%doc %{_texmfdistdir}/doc/latex/europecv/examples/bulgarian-koi8-r.tex
%doc %{_texmfdistdir}/doc/latex/europecv/examples/bulgarian-utf8.tex
%doc %{_texmfdistdir}/doc/latex/europecv/examples/greek-utf8.pdf
%doc %{_texmfdistdir}/doc/latex/europecv/examples/greek-utf8.tex
%doc %{_texmfdistdir}/doc/latex/europecv/examples/maltese-maltese.tex
%doc %{_texmfdistdir}/doc/latex/europecv/examples/maltese-utf8.tex
%doc %{_texmfdistdir}/doc/latex/europecv/examples/minimal.pdf
%doc %{_texmfdistdir}/doc/latex/europecv/examples/minimal.tex
%doc %{_texmfdistdir}/doc/latex/europecv/templates/cv_template_de.pdf
%doc %{_texmfdistdir}/doc/latex/europecv/templates/cv_template_de.tex
%doc %{_texmfdistdir}/doc/latex/europecv/templates/cv_template_en.pdf
%doc %{_texmfdistdir}/doc/latex/europecv/templates/cv_template_en.tex
%doc %{_texmfdistdir}/doc/latex/europecv/templates/cv_template_it.pdf
%doc %{_texmfdistdir}/doc/latex/europecv/templates/cv_template_it.tex
%doc %{_texmfdistdir}/doc/latex/europecv/templates/cv_template_pl.pdf
%doc %{_texmfdistdir}/doc/latex/europecv/templates/cv_template_pl.tex
%doc %{_texmfdistdir}/doc/latex/europecv/templates/publications.bib

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
