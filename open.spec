Summary: A tool which will start a program on a virtual console.
Name: open
Version: 1.4
Release: 6
Copyright: GPL
Group: Applications/System
Source: ftp://sunsite.unc.edu/pub/Linux/utils/console/open-1.4.tar.gz
Patch: open-1.4-includes.patch
BuildRoot: /var/tmp/open-root

%description
The open command starts a specified command with the first available
virtual console, or on a virtual console that you specify.

Install the open package if you regularly use virtual consoles to
run programs.

%prep
%setup -q
%patch -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}

make BINDIR=$RPM_BUILD_ROOT/usr/bin MANDIR=$RPM_BUILD_ROOT/usr/man/man1 install

strip $RPM_BUILD_ROOT/usr/bin/{open,switchto}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/open
/usr/bin/switchto
/usr/man/man1/open.1
/usr/man/man1/switchto.1
