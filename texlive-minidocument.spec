Name:		texlive-minidocument
Version:	43752
Release:	2
Summary:	Creates miniature documents inside other LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/minidocument
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minidocument.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minidocument.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minidocument.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package can be used to create miniature documents inside
other LaTeX documents. Inside the minidocument all features of
the outer vertical mode like page breaking, floats, marginpars,
etc. are available.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/minidocument
%{_texmfdistdir}/tex/latex/minidocument
%doc %{_texmfdistdir}/doc/latex/minidocument

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
