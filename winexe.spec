

Name: winexe
Version: 1.1
Release: 3%{?dist}
License: GPLv3+
URL: http://sourceforge.net/projects/winexe/
Summary: Remote Windows-command executor

Source0: %{name}.tar.bz2

BuildRequires: mingw32-gcc
BuildRequires: mingw64-gcc
BuildRequires: popt-devel
BuildRequires: python
BuildRequires: samba-devel


%description
Winexe remotely executes commands on Windows systems.


%prep
%setup -q -n %{name}


%build
cd source
CFLAGS='%{mingw32_cflags}' LINKFLAGS='%{mingw32_ldflags}' ./waf configure build --prefix=%{_usr} --targets=winexesvc32.exe
CFLAGS='%{mingw64_cflags}' LINKFLAGS='%{mingw64_ldflags}' ./waf configure build --prefix=%{_usr} --targets=winexesvc64.exe
CFLAGS="$RPM_OPT_FLAGS" LINKFLAGS="$RPM_LD_FLAGS" ./waf configure build --prefix=%{_usr} --targets=bin2c,winexesvc32_exe.c,winexesvc64_exe.c,winexe


%install
cd source
%{__install} -D -m 755 build/%{name} %{buildroot}%{_bindir}/%{name}
%{__install} -D -m 644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1


%files
%doc COPYING NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*


%changelog
* Fri May 20 2016 Gardar Thorsteinsson <gardart@gmail.com> 1.1-2
- Patch added to fix new Samba4 library names
- new package built with tito

* Tue Mar 25 2014 Tomas Edwardsson <tommi@tommi.org> 1.1-1
- Removed checkout (tommi@tommi.org)
- Updated changelog (tommi@tommi.org)
- Remove patch, already applied (tommi@tommi.org)
- tito releaser configuration added (tommi@tommi.org)

* Tue Mar 25 2014 Tomas Edwardsson <tommi@tommi.org>
- Removed checkout (tommi@tommi.org)
- Updated changelog (tommi@tommi.org)
- Remove patch, already applied (tommi@tommi.org)
- tito releaser configuration added (tommi@tommi.org)

* Tue Mar 25 2014 Tomas Edwardsson <tommi@tommi.org>
- Remove patch, already applied (tommi@tommi.org)
- tito releaser configuration added (tommi@tommi.org)

* Tue Mar 25 2014 Tomas Edwardsson <tommi@tommi.org> 1.1-0.2.20140208gitb787d2a
- new package built with tito

* Tue Feb 11 2014 Satoshi Matsumoto <kaorimatz@gmail.com> - 1.1-0.2.20140208gitb787d2a
- Fix license to GPLv3+

* Sat Feb 08 2014 Satoshi Matsumoto <kaorimatz@gmail.com> - 1.1-0.1.20140208gitb787d2a
- Initial package
