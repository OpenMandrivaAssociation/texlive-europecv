%global tl_name europecv
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Unofficial class for European curricula vitae
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/europecv
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/europecv.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/europecv.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The europecv class is an unofficial LaTeX implementation of the standard
model for curricula vitae (the "Europass CV") as recommended by the
European Commission. Although primarily intended for users in the
European Union, the class is flexible enough to be used for any kind of
curriculum vitae. The class has localisations for all the official
languages of the EU (plus Catalan), as well as options permitting input
in UTF-8 and koi8-r.

