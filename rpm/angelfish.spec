%global _metainfodir %{_datadir}/metainfo

Name:           angelfish
Version:        24.08.2
Release:        1%{?dist}
Summary:        Plasma Mobile minimal web browser

License:        MIT and GPLv2+ and LGPLv2 and LGPLv2+
# For a breakdown of the licensing, see PACKAGE-LICENSING
URL:            https://apps.kde.org/angelfish/
Source0: %{name}-%{version}.tar.bz2

Source10: org.kde.angelfish-86.png
Source11: org.kde.angelfish-108.png
Source12: org.kde.angelfish-128.png
Source13: org.kde.angelfish-256.png

# Sailfish OS specific
Patch1: 0001-Skip-few-dependencies.patch
#Patch2: 0002-Revert-Make-use-of-C-20-ranges-library.patch


#BuildRequires:  appstream
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
#BuildRequires:  libappstream-glib
 
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-kdbusaddons-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kirigami-devel
BuildRequires:  kf6-kirigami-addons-devel
BuildRequires:  kf6-knotifications-devel
#BuildRequires:  cmake(KF5Purpose)
BuildRequires:  kf6-qqc2-desktop-style
BuildRequires:  kf6-kwindowsystem-devel
BuildRequires:  futuresql-qt6-devel

BuildRequires:  qt6-qtbase-devel
#BuildRequires:  cmake(Qt5Feedback)
#BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtquickcontrols2-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qtwebengine-devel
BuildRequires:  qt6-qtwebsockets-devel
BuildRequires:  qt6-qtwebchannel-devel
BuildRequires:  qt6-qtlocation-devel
BuildRequires:  qt6-qtbase-private-devel

Requires: kf6-kirigami
Requires: kf6-kirigami-addons
Requires: qt6-qtmultimedia
Requires: qt6-qtsvg
Requires: qt6-qtlocation
Requires: qt6-qt5compat
Requires: kf6-breeze-icons

%description
Web browser for mobile devices with Plasma integration

PackageName: Angelfish Web Browser
Type: desktop-application
Categories:
 - Network
Custom:
  Repo: https://invent.kde.org/plasma-mobile/angelfish
  PackagingRepo: https://github.com/sailfishos-chum/angelfish
Icon: https://github.com/sailfishos-chum/angelfish/raw/main/rpm/org.kde.angelfish-256.png
Screenshots:
 - https://github.com/sailfishos-chum/angelfish/raw/main/screenshots/screenshot1.png
 - https://github.com/sailfishos-chum/angelfish/raw/main/screenshots/screenshot2.png

%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
%cmake_kf6
%cmake_build

%install
%cmake_install

# adjust Exec command in .desktop
sed -i "s|Exec=angelfish|Exec=qt-runner /usr/bin/angelfish|g" \
    %{buildroot}/%{_datadir}/applications/org.kde.%{name}.desktop
echo -e "X-Nemo-Single-Instance=no\nX-Nemo-Application-Type=no-invoker\n\n[X-Sailjail]\nSandboxing=Disabled" >> \
     %{buildroot}/%{_datadir}/applications/org.kde.%{name}.desktop

# copy icons
install -p -m644 -D %{SOURCE10} \
	%{buildroot}/%{_datadir}/icons/hicolor/86x86/apps/org.kde.%{name}.png
install -p -m644 -D %{SOURCE11} \
	%{buildroot}/%{_datadir}/icons/hicolor/108x108/apps/org.kde.%{name}.png
install -p -m644 -D %{SOURCE12} \
	%{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/org.kde.%{name}.png
install -p -m644 -D %{SOURCE13} \
	%{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/org.kde.%{name}.png


%files
%license LICENSES/{MIT,GPL-2.0-or-later,LGPL-2.0-only,LGPL-2.0-or-later}.txt
%doc README.md

%{_bindir}/%{name}
%{_bindir}/%{name}-webapp

%{_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/config.kcfg/%{name}settings.kcfg
%{_datadir}/icons/hicolor/*/apps/org.kde.%{name}.*
%{_datadir}/knotifications6/%{name}.notifyrc
%{_datadir}/locale

%{_metainfodir}/org.kde.%{name}.metainfo.xml
