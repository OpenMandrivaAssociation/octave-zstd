%global octpkg octave_zstd

Summary:	The octave_zstd package provides functions for compress and decompress about ZS
Name:		octave-octave_zstd
Version:	1.1.0
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/octave_zstd/
Url:		https://github.com/CNOCTAVE/octave_zstd
Source0:	https://github.com/CNOCTAVE/octave_zstd/releases/download/%{version}/octave_zstd.tar.gz

BuildRequires:	octave-devel >= 8.0.0
BuildRequires:	octave-tar >= 1.0.1
BuildRequires:	pkgconfig(libzstd)

Requires:	octave(api) = %{octave_api}
Requires:	octave-tar >= 1.0.1

Requires(post): octave
Requires(postun): octave

%description
The octave_zstd package provides functions for compress and 
decompress about ZSTD format.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}

rm -f PKG_ADD

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

