Summary:	A tool which will start a program on a virtual console
Summary(de.UTF-8):	Tools zum Erstellen virtueller Konsolen
Summary(es.UTF-8):	Herramientas para creación de consolas virtuales
Summary(fr.UTF-8):	Outils pour créer des consoles virtuelles
Summary(pl.UTF-8):	Narzędzie uruchamiające program na konsoli wirtualnej
Summary(pt_BR.UTF-8):	Ferramentas para criação de consoles virtuais
Summary(ru.UTF-8):	Утилита для запуска программы на указанной виртуальной консоли
Summary(tr.UTF-8):	Sanal konsol yaratmak için araçlar
Summary(uk.UTF-8):	Утиліта для запуску програми на вказаній віртуальній консолі
Name:		open
Version:	1.4
Release:	20
License:	GPL
Group:		Applications/Console
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/console/%{name}-%{version}.tar.gz
# Source0-md5:	590781ba76d9d499d7843c0b4651da70
Patch0:		%{name}-includes.patch
ExcludeArch:	s390 s390x
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The open command starts a specified command with the first available
virtual console, or on a virtual console that you specify. Install the
open package if you regularly use virtual consoles to run programs.

%description -l de.UTF-8
Dieses Programm führt einen Befehl auf eine angegebene virtuelle
Konsolennummer aus. Es ist auch möglich, den Befehl auf die erste,
noch nicht in Gebrauch befindliche Konsole auszuführen.

%description -l es.UTF-8
Este programa ejecuta un comando en una determinada consola virtual.
También puede ejecutar el programa en la primera consola virtual que
no esté más en uso.

%description -l fr.UTF-8
Ce programme exécute une commande sur un numéro de console donné. il
peut aussi exécuter le programme sur la première console virtuelle qui
n'est pas encore utilisée.

%description -l pl.UTF-8
Polecenie open uruchamia podane polecenie na pierwszej dostępnej
konsoli wirtualnej, lub na podanej konsoli.

%description -l pt_BR.UTF-8
Este programa executa um comando numa determinada console virtual.
Também pode executar o programa no primeiro console virtual que não
está mais em uso.

%description -l ru.UTF-8
Программа open запускает указанную команду на первой доступной
виртуальной консоли или на консоли указанной пользователем.

%description -l tr.UTF-8
Bu program sayesinde bir kullanıcı istediği sanal konsolda bir program
koşturabilir. İstenirse program kullanımda olmayan ilk sanal konsolda
çalıştırılabilir.

%description -l uk.UTF-8
Програма open запускає вказану команду на першій доступній віртуальній
консолі чи на консолі вказаній користувачем.

%prep
%setup -q
%patch0 -p1

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
