Summary:	A tool which will start a program on a virtual console.
Name:		open
Version:	1.4
Release:	6
Copyright:	GPL
Group:		Applications/System
Source:		ftp://sunsite.unc.edu/pub/Linux/utils/console/%{name}-%{version}.tar.gz
Patch:		open-1.4-includes.patch
BuildRoot:	/tmp/%{name}-%{version}-root

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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

make install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/{open,switchto}

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/{open,switchto}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(4755,root,root) %{_bindir}/open
%attr(4755,root,root) %{_bindir}/switchto
%{_mandir}/man1/open.1.gz
%{_mandir}/man1/switchto.1.gz
