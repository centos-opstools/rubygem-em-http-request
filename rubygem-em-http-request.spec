# Generated from em-http-request-1.1.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name em-http-request

Name:           rubygem-%{gem_name}
Version:        1.1.5
Release:        3%{?dist}
Summary:        EventMachine based, async HTTP Request client
Group:          Development/Languages
License:        MIT
URL:            http://github.com/igrigorik/em-http-request
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:         0000-Remove-bundler-dependency.patch

BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(multi_json)
BuildRequires:  rubygem(rack)
BuildRequires:  rubygem(eventmachine) >= 1.0.3
BuildRequires:  rubygem(em-socksify) >= 0.3
BuildRequires:  rubygem(addressable) >= 2.3.4
BuildRequires:  rubygem(cookiejar) >= 0.3.2
BuildRequires:  rubygem(http_parser.rb) >= 0.6.0

Requires:       rubygem(eventmachine) >= 1.0.3
Requires:       rubygem(em-socksify) >= 0.3
Requires:       rubygem(addressable) >= 2.3.4
Requires:       rubygem(cookiejar) >= 0.3.2
Requires:       rubygem(http_parser.rb) >= 0.6.0

%if 0%{?rhel} > 0
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
EventMachine based, async HTTP Request client.


%package doc
Summary:        Documentation for %{name}
Group:          Documentation
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%patch0 -p1

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
rm -f .%{gem_dir}/.travis.yml
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


# Run the test suite
%check
pushd .%{gem_instdir}
# XXX: Disable tests, because network connection is required
#rspec -Ilib spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gemtest
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%{gem_instdir}/.rspec
%{gem_instdir}/benchmarks
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Changelog.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/em-http-request.gemspec
%{gem_instdir}/examples
%{gem_instdir}/spec

%changelog
* Mon Sep 04 2017 Matthias Runge <mrunge@redhat.com> - 1.1.5-3
- bump version to trigger build
- initial import into CentOS opstools

* Mon Jan 02 2017 Martin Mágr <mmagr@redhat.com> - 1.1.5-2
- Disabled unit tests due to network connection requirement

* Mon Jan 02 2017 Martin Mágr <mmagr@redhat.com> - 1.1.5-1
- Initial package
