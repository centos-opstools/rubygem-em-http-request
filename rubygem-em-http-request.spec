# Generated from em-http-request-1.1.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name em-http-request

Name:           rubygem-%{gem_name}
Version:        XXX
Release:        1%{?dist}
Summary:        EventMachine based, async HTTP Request client
Group:          Development/Languages
License:        MIT
URL:            http://github.com/igrigorik/em-http-request
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(multi_json)
BuildRequires:  rubygem(rack)
BuildRequires:  rubygem(eventmachine)
BuildRequires:  rubygem(em-socksify)
BuildRequires:  rubygem(addressable)
BuildRequires:  rubygem(cookiejar)
BuildRequires:  rubygem(http_parser.rb)

Requires:       rubygem(eventmachine)
Requires:       rubygem(em-socksify)
Requires:       rubygem(addressable)
Requires:       rubygem(cookiejar)
Requires:       rubygem(http_parser.rb)

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
%if 0%{?dlrn} > 0
%setup -q -D -T -n  %{dlrn_nvr}
%else
%setup -q -D -T -n  %{gem_name}-%{version}
%endif
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

# Remove bundler dependency
find spec/ -type f -exec sed "s/require ['\"]bundler.*['\"]//g" {} +


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
