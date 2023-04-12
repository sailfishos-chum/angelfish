%global _metainfodir %{_datadir}/metainfo

Name:           angelfish
Version:        23.03.90
Release:        1%{?dist}
Summary:        Plasma Mobile minimal web browser

License:        MIT and GPLv2+ and LGPLv2 and LGPLv2+
# For a breakdown of the licensing, see PACKAGE-LICENSING
URL:            https://invent.kde.org/plasma-mobile/%{name}
Source0: %{name}-%{version}.tar.bz2

# Sailfish OS specific
Patch1: 0001-Skip-few-dependencies.patch
Patch2: 0002-Revert-Make-use-of-C-20-ranges-library.patch

%{?opt_kf5_default_filter}


#BuildRequires:  appstream
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  opt-extra-cmake-modules
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  opt-kf5-rpm-macros
#BuildRequires:  libappstream-glib
 
BuildRequires:  opt-kf5-kconfig-devel
BuildRequires:  opt-kf5-kcoreaddons-devel
BuildRequires:  opt-kf5-kdbusaddons-devel
BuildRequires:  opt-kf5-ki18n-devel
BuildRequires:  opt-kf5-kirigami2-devel
BuildRequires:  opt-kf5-kirigami-addons
BuildRequires:  opt-kf5-knotifications-devel
#BuildRequires:  cmake(KF5Purpose)
#BuildRequires:  cmake(KF5QQC2DesktopStyle)
BuildRequires:  opt-kf5-kwindowsystem-devel

BuildRequires:  opt-qt5-qtbase-devel
#BuildRequires:  cmake(Qt5Feedback)
#BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  opt-qt5-qtmultimedia-devel
BuildRequires:  opt-qt5-qtdeclarative-devel
BuildRequires:  opt-qt5-qtquickcontrols2-devel
BuildRequires:  opt-qt5-qtsvg-devel
BuildRequires:  opt-qt5-qtwebengine-devel
BuildRequires:  opt-qt5-qtwebsockets-devel
BuildRequires:  opt-qt5-qtwebchannel-devel
BuildRequires:  opt-qt5-qtlocation-devel
BuildRequires:  opt-qt5-qtlocation-pos-geoclue
BuildRequires:  opt-qt5-qtlocation-pos-geoclue2
BuildRequires:  opt-qt5-qtlocation-pos-positionpoll

%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}

Requires: opt-kf5-kirigami2%{_isa} 
Requires: opt-qt5-qtwayland%{_isa}
Requires: opt-kf5-kconfig-gui
Requires: opt-kf5-kcoreaddons
Requires: opt-kf5-kdbusaddons
Requires: opt-kf5-ki18n
Requires: opt-kf5-kirigami2
Requires: opt-kf5-kirigami-addons
Requires: opt-kf5-knotifications
Requires: opt-kf5-kwindowsystem
Requires: opt-qt5-qtbase-gui
Requires: opt-qt5-qtmultimedia
Requires: opt-qt5-qtquickcontrols2
Requires: opt-qt5-qtsvg
Requires: opt-qt5-qtwebengine
Requires: opt-qt5-qtlocation

%description
Web browser for mobile devices with Plasma integration

%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

mkdir -p build
pushd build

%_opt_cmake_kf5 ../
%make_build

popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd


%files
%license LICENSES/{MIT,GPL-2.0-or-later,LGPL-2.0-only,LGPL-2.0-or-later}.txt
%doc README.md

%{_opt_kf5_bindir}/%{name}
%{_opt_kf5_bindir}/%{name}-webapp

%{_opt_kf5_datadir}/applications/org.kde.%{name}.desktop
%{_opt_kf5_datadir}/config.kcfg/%{name}settings.kcfg
%{_opt_kf5_datadir}/icons/hicolor/scalable/apps/org.kde.%{name}.svg
%{_opt_kf5_datadir}/knotifications5/%{name}.notifyrc
%{_opt_kf5_datadir}/locale

%{_metainfodir}/org.kde.%{name}.metainfo.xml
