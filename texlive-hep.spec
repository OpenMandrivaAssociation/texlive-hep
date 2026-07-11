%global tl_name hep
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	A convenience wrapper for High Energy Physics packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hep
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hep.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hep.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Loads the author's hepunits and hepnicenames packages, and a selection
of others that are useful in High Energy Physics papers, etc.

