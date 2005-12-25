Summary:	Sos - Polish store system
Summary(pl):	Sos - System Obs³ugi Sprzeda¿y 
Name:		sos
Version:	2.0.4
Release:	0.1
License:	Demo of commercial application
Group:		Applications
Source0:	http://www.softservice.com.pl/store/sos/%{name}-demo-%{version}.tgz
# Source0-md5:	a9dc0c0ac04be91ae050d0b7cdb4194f
URL:		http://sos.softservice.com.pl/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SOS is a Polish store system, working in the most infallible OS 
(namely Linux). Package allows one to document and account supplies of 
goods, creating invoices. It also contains KPiR (which is specific for 
Polish accounting system).

If you don't live in Poland, you probably won't use it anyway.

%description -l pl
SOS jest system magazynowym pracuj±cym w najbardziej niezawodnym
systemie operacyjnym jakim jest Linux. Pakiet pozwala na
dokumentowanie przyjêæ towarów do magazynu oraz wystawianie faktur
sprzeda¿y oraz paragonów. Dodatkowo dostêpna jest prosta Podatkowa
Ksi±¿ka Przychodów i Rozchodów umo¿liwiaj±ca rejestracjê zdarzeñ
gospodarczych do celów podatkowych.

%prep
%setup -q -n %{name}-demo-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install bin/* $RPM_BUILD_ROOT%{_bindir}
for subdir in bazy cfg_def pl scripts; do
	install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/$subdir
	cp -a $subdir/* $RPM_BUILD_ROOT%{_datadir}/%{name}/$subdir
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
