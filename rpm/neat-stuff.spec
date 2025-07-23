Name: neat-stuff
Version: 1.2.4
Release: 1
Summary: NEAT Stuff
Group: Applications/Internet
License: GPL-3.0-or-later
URL: https://www.neat-project.org/
Source: https://packages.nntb.no/software/%{name}/%{name}-%{version}.tar.xz

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
Requires: bash-completion
Requires: bridge-utils
Requires: btrfs-progs
Requires: bc
Requires: bwm-ng
Requires: colordiff
Requires: cronie
Requires: ethtool
Requires: git
Requires: gpm
Requires: hping3
Requires: htop
Requires: joe
Requires: jq
Requires: libidn
Requires: lksctp-tools
Requires: (mlocate or plocate)
Requires: net-snmp-utils
Requires: net-tools
Requires: nmap
Requires: (ntpsec or ntpdate)
Requires: pxz
Requires: reprepro
Requires: smartmontools
Requires: subnetcalc
Requires: tcpdump
Requires: tftp
Requires: traceroute
Requires: tree
Requires: vconfig
Requires: virt-what
Requires: whois
Recommends: grub2-tools
Recommends: ipsec-tools
Recommends: netperfmeter
Recommends: libneat-examples,
Recommends: libneat-socketapi-examples,
Recommends: reiserfs-utils
Recommends: rsplib-docs
Recommends: rsplib-services
Recommends: rsplib-tools
Recommends: wireshark-cli

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
Requires: banner
Requires: bison
Requires: bzip2-devel
Requires: clang
Requires: cmake
Requires: (createrepo_c or createrepo)
Requires: debhelper
Requires: dejavu-sans-fonts
Requires: dejavu-sans-mono-fonts
Requires: dejavu-serif-fonts
Requires: devscripts
Requires: flex
Requires: gcc
Requires: gcc-c++
Requires: gdb
Requires: ghostscript
Requires: gimp
Requires: glib2-devel
Requires: gnupg
Requires: google-noto-cjk-fonts
Requires: google-noto-sans-fonts
Requires: google-noto-serif-fonts
Requires: GraphicsMagick
Requires: jansson-devel
Requires: ldns-devel
Requires: libcurl-devel
Requires: libmnl-devel
Requires: libpcap-devel
Requires: libtool
Requires: libuv-devel
Requires: lksctp-tools-devel
Requires: make
Requires: mock
Requires: openssl-devel
Requires: openssl-devel-engine
Requires: pbuilder
Requires: perl-Image-ExifTool
Requires: python3-devel
Requires: qt6-qtbase-devel
Requires: quilt
Requires: R-base
Requires: rpm
Requires: swig
Requires: texlive-epstopdf-bin
Requires: urw-base35-fonts
Requires: valgrind
Recommends: libneat-devel
Recommends: libneat-docs
Recommends: libneat-socketapi-devel
Recommends: rsplib-devel


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
