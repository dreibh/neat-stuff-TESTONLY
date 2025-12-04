Name: neat-stuff
Version: 1.2.5~rc1.2
Release: 1
Summary: NEAT Stuff
Group: Applications/Internet
License: GPL-3.0-or-later
URL: https://www.neat-project.org/
Source: https://packages.nntb.no/software/%{name}/%{name}-%{version}.tar.xz

# FIXME: S390x does not provide the dependency Gimp 3.x, yet.
#        Once this is fixed, the architecture exclusion can be removed:
ExcludeArch: s390x

AutoReqProv: on
BuildRequires: cmake
BuildRequires: dejavu-sans-fonts
BuildRequires: dejavu-sans-mono-fonts
BuildRequires: dejavu-serif-fonts
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: ghostscript
BuildRequires: gimp
BuildRequires: google-noto-cjk-fonts
BuildRequires: google-noto-sans-fonts
BuildRequires: google-noto-serif-fonts
BuildRequires: GraphicsMagick
BuildRequires: perl-Image-ExifTool
BuildRequires: texlive-epstopdf-bin
BuildRequires: urw-base35-fonts
BuildRoot: %{_tmppath}/%{name}-%{version}-build

BuildArch: noarch

# TEST ONLY:
%define _unpackaged_files_terminate_build 0


%description
This metapackage contains basic software for NEAT system management.
The software installed provides a common working environment.
See https://www.neat-project.org for details on NEAT!

%prep
%setup -q

%build
# NOTE: CMAKE_VERBOSE_MAKEFILE=OFF for reduced log output!
%cmake -DCMAKE_INSTALL_PREFIX=/usr -DPYTHON_LIBRARY_PREFIX=%{buildroot}/usr -DFLAT_DIRECTORY_STRUCTURE=1 -DBUILD_BOOTSPLASH=1 -DCMAKE_VERBOSE_MAKEFILE=OFF .
%cmake_build

%install
%cmake_install
# ====== Relocate files =====================================================
mkdir -p %{buildroot}/boot/NEAT
mv %{buildroot}/usr/share/neat-desktop/splash/NEATManagement1-*.jpeg  %{buildroot}/boot/NEAT
mv %{buildroot}/usr/share/neat-desktop/splash/NEATDevelopment1-*.jpeg %{buildroot}/boot/NEAT
mv %{buildroot}/usr/share/neat-desktop/splash/NEATDesktop1-*.jpeg     %{buildroot}/boot/NEAT
mkdir -p %{buildroot}/etc/neat
mv %{buildroot}/usr/share/neat-desktop/splash/neat-stuff-version %{buildroot}/etc/neat
# ===========================================================================


%package management
Summary: Management tools for the NEAT system environment
Group: Applications/Internet
BuildArch: noarch
Requires: acl
Requires: bash
Requires: bash-completion
Requires: bind-utils
Requires: bridge-utils
Requires: bwm-ng
Requires: bzip2
Requires: chrpath
Requires: cloud-utils-growpart
Requires: cmake
Requires: curl
Requires: dnf-automatic
Requires: ethtool
Requires: fail2ban
Requires: gdisk
Requires: git
Requires: gpg
Requires: gpm
Requires: hipercontracer
Requires: htop
Requires: iproute
Requires: iproute-tc
Requires: iptables
Requires: iputils
Requires: joe
Requires: jq
Requires: kernel-modules-extra
Requires: libidn
Requires: make
Requires: man
Requires: netperfmeter
Requires: netplan
Requires: net-tools
Requires: nmap
Requires: openssh-server
Requires: openssl
Requires: parallel
Requires: plocate
Requires: pwgen
Requires: python3
Requires: rsplib-tools
Requires: rsync
Requires: subnetcalc
Requires: sudo
Requires: tar
Requires: tcpdump
Requires: td-system-tools
Requires: td-system-tools-configure-grub
Requires: traceroute
Requires: tree
Requires: tsctp
Requires: unzip
Requires: uuid
Requires: virt-what
Requires: wget
Requires: wireshark-cli
Requires: zip
Recommends: grub2-tools

%description management
This metapackage contains basic software for NEAT system management.
The software installed provides a common working environment.
See https://www.neat-project.org for details on NEAT!

%files management
/boot/NEAT/NEATManagement1-*.jpeg
%{_sysconfdir}/grub.d/??_neat_management_theme
%{_sysconfdir}/neat/neat-stuff-version
%{_datadir}/neat-stuff/grub-defaults
%{_sysconfdir}/system-info.d/18-neat
%{_sysconfdir}/system-maintenance.d/18-neat

%post management
if [ -e /usr/sbin/grub2-mkconfig ] ; then /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg || true ; fi

%postun management
rm -f /etc/grub.d/??_neat_desktop_theme
if [ -e /usr/sbin/grub2-mkconfig ] ; then /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg || true ; fi


