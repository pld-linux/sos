Summary:	Sos
Summary(pl):	Sos
Name:		sos
Version:	2.0.2
Release:	0
#Epoch:		-
License:	Demo of comercial application
Group:		-
######		Unknown group!
#Vendor:		-
#Icon:		-
Source0:	http://www.softservice.com.pl/store/sos/%{name}-demo-%{version}.tgz
# Source0-md5:	1bd931b5b39dd2d321dacb1d99857444
URL:		http://sos.softservice.com.pl
#3BuildRequires:	-
#PreReq:		-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
_Place_Holder_

%description -l pl
SOS jest system magazynowym pracuj±cym w najbardziej niezawodnym
systemie operacyjnym jakim jest LINUX. Pakiet pozwala na
dokumentowanie przyjêæ towarów do magazynu oraz wystawianie faktur
sprzeda¿y oraz paragonów. Dodatkowo dostêpna jest prosta Podatkowa
Ksi±¿ka Przychodów i Rozchodów umo¿liwiaj±ca rejestracjê zda¿eñ
gospodarczych do celów podatkowych.


%prep
%setup -q -n %{name}-demo-%{version}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT/usr/bin/
install -d $RPM_BUILD_ROOT/%{_datadir}/%{name}

install bin/* $RPM_BUILD_ROOT/usr/bin/
for subdir in bazy cfg_def pl scripts; do
	install -d $RPM_BUILD_ROOT/%{_datadir}/%{name}/$subdir
	cp -avR $subdir/* $RPM_BUILD_ROOT/%{_datadir}/%{name}/$subdir
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
