Summary:	A tool which will start a program on a virtual console
Summary(de):	Tools zum Erstellen virtueller Konsolen
Summary(fr):	Outils pour cr�er des consoles virtuelles
Summary(tr):	Sanal konsol yaratmak i�in ara�lar
Name:		open
Version:	1.4
Release:	12
License:	GPL
Group:		Applications/Console
Group(de):	Applikationen/Konsole
Group(pl):	Aplikacje/Konsola
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/console/%{name}-%{version}.tar.gz
Patch0:		%{name}-includes.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The open command starts a specified command with the first available
virtual console, or on a virtual console that you specify. Install the
open package if you regularly use virtual consoles to run programs.

%description -l de
Dieses Programm f�hrt einen Befehl auf eine angegebene virtuelle
Konsolennummer aus. Es ist auch m�glich, den Befehl auf die erste,
noch nicht in Gebrauch befindliche Konsole auszuf�hren.

%description -l fr
Ce programme ex�cute une commande sur un num�ro de console donn�. il
peut aussi ex�cuter le programme sur la premi�re console virtuelle qui
n'est pas encore utilis�e.

%description -l tr
Bu program sayesinde bir kullan�c� istedi�i sanal konsolda bir program
ko�turabilir. �stenirse program kullan�mda olmayan ilk sanal konsolda
�al��t�r�labilir.

%prep
%setup -q
%patch -p1

%build
%{__make} CFLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(2755,root,root) %{_bindir}/open
%attr(755,root,root) %{_bindir}/switchto
%{_mandir}/man1/*
