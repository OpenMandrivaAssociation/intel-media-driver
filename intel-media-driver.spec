%define major   7
%define libname %mklibname igfxcmrt %{major}
%define develname %mklibname igfxcmrt -d

Name:           intel-media-driver
Version:        23.3.1
Release:        1
Summary:        Hardware-accelerated video processing on Intel integrated GPUs Library
Group:          System/Kernel and hardware
License:        MIT
URL:            https://github.com/intel/media-driver
Source0:        %{url}/archive/%{version}/media-driver-intel-media-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(igdgmm)
BuildRequires:  pkgconfig(libdrm_intel)
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ocl-icd)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(libva)

%description
Intel Media SDK provides a plain C API to access hardware-accelerated video
decode, encode and filtering on Intel Gen graphics hardware platforms.
Implementation written in C++ 11 with parts in C-for-Media (CM).

Supported video encoders: HEVC, AVC, MPEG-2, JPEG, VP9 Supported video decoders:
HEVC, AVC, VP8, VP9, MPEG-2, VC1, JPEG Supported video pre-processing filters:
Color Conversion, Deinterlace, Denoise, Resize, Rotate, Composition

%package -n     vaapi-driver-%{name}
Summary:        Hardware-accelerated video processing driver for VAAPI Intel
Group:          System/Kernel and hardware
 
%description -n vaapi-driver-%{name}
This package contains the driver needed to access hardware 
 

%package -n     %{libname}
Summary:        Hardware-accelerated video processing on Intel integrated GPUs Library
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}
 
%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with igfxcmrt library.
 
%package -n     %{develname}
Summary:        SDK for hardware-accelerated video processing on Intel integrated GPUs
Group:          Development/C++
Requires:       %{libname} = %{version}
Provides:       %{name}-devel = %{version}-%{release}
 
%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use igfxcmrt library.

%files -n vaapi-driver-%{name}
%{_libdir}/dri/*_drv_video.so
 
%files -n %{libname}
%{_libdir}/libigfxcmrt.so.%{major}{,.*}
 
%files -n %{develname}
%dir %{_includedir}/igfxcmrt
%{_includedir}/igfxcmrt/cm_*.h
%{_libdir}/libigfxcmrt.so
%{_libdir}/pkgconfig/igfxcmrt.pc

%prep
%autosetup -p1 -n media-driver-intel-media-%{version}

%build
%cmake \
    -DBUILD_DISPATCHER=ON \
    -DBUILD_SAMPLES=OFF \
    -DBUILD_TESTS=ON \
    -DBUILD_TOOLS=OFF \
    -DENABLE_OPENCL=ON \
    -DENABLE_WAYLAND=ON \
    -DENABLE_X11=ON \
    -DENABLE_X11_DRI3=ON \
    -DUSE_SYSTEM_GTEST=ON \

%make_build

%install
%make_install -C build
find %{buildroot} -name '*.la' -exec rm -f {} ';'
