%define major   7
%define libname %mklibname igfxcmrt
%define develname %mklibname igfxcmrt -d

Name:           intel-media-driver
Version:        25.4.0
Release:        1
Summary:        Hardware-accelerated video processing on Intel integrated GPUs Library
Group:          System/Kernel and hardware
License:        MIT
URL:            https://github.com/intel/media-driver
Source0:        https://github.com/intel/media-driver/archive/%{version}/media-driver-intel-media-%{version}.tar.gz

BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(igdgmm)
BuildRequires:  pkgconfig(libdrm_intel)
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(OpenCL)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(libva)

BuildSystem:	cmake
BuildOption:	-DBUILD_DISPATCHER=ON
BuildOption:	-DBUILD_SAMPLES=OFF
BuildOption:	-DBUILD_TESTS=ON
BuildOption:	-DBUILD_TOOLS=OFF
BuildOption:	-DENABLE_OPENCL=ON
BuildOption:	-DENABLE_WAYLAND=ON
BuildOption:	-DENABLE_X11=ON
BuildOption:	-DENABLE_X11_DRI3=ON
BuildOption:	-DUSE_SYSTEM_GTEST=ON

Requires:       %{libname} = %{EVRD}

%patchlist
media-driver-clang.patch

%description
Intel Media SDK provides a plain C API to access hardware-accelerated video
decode, encode and filtering on Intel Gen graphics hardware platforms.
Implementation written in C++ 11 with parts in C-for-Media (CM).
Hardware-accelerated video processing driver for VAAPI Intel

Supported video encoders: HEVC, AVC, MPEG-2, JPEG, VP9 Supported video decoders:
HEVC, AVC, VP8, VP9, MPEG-2, VC1, JPEG Supported video pre-processing filters:
Color Conversion, Deinterlace, Denoise, Resize, Rotate, Composition
 
%package -n     %{libname}
Summary:        Hardware-accelerated video processing on Intel integrated GPUs Library
Group:          System/Libraries
 
%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with igfxcmrt library.
 
%package -n     %{develname}
Summary:        SDK for hardware-accelerated video processing on Intel integrated GPUs
Group:          Development/C++
Requires:       %{name} = %{EVRD}
Requires:       %{libname} = %{EVRD}
Provides:       %{name}-devel = %{EVRD}
 
%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use igfxcmrt library.

%files
%{_libdir}/dri/*_drv_video.so
 
%files -n %{libname}
%{_libdir}/libigfxcmrt.so.%{major}{,.*}
 
%files -n %{develname}
%dir %{_includedir}/igfxcmrt
%{_includedir}/igfxcmrt/cm_*.h
%{_libdir}/libigfxcmrt.so
%{_libdir}/pkgconfig/igfxcmrt.pc
