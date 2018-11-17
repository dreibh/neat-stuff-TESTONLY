Name: neat-stuff
Version: 0.7.0~rc1.0
Release: 1
Summary: NEAT Control
Group: Applications/Internet
License: GPLv3
URL: https://www.nntb.no/
Source: https://www.nntb.no/download/%{name}-%{version}.tar.gz

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
NEAT is a testbed for multi-homed systems. This package
contains the management software for the testbed's
infrastructure management software.
See https://www.nntb.no for details on NEAT!

%prep
%setup -q

%build
%cmake -DCMAKE_INSTALL_PREFIX=/usr -DPYTHON_LIBRARY_PREFIX=%{buildroot}/usr -DFLAT_DIRECTORY_STRUCTURE=1 -DBUILD_BOOTSPLASH=1 .
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install


%package management
Summary: NEAT Management
Group: Applications/Internet
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
Requires: netperfmeter
Requires: net-snmp-utils
Requires: net-tools
Requires: nmap
Requires: ntpdate
Requires: pxz
Requires: reiserfs-utils
Requires: reprepro
Requires: smartmontools
Requires: sslscan
Requires: subnetcalc
Requires: tcpdump
Requires: tftp
Requires: traceroute
Requires: tree
Requires: vconfig
Requires: virt-what
Requires: whois
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
/etc/grub.d/??_nornet_development_theme

%post management
cp /usr/share/nornet/grub-defaults /etc/default/grub
grub2-mkconfig -o /boot/grub2/grub.cfg

%postun management
rm -f /etc/grub.d/??_nornet_desktop_theme
grub2-mkconfig -o /boot/grub2/grub.cfg


%package development
Summary: NEAT Development
Group: Applications/Internet
Requires: autoconf
Requires: automake
Requires: banner
Requires: bison
Requires: bzip2-devel
Requires: clang
Requires: cmake
Requires: createrepo
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
Requires: python3-psycopg2
Requires: python3-pymongo
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
/etc/grub.d/??_nornet_development_theme
/etc/pbuilderrc

%post development
cp /usr/share/nornet/grub-defaults /etc/default/grub
grub2-mkconfig -o /boot/grub2/grub.cfg

%postun development
rm -f /etc/grub.d/??_nornet_desktop_theme
grub2-mkconfig -o /boot/grub2/grub.cfg


%package api
Summary: NEAT API
Group: Applications/Internet
Requires: %{name}-management = %{version}-%{release}
Requires: %{name}-api = %{version}-%{release}


%package desktop
Summary: NEAT Desktop
Group: Applications/Internet
Requires: %{name}-management = %{version}-%{release}
Requires: %{name}-api = %{version}-%{release}
Recommends: xorg-x11-drv-vmware

%description desktop
This meta-package contains the scripts to configure a NEAT desktop.
See https://www.neat-project.org for details on NEAT!

%files desktop
/boot/NEAT/NEATDesktop1-1024x768.jpeg
/etc/grub.d/??_nornet_desktop_theme
/usr/share/nornet-desktop/background/*
/usr/share/nornet-desktop/desktop/*
/usr/share/nornet-desktop/NEAT-A4.pdf

%post desktop
cp /usr/share/nornet/grub-defaults /etc/default/grub
grub2-mkconfig -o /boot/grub2/grub.cfg

%postun desktop
rm -f /etc/grub.d/??_nornet_desktop_theme
grub2-mkconfig -o /boot/grub2/grub.cfg


%changelog
* Fri Nov 16 2018 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.0.0
- Created RPM package.