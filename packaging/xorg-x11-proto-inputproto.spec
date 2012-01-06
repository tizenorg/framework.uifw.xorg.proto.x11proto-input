
Name:       xorg-x11-proto-inputproto
Summary:    X.Org X11 Protocol inputproto
Version:    2.0.1
Release:    0
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/proto/inputproto-%{version}.tar.gz
Provides:   inputproto
BuildRequires: pkgconfig(xorg-macros)


%description
Description: %{summary}



%prep
%setup -q -n inputproto-%{version}

%build

%reconfigure --disable-shared

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%clean
rm -rf %{buildroot}





%files
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/inputproto.pc
%{_includedir}/X11/extensions/XI.h
%{_includedir}/X11/extensions/XIproto.h
%{_includedir}/X11/extensions/XI2.h
%{_includedir}/X11/extensions/XI2proto.h
%{_docdir}/inputproto


