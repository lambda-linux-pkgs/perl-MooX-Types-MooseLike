Name:           perl-MooX-Types-MooseLike
Version:        0.27
Release:        1%{?dist}
Summary:        Some Moosish types and a type builder
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/MooX-Types-MooseLike/
Source0:        http://www.cpan.org/authors/id/M/MA/MATEU/MooX-Types-MooseLike-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(List::Util)
#BuildRequires:  perl(Module::Runtime) >= 0.012
BuildRequires:  perl(Moo) >= 0.09101
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(overload)
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Fatal) >= 0.003
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(warnings)
#Requires:       perl(Module::Runtime) >= 0.012
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
For package support, please visit
https://github.com/lambda-linux-pkgs/%{name}/issues

See MooX::Types::MooseLike::Base for a list of available base types. Its source
also provides an example of how to build base types, along with both
parameterizable and non-parameterizable.

%prep
%setup -q -n MooX-Types-MooseLike-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Aug 29 2014 Petr Pisar <ppisar@redhat.com> - 0.27-1
- 0.27 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 18 2013 Simone Caronni <negativo17@gmail.com> - 0.25-2
- Review fixes.

* Mon Aug 05 2013 Simone Caronni <negativo17@gmail.com> 0.25-1
- Specfile autogenerated by cpanspec 1.78.
