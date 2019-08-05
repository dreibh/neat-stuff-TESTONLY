Name: neat-stuff
Version: 0.9.0
Release: 1
Summary: NEAT Control
Group: Applications/Internet
License: GPLv3
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


# This package does not generate debug information (no executables):
%global debug_package %{nil}

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
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
# ====== Relocate files =====================================================
mkdir -p %{buildroot}/boot/NEAT
mv %{buildroot}/usr/share/neat-desktop/splash/NEATManagement1-1024x768.jpeg  %{buildroot}/boot/NEAT
mv %{buildroot}/usr/share/neat-desktop/splash/NEATDevelopment1-1024x768.jpeg %{buildroot}/boot/NEAT
mv %{buildroot}/usr/share/neat-desktop/splash/NEATDesktop1-1024x768.jpeg     %{buildroot}/boot/NEAT
mkdir -p %{buildroot}/etc/neat
mv %{buildroot}/usr/share/neat-desktop/splash/neat-stuff-version %{buildroot}/etc/neat
# ===========================================================================


%package management
Summary: NEAT Management
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
Requires: ipsec-tools
Requires: joe
Requires: jq
Requires: libidn
Requires: lksctp-tools
Requires: mlocate
Requires: net-snmp-utils
Requires: net-tools
Requires: nmap
Requires: ntpdate
Requires: pxz
Requires: reiserfs-utils
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
Recommends: netperfmeter
Recommends: libneat-examples,
Recommends: libneat-socketapi-examples,
Recommends: rsplib-docs
Recommends: rsplib-services
Recommends: rsplib-tools
Recommends: wireshark-cli

%description management
This metapackage contains basic software for NEAT system management.
The software installed provides a common working environment.
See https://www.neat-project.org for details on NEAT!

%files management
/boot/NEAT/NEATManagement1-1024x768.jpeg
%{_sysconfdir}/grub.d/??_neat_management_theme
%{_sysconfdir}/neat/neat-stuff-version
%{_datadir}/neat-stuff/grub-defaults

%post management
# echo "Updating /etc/default/grub with NorNet settings:"
# echo "-----"
# cat /usr/share/nornet/grub-defaults | \
#    ( if grep "biosdevname=0" >/dev/null 2>&1 /proc/cmdline ; then sed "s/^GRUB_CMDLINE_LINUX=\"/GRUB_CMDLINE_LINUX=\"biosdevname=0 /g" ; else cat ; fi ) | \
#    ( if grep "net.ifnames=0" >/dev/null 2>&1 /proc/cmdline ; then sed "s/^GRUB_CMDLINE_LINUX=\"/GRUB_CMDLINE_LINUX=\"net.ifnames=0 /g" ; else cat ; fi ) | tee /etc/default/grub.new && \
# mv /etc/default/grub.new /etc/default/grub
if [ -e /usr/sbin/grub2-mkconfig ] ; then /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg || true ; fi

%postun management
rm -f /etc/grub.d/??_neat_desktop_theme
if [ -e /usr/sbin/grub2-mkconfig ] ; then /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg || true ; fi


%package development
Summary: NEAT Development
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
Requires: gnuplot
Requires: google-noto-cjk-fonts
Requires: google-noto-sans-fonts
Requires: google-noto-serif-fonts
Requires: GraphicsMagick
Requires: libcurl-devel
Requires: libpcap-devel
Requires: libtool
Requires: lksctp-tools-devel
Requires: make
Requires: mock
Requires: openssl-devel
Requires: pbuilder
Requires: perl-Image-ExifTool
Requires: pkg-config
Requires: python3
Requires: qt5-qtbase-devel
Requires: quilt
Requires: R-base
Requires: rpm
Requires: texlive-epstopdf-bin
Requires: urw-base35-fonts
Requires: valgrind
Recommends: libneat-devel
Recommends: libneat-docs
Recommends: libneat-socketapi-devel
Recommends: rsplib-devel


%description development
This meta-package contains basic software for NEAT development.
The software installed provides a common working environment.
See https://www.neat-project.org for details on NEAT!

%files development
/boot/NEAT/NEATDevelopment1-1024x768.jpeg
%{_sysconfdir}/grub.d/??_neat_development_theme

%post development
if [ -e /usr/sbin/grub2-mkconfig ] ; then /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg || true ; fi

%postun development
rm -f /etc/grub.d/??_neat_desktop_theme
if [ -e /usr/sbin/grub2-mkconfig ] ; then /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg || true ; fi


%package desktop
Summary: NEAT Desktop
Group: Applications/Internet
BuildArch: noarch
Requires: %{name}-management = %{version}-%{release}
Recommends: xorg-x11-drv-vmware

%description desktop
This meta-package contains the scripts to configure a NEAT desktop.
See https://www.neat-project.org for details on NEAT!

%files desktop
/boot/NEAT/NEATDesktop1-1024x768.jpeg
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
