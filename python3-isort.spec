# TODO:
# - enable tests
# - package docs (mkdocs based)
#
# Conditional build:
%bcond_with	tests	# unit tests (needs more dependencies in PLD)

%define		module	isort
Summary:	Python 2 library to sort imports alphabetically
Summary(pl.UTF-8):	Narzędzie Pythona 2 do alfabetycznego sortowania listy importów
Name:		python3-%{module}
Version:	9.0.2
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/isort/
Source0:	https://files.pythonhosted.org/packages/source/i/isort/%{module}-%{version}.tar.gz
# Source0-md5:	d83b9145f1cc90203c1e6907ca93ad29
Patch0:		%{module}-no-mypyc-build-dep.patch
URL:		https://github.com/timothycrosley/isort
BuildRequires:	python3-build
BuildRequires:	python3-hatch-vcs
BuildRequires:	python3-hatchling
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.10
%if %{with tests}
BuildRequires:	python3-colorama >= 0.4.6
BuildRequires:	python3-hypothesis >= 6.10.1
BuildRequires:	python3-hypothesmith >= 0.1.3
BuildRequires:	python3-libcst >= 0.3.18
BuildRequires:	python3-mypy_extensions >= 1.1.0
BuildRequires:	python3-pytest >= 7.4.2
# verify if needed for tests
#BuildRequires:	python3-pip-api
#BuildRequires:	python3-pipreqs
#BuildRequires:	python3-requirementslib >= 1.5
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
isort is a Python utility / library to sort imports alphabetically,
and automatically separated into sections and by type. It provides a
command line utility, Python library and plugins for various editors
to quickly sort all your imports. It requires Python 3.10+ to run but
supports formatting Python 2 code too.

This package contains Python 3 library.

%description -l pl.UTF-8
isort to pythonowe narzędzie/biblioteka do alfabetycznego sortowania
importów i automatycznego dzielenia ich na sekcje i po rodzaju.
Udostępnia narzędzie wiersza poleceń, bibliotekę Pythona i wtyczki do
różnych edytorów, pozwalające szybko posortować importy. Wymaga do
działania Pythona 3.10+, ale obsługuje także formatowanie kodu Pythona
2.

Ten pakiet zawiera bibliotekę Pythona 3.

%package -n isort
Summary:	Python utility to sort imports alphabetically
Summary(pl.UTF-8):	Pythonowe narzędzie do alfabetycznego sortowania listy importów
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}

%description -n isort
isort is a Python utility / library to sort imports alphabetically,
and automatically separated into sections and by type. It provides a
command line utility, Python library and plugins for various editors
to quickly sort all your imports. It requires Python 3.10+ to run but
supports formatting Python 2 code too.

This package contains command line utility.

%description -n isort -l pl.UTF-8
isort to pythonowe narzędzie/biblioteka do alfabetycznego sortowania
importów i automatycznego dzielenia ich na sekcje i po rodzaju.
Udostępnia narzędzie wiersza poleceń, bibliotekę Pythona i wtyczki do
różnych edytorów, pozwalające szybko posortować importy. Wymaga do
działania Pythona 3.10+, ale obsługuje także formatowanie kodu Pythona
2.

Ten pakiet zawiera narzędzie wiersza poleceń.

%prep
%setup -q -n %{module}-%{version}
%patch -P0 -p1

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest test_isort.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%{py3_sitescriptdir}/isort
%{py3_sitescriptdir}/isort-%{version}.dist-info

%files -n isort
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/isort
%attr(755,root,root) %{_bindir}/isort-identify-imports