%package development
Summary: Development tools for the NEAT system environment
Group: Applications/Internet
BuildArch: noarch
Requires: autoconf
Requires: automake
Requires: bc
Requires: bison
Requires: boost-devel
Requires: bzip2-devel
Requires: c-ares-devel
Requires: clang
Requires: cmake
Requires: dejavu-fonts-all
Requires: extra-cmake-modules
Requires: flex
Requires: g++
Requires: gcc
Requires: gdb
Requires: GeoIP-devel
Requires: ghostscript
Requires: git-lfs
Requires: google-noto-fonts-all
Requires: GraphicsMagick
Requires: libcurl-devel
Requires: libtool
Requires: lksctp-tools-devel
Requires: mock
Requires: open-sans-fonts
Requires: openssl-devel
Requires: pbuilder
Requires: pdf2svg
Requires: perl-Image-ExifTool
Requires: pkg-config
Requires: python3
Requires: python3-netifaces
Requires: python3-pip
Requires: python3-setuptools
Requires: qt6-linguist
Requires: qt6-qtbase-devel
Requires: R-base
Requires: reprepro
Requires: rpm-build
Requires: rsplib-libcpprspserver-devel
Requires: rsplib-librsplib-devel
Requires: shellcheck
Requires: tidy
Requires: urw-base35-fonts
Requires: xz-devel
Requires: zlib-devel
Requires: jansson-devel
Requires: ldns-devel
Requires: libmnl-devel
Requires: libuv-devel
Requires: lksctp-tools-devel
Requires: openssl-devel
Requires: openssl-devel-engine
Requires: python3-devel
Requires: swig
Recommends: valgrind
Recommends: yamllint


%description development
This metapackage contains basic software for NEAT development.
The software installed provides a common working environment.
See https://www.neat-project.org for details on NEAT!

%files development
/boot/NEAT/NEATDevelopment1-*.jpeg
%{_sysconfdir}/grub.d/??_neat_development_theme

%post development
if [ -e /usr/sbin/grub2-mkconfig ] ; then /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg || true ; fi

%postun development
rm -f /etc/grub.d/??_neat_desktop_theme
if [ -e /usr/sbin/grub2-mkconfig ] ; then /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg || true ; fi


%package desktop
Summary: Desktop setup for the NEAT system environment
Group: Applications/Internet
BuildArch: noarch
Requires: %{name}-management = %{version}-%{release}
Recommends: xorg-x11-drv-vmware

%description desktop
This metapackage contains the scripts to configure a NEAT desktop.
See https://www.neat-project.org for details on NEAT!

%files desktop
/boot/NEAT/NEATDesktop1-*.jpeg
%{_sysconfdir}/grub.d/??_neat_desktop_theme
%{_datadir}/neat-desktop/background/*
%{_datadir}/neat-desktop/desktop/*
%{_datadir}/neat-desktop/NEAT-A4.pdf
%ghost %{_datadir}/neat-desktop/splash

%post desktop
if [ -e /usr/sbin/grub2-mkconfig ] ; then /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg || true ; fi

%postun desktop
rm -f /etc/grub.d/??_neat_desktop_theme
if [ -e /usr/sbin/grub2-mkconfig ] ; then /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg || true ; fi


%changelog
* Wed Jul 23 2025 Thomas Dreibholz <thomas.dreibholz@gmail.com> - 1.2.4-1
- New upstream release.
* Fri Jul 11 2025 Thomas Dreibholz <thomas.dreibholz@gmail.com> - 1.2.3-1
- New upstream release.
* Thu Jul 10 2025 Thomas Dreibholz <thomas.dreibholz@gmail.com> - 1.2.2
- New upstream release.
* Sat Dec 14 2024 Thomas Dreibholz <thomas.dreibholz@gmail.com> - 1.2.1
- New upstream release.
* Sat Dec 14 2024 Thomas Dreibholz <thomas.dreibholz@gmail.com> - 1.2.0
- New upstream release.
* Tue Dec 19 2023 Thomas Dreibholz <thomas.dreibholz@gmail.com> - 1.1.10
- New upstream release.
* Wed Dec 06 2023 Thomas Dreibholz <thomas.dreibholz@gmail.com> - 1.1.9
- New upstream release.
* Wed Feb 08 2023 Thomas Dreibholz <thomas.dreibholz@gmail.com> - 1.1.8
- New upstream release.
* Sun Sep 11 2022 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.7
- New upstream release.
* Wed Feb 16 2022 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.6
- New upstream release.
* Mon Feb 14 2022 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.5
- New upstream release.
* Mon Jun 14 2021 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.4
- New upstream release.
* Wed Dec 16 2020 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.3
- New upstream release.
* Sun Nov 15 2020 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.2
- New upstream release.
* Fri Oct 09 2020 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.1
- New upstream release.
* Tue Oct 06 2020 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.0
- New upstream release.
* Tue May 05 2020 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.0.3
- New upstream release.
* Fri Apr 24 2020 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.0.2
- New upstream release.
* Tue Jan 21 2020 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.0.1
- New upstream release.
* Mon Jan 20 2020 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.0.0
- New upstream release.
* Thu Nov 07 2019 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.9.4
- New upstream release.
* Fri Sep 20 2019 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.9.3
- New upstream release.
* Thu Aug 22 2019 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.9.2
- New upstream release.
* Wed Aug 07 2019 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.9.1
- New upstream release.
* Mon Aug 05 2019 Thomas Dreibholz <dreibh@simula.no> - 0.9.0
- New upstream release.
* Fri Jul 05 2019 Thomas Dreibholz <dreibh@simula.no> - 0.8.5
- New upstream release.
* Wed Jul 03 2019 Thomas Dreibholz <dreibh@simula.no> - 0.8.4
- New upstream release.
* Mon Jun 17 2019 Thomas Dreibholz <dreibh@simula.no> - 0.8.3
- New upstream release.
* Wed May 15 2019 Thomas Dreibholz <dreibh@simula.no> - 0.8.2
- New upstream release.
* Wed Mar 06 2019 Thomas Dreibholz <dreibh@simula.no> - 0.8.1
- New upstream release.
* Fri Nov 16 2018 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.0.0
- Created RPM package.
