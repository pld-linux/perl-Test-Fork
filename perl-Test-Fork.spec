#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Test
%define		pnam	Fork
Summary:	Test::Fork - test code which forks
Summary(pl.UTF-8):	Test::Fork - testowanie kodu, który rozgałęzia procesy
Name:		perl-Test-Fork
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ac77c9fec0f933db312d7b2fc9b3e7d1
URL:		https://metacpan.org/release/Test-Fork
BuildRequires:	perl-Module-Build >= 0.2808
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(Test::Builder::Module) >= 0.02
BuildRequires:	perl-Test-Builder-Tester >= 1.02
BuildRequires:	perl-Test-Simple >= 0.62
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
THIS IS ALPHA CODE! The implementation is unreliable and the interface
is subject to change.

Because each test has a number associated with it, testing code which
forks is problematic. Coordinating the test number amongst the parent
and child processes is complicated. Test::Fork provides a function to
smooth over the complications.

%description -l pl.UTF-8
TEN KOD JEST W STADIUM ALFA! Implementacja nie jest wiarygodna, a
interfejs może się zmienić.

Ponieważ każdy test ma powiązaną ze sobą liczbę, testowanie kodu,
który rozgałęzia procesy (wykonuje fork), jest problematyczne.
Koordynowanie numerów testów między procesy rodzica i potomka jest
skomplikowane. Test::Fork dostarcza funkcję, która zaciera te
komplikacje.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Test/Fork.pm
%{_mandir}/man3/Test::Fork.3pm*
