Summary:	A tool which will start a program on a virtual console
Summary(de):	Tools zum Erstellen virtueller Konsolen
Summary(fr):	Outils pour créer des consoles virtuelles
Summary(tr):	Sanal konsol yaratmak için araçlar
Name:		open
Version:	1.4
Release:	7
License:	GPL
Group:		Utilities/Console
Source:		ftp://sunsite.unc.edu/pub/Linux/utils/console/%{name}-%{version}.tar.gz
Patch:		open-includes.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The open command starts a specified command with the first available
virtual console, or on a virtual console that you specify.  Install the
open package if you regularly use virtual consoles to run programs.

%description -l de
Dieses Programm führt einen Befehl auf eine angegebene virtuelle
Konsolennummer aus. Es ist auch möglich, den Befehl auf die erste, noch
nicht in Gebrauch befindliche Konsole auszuführen.

%description -l fr
Ce programme exécute une commande sur un numéro de console donné. il peut
aussi exécuter le programme sur la première console virtuelle qui n'est pas
encore utilisée.

%description -l tr
Bu program sayesinde bir kullanýcý istediði sanal konsolda bir program
koþturabilir. Ýstenirse program kullanýmda olmayan ilk sanal konsolda
çalýþtýrýlabilir.

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
%attr(2755,root,root) %{_bindir}/open
%attr(755,root,root) %{_bindir}/switchto
%{_mandir}/man1/*
