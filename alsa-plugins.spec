#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
# Source0 file verified with key 0x8380596DA6E59C91 (release@alsa-project.org)
#
Name     : alsa-plugins
Version  : 1.2.7.1
Release  : 53
URL      : https://www.alsa-project.org/files/pub/plugins/alsa-plugins-1.2.7.1.tar.bz2
Source0  : https://www.alsa-project.org/files/pub/plugins/alsa-plugins-1.2.7.1.tar.bz2
Source1  : https://www.alsa-project.org/files/pub/plugins/alsa-plugins-1.2.7.1.tar.bz2.sig
Summary  : Extra alsa plugins
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: alsa-plugins-data = %{version}-%{release}
Requires: alsa-plugins-lib = %{version}-%{release}
Requires: alsa-plugins-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(avtp)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(libavcodec)
BuildRequires : pkgconfig(libavutil)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libswresample)
BuildRequires : pkgconfig(samplerate)
BuildRequires : pkgconfig(sndfile)
BuildRequires : pkgconfig(speexdsp)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
PulseAudio <--> ALSA plugins
============================
This plugin allows any program that uses the ALSA API to access a PulseAudio
sound daemon. In other words, native ALSA applications can play and record
sound across a network.

%package data
Summary: data components for the alsa-plugins package.
Group: Data

%description data
data components for the alsa-plugins package.


%package lib
Summary: lib components for the alsa-plugins package.
Group: Libraries
Requires: alsa-plugins-data = %{version}-%{release}
Requires: alsa-plugins-license = %{version}-%{release}

%description lib
lib components for the alsa-plugins package.


%package license
Summary: license components for the alsa-plugins package.
Group: Default

%description license
license components for the alsa-plugins package.


%prep
%setup -q -n alsa-plugins-1.2.7.1
cd %{_builddir}/alsa-plugins-1.2.7.1
pushd ..
cp -a alsa-plugins-1.2.7.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685477846
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1685477846
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/alsa-plugins
cp %{_builddir}/alsa-plugins-%{version}/COPYING %{buildroot}/usr/share/package-licenses/alsa-plugins/597bf5f9c0904bd6c48ac3a3527685818d11246d || :
cp %{_builddir}/alsa-plugins-%{version}/COPYING.GPL %{buildroot}/usr/share/package-licenses/alsa-plugins/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1 || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/alsa/alsa.conf.d/10-rate-lav.conf
/usr/share/alsa/alsa.conf.d/10-samplerate.conf
/usr/share/alsa/alsa.conf.d/10-speexrate.conf
/usr/share/alsa/alsa.conf.d/50-arcam-av-ctl.conf
/usr/share/alsa/alsa.conf.d/50-oss.conf
/usr/share/alsa/alsa.conf.d/50-pulseaudio.conf
/usr/share/alsa/alsa.conf.d/60-a52-encoder.conf
/usr/share/alsa/alsa.conf.d/60-speex.conf
/usr/share/alsa/alsa.conf.d/60-upmix.conf
/usr/share/alsa/alsa.conf.d/60-vdownmix.conf
/usr/share/alsa/alsa.conf.d/98-usb-stream.conf

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/alsa-lib/libasound_module_conf_pulse.so
/V3/usr/lib64/alsa-lib/libasound_module_ctl_arcam_av.so
/V3/usr/lib64/alsa-lib/libasound_module_ctl_oss.so
/V3/usr/lib64/alsa-lib/libasound_module_ctl_pulse.so
/V3/usr/lib64/alsa-lib/libasound_module_pcm_a52.so
/V3/usr/lib64/alsa-lib/libasound_module_pcm_aaf.so
/V3/usr/lib64/alsa-lib/libasound_module_pcm_oss.so
/V3/usr/lib64/alsa-lib/libasound_module_pcm_pulse.so
/V3/usr/lib64/alsa-lib/libasound_module_pcm_speex.so
/V3/usr/lib64/alsa-lib/libasound_module_pcm_upmix.so
/V3/usr/lib64/alsa-lib/libasound_module_pcm_usb_stream.so
/V3/usr/lib64/alsa-lib/libasound_module_pcm_vdownmix.so
/V3/usr/lib64/alsa-lib/libasound_module_rate_lavrate.so
/V3/usr/lib64/alsa-lib/libasound_module_rate_samplerate.so
/V3/usr/lib64/alsa-lib/libasound_module_rate_speexrate.so
/usr/lib64/alsa-lib/libasound_module_conf_pulse.so
/usr/lib64/alsa-lib/libasound_module_ctl_arcam_av.so
/usr/lib64/alsa-lib/libasound_module_ctl_oss.so
/usr/lib64/alsa-lib/libasound_module_ctl_pulse.so
/usr/lib64/alsa-lib/libasound_module_pcm_a52.so
/usr/lib64/alsa-lib/libasound_module_pcm_aaf.so
/usr/lib64/alsa-lib/libasound_module_pcm_oss.so
/usr/lib64/alsa-lib/libasound_module_pcm_pulse.so
/usr/lib64/alsa-lib/libasound_module_pcm_speex.so
/usr/lib64/alsa-lib/libasound_module_pcm_upmix.so
/usr/lib64/alsa-lib/libasound_module_pcm_usb_stream.so
/usr/lib64/alsa-lib/libasound_module_pcm_vdownmix.so
/usr/lib64/alsa-lib/libasound_module_rate_lavrate.so
/usr/lib64/alsa-lib/libasound_module_rate_lavrate_fast.so
/usr/lib64/alsa-lib/libasound_module_rate_lavrate_faster.so
/usr/lib64/alsa-lib/libasound_module_rate_lavrate_high.so
/usr/lib64/alsa-lib/libasound_module_rate_lavrate_higher.so
/usr/lib64/alsa-lib/libasound_module_rate_samplerate.so
/usr/lib64/alsa-lib/libasound_module_rate_samplerate_best.so
/usr/lib64/alsa-lib/libasound_module_rate_samplerate_linear.so
/usr/lib64/alsa-lib/libasound_module_rate_samplerate_medium.so
/usr/lib64/alsa-lib/libasound_module_rate_samplerate_order.so
/usr/lib64/alsa-lib/libasound_module_rate_speexrate.so
/usr/lib64/alsa-lib/libasound_module_rate_speexrate_best.so
/usr/lib64/alsa-lib/libasound_module_rate_speexrate_medium.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/alsa-plugins/597bf5f9c0904bd6c48ac3a3527685818d11246d
/usr/share/package-licenses/alsa-plugins/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1
