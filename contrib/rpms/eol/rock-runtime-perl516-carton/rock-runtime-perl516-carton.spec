%filter_from_provides /.*/d
%filter_from_requires /^perl.*/d
%filter_setup

Name:           rock-runtime-perl516-carton
Epoch:          1
Version:        0.9.10
Release:        1%{?dist}
Summary:        A tool to manage Perl 5.16.x dependencies

Group:          Development/Languages
License:        (GPL+ or Artistic) and (GPLv2+ or Artistic) and Copyright Only and MIT and Public Domain and UCD
URL:            http://search.cpan.org/dist/carton/
Source0:        http://backpan.perl.org/authors/id/T/TO/TOKUHIROM/Test-Requires-0.06.tar.gz
Source1:        http://backpan.perl.org/authors/id/D/DA/DAGOLDEN/Capture-Tiny-0.21.tar.gz
Source2:        http://backpan.perl.org/authors/id/M/MI/MIYAGAWA/App-cpanminus-1.6008.tar.gz
Source3:        http://backpan.perl.org/authors/id/D/DA/DAGOLDEN/CPAN-Meta-YAML-0.008.tar.gz
Source4:        http://backpan.perl.org/authors/id/M/MI/MIYAGAWA/Module-CPANfile-0.9010.tar.gz
Source5:        http://backpan.perl.org/authors/id/D/DA/DAGOLDEN/Parse-CPAN-Meta-1.4404.tar.gz
Source6:        http://backpan.perl.org/authors/id/D/DA/DAGOLDEN/CPAN-Meta-Requirements-2.122.tar.gz
Source7:        http://backpan.perl.org/authors/id/D/DA/DAGOLDEN/CPAN-Meta-2.120921.tar.gz
Source8:        http://backpan.perl.org/authors/id/T/TM/TMTM/Class-Data-Inheritable-0.08.tar.gz
Source9:        http://backpan.perl.org/authors/id/D/DR/DROLSKY/Devel-StackTrace-1.30.tar.gz
Source10:       http://backpan.perl.org/authors/id/D/DR/DROLSKY/Exception-Class-1.37.tar.gz
Source11:       http://backpan.perl.org/authors/id/M/ML/MLEHMANN/common-sense-3.6.tar.gz
Source12:       http://backpan.perl.org/authors/id/M/ML/MLEHMANN/JSON-XS-2.33.tar.gz
Source13:       http://backpan.perl.org/authors/id/M/MA/MAKAMAKA/JSON-2.53.tar.gz
Source14:       http://backpan.perl.org/authors/id/D/DO/DOY/Try-Tiny-0.12.tar.gz
Source15:       http://backpan.perl.org/authors/id/A/AP/APEIRON/local-lib-1.008009.tar.gz
Source16:       http://backpan.perl.org/authors/id/M/MI/MIYAGAWA/carton-v%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  rock-runtime-perl516-core-rpmbuild >= 5.12.3-1
BuildRequires:  rock-runtime-perl516-cpanm
Requires:       rock-runtime-perl516-core >= 5.12.3-1

%description
carton is a command line tool to track the Perl module dependencies for your
Perl application. The managed dependencies are tracked in a carton.lock file,
which is meant to be version controlled, and the lock file allows other
developers of your application will have the exact same versions of the
modules.

%prep

%build
export PATH="%{perl516_rootdir}%{_bindir}:$PATH"

cpanm -l local \
    %{SOURCE0} \
    %{SOURCE1} \
    %{SOURCE2} \
    %{SOURCE3} \
    %{SOURCE4} \
    %{SOURCE5} \
    %{SOURCE6} \
    %{SOURCE7} \
    %{SOURCE8} \
    %{SOURCE9} \
    %{SOURCE10} \
    %{SOURCE11} \
    %{SOURCE12} \
    %{SOURCE13} \
    %{SOURCE14} \
    %{SOURCE15} \
    %{SOURCE16}

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{perl516_rootdir}%{_bindir} \
         %{buildroot}%{perl516_rootdir}%{_prefix}/lib

mv local %{buildroot}%{perl516_rootdir}%{_prefix}/lib/carton

cat << EOF > %{buildroot}%{perl516_rootdir}%{_bindir}/carton
#!/usr/bin/env bash

perl \
  -Mlocal::lib=%{perl516_rootdir}%{_prefix}/lib/carton \
  %{perl516_rootdir}%{_prefix}/lib/carton/bin/carton "\$@"
EOF

chmod 755 %{buildroot}%{perl516_rootdir}%{_bindir}/carton

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{perl516_rootdir}%{_bindir}/carton
%{perl516_rootdir}%{_prefix}/lib/carton

%changelog
* Fri Mar 22 2013 RockStack <packages@rockstack.org> - 1:0.9.10-1
- Update to 0.9.10

* Tue Nov 20 2012 RockStack <packages@rockstack.org> - 1:0.9.7-0.1
- Fix version and epoch
- Fix paths

* Tue Sep 11 2012 RockStack <packages@rockstack.org> - 1.5014-2
- Rebuild for Perl 5.16.1
- Update dependencies

* Mon May 14 2012 RockStack <packages@rockstack.org> - 1.5014-1
- Initial build
