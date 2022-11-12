Name:		texlive-hep
Version:	15878
Release:	1
Summary:	A "convenience wrapper" for High Energy Physics packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hep
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Loads the author's hepunits and hepnicenames packages, and a
selection of others that are useful in High Energy Physics
papers, etc.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/hep/hep.sty
%doc %{_texmfdistdir}/doc/latex/hep/ChangeLog
%doc %{_texmfdistdir}/doc/latex/hep/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
