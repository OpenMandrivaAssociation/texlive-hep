# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/hep
# catalog-date 2008-08-21 09:38:31 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-hep
Version:	1.0
Release:	1
Summary:	A "convenience wrapper" for High Energy Physics packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hep
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
