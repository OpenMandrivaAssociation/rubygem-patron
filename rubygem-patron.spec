%define oname patron

Summary:    Patron HTTP client
Name:       rubygem-%{oname}
Version:    0.4.18
Release:    1
Group:      Development/Ruby
License:    MIT
URL:        http://github.com/toland/Patron
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
BuildRequires: rubygems
BuildRequires: ruby-devel
BuildRequires: curl-devel
Provides:   rubygem(%{oname}) = %{version}

%description
Ruby HTTP client library based on libcurl


%prep

%build
mkdir -p .%{ruby_gemdir}
gem install -V --local --install-dir .%{ruby_gemdir} \
               --force --rdoc %{SOURCE0}

%install
mkdir -p %{buildroot}%{ruby_gemdir}
cp -a .%{ruby_gemdir}/* %{buildroot}%{ruby_gemdir}
rm -rf %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/ext/
rm -f %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/.autotest
rm -f %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/.gitignore
rm -f %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/.rspec

# install the so file in sitearchdir
mkdir -p %{buildroot}%{ruby_sitearchdir}
mv %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/lib/patron/*.so %{buildroot}%{ruby_sitearchdir}

%files
%defattr(-, root, root, -)
%{ruby_gemdir}/gems/%{oname}-%{version}/*
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
%{ruby_sitearchdir}/*.so


%changelog
* Thu Nov 04 2010 Rémy Clouard <shikamaru@mandriva.org> 0.4.9-1mdv2011.0
+ Revision: 593114
- import rubygem-patron

