
Name:       xorg-x11-proto-inputproto
Summary:    X.Org X11 Protocol inputproto
Version:    2.0.1
Release:    0
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/proto/inputproto-%{version}.tar.gz
Source1001: packaging/xorg-x11-proto-inputproto.manifest 
Provides:   inputproto
BuildRequires: pkgconfig(xorg-macros)


%description
Description: %{summary}



%prep
%setup -q -n %{name}-%{version}

%build
cp %{SOURCE1001} .

%reconfigure --disable-shared

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%clean
rm -rf %{buildroot}





%files
%manifest xorg-x11-proto-inputproto.manifest
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/inputproto.pc
%{_includedir}/X11/extensions/XI.h
%{_includedir}/X11/extensions/XIproto.h
%{_includedir}/X11/extensions/XI2.h
%{_includedir}/X11/extensions/XI2proto.h
%{_docdir}/inputproto


