Summary:	A tool which will start a program on a virtual console
Summary(de):	Tools zum Erstellen virtueller Konsolen
Summary(es):	Herramientas para creaciСn de consolas virtuales
Summary(fr):	Outils pour crИer des consoles virtuelles
Summary(pl):	NarzЙdzie uruchamiaj╠ce program na konsoli wirtualnej
Summary(pt_BR):	Ferramentas para criaГЦo de consoles virtuais
Summary(ru):	Утилита для запуска программы на указанной виртуальной консоли
Summary(tr):	Sanal konsol yaratmak iГin araГlar
Summary(uk):	Утил╕та для запуску програми на вказан╕й в╕ртуальн╕й консол╕
Name:		open
Version:	1.4
Release:	17
License:	GPL
Group:		Applications/Console
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/console/%{name}-%{version}.tar.gz
# Source0-md5: 590781ba76d9d499d7843c0b4651da70
Patch0:		%{name}-includes.patch
ExcludeArch:	s390 s390x
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The open command starts a specified command with the first available
virtual console, or on a virtual console that you specify. Install the
open package if you regularly use virtual consoles to run programs.

%description -l de
Dieses Programm fЭhrt einen Befehl auf eine angegebene virtuelle
Konsolennummer aus. Es ist auch mЖglich, den Befehl auf die erste,
noch nicht in Gebrauch befindliche Konsole auszufЭhren.

%description -l es
Este programa ejecuta un comando en una determinada consola virtual.
TambiИn puede ejecutar el programa en la primera consola virtual que
no estИ mАs en uso.

%description -l fr
Ce programme exИcute une commande sur un numИro de console donnИ. il
peut aussi exИcuter le programme sur la premiХre console virtuelle qui
n'est pas encore utilisИe.

%description -l pl
Polecenie open uruchamia podane polecenie na pierwszej dostЙpnej
konsoli wirtualnej, lub na podanej konsoli.

%description -l pt_BR
Este programa executa um comando numa determinada console virtual.
TambИm pode executar o programa no primeiro console virtual que nЦo
estА mais em uso.

%description -l ru
Программа open запускает указанную команду на первой доступной
виртуальной консоли или на консоли указанной пользователем.

%description -l tr
Bu program sayesinde bir kullanЩcЩ istediПi sanal konsolda bir program
koЧturabilir. щstenirse program kullanЩmda olmayan ilk sanal konsolda
ГalЩЧtЩrЩlabilir.

%description -l uk
Програма open запуска╓ вказану команду на перш╕й доступн╕й в╕ртуальн╕й
консол╕ чи на консол╕ вказан╕й користувачем.

%prep
%setup -q
%patch -p1

%build
%{__make} CFLAGS="%{rpmcflags}"

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
%doc README*
%attr(2755,root,root) %{_bindir}/open
%attr(755,root,root) %{_bindir}/switchto
%{_mandir}/man1/*
