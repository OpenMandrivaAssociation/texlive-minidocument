%global tl_name minidocument
%global tl_revision 43752

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Creates miniature documents inside other LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/minidocument
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/minidocument.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/minidocument.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/minidocument.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package can be used to create miniature documents inside other
LaTeX documents. Inside the minidocument all features of the outer
vertical mode like page breaking, floats, marginpars, etc. are
available.

