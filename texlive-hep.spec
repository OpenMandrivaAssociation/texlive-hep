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
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Loads the author's hepunits and hepnicenames packages, and a
selection of others that are useful in High Energy Physics
papers, etc.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
