%define	module	spynner
%define name	python-%{module}
%define version 1.10
%define release %mkrel 1

Summary:	Programmatic web browsing module with AJAX support for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/s/%{module}/%{module}-%{version}.tar.gz
Patch0:		manual-example-install-1.10.patch
License:	GPLv3+
Group:		Development/Python
Url:		https://github.com/makinacorpus/spynner
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python-beautifulsoup, python-pyquery
Requires:	python-qt4 >= 4.4.3
BuildRequires:	python-setuptools
BuildRequires:	python-beautifulsoup, python-pyquery
BuildRequires:	python-qt4 >= 4.4.3

%description
Spynner is a stateful programmatic web browser module for Python.
Based upon PyQT and WebKit, it supports Javascript, AJAX, and every
other technology that browsers other than WebKit are able to handle
(Flash, SVG, ...). Spynner takes advantage of jQuery, a powerful
Javascript library that makes the interaction with pages and event
simulation really easy.

Using Spynner, one can simulate a web browser with no GUI (although a
browsing window can be opened for debugging purposes); it therefore
may be used to implement web crawlers or acceptance testing tools.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p0 

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc CHANGES.txt COPYING README.rst examples/

