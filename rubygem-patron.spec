%define oname patron

Summary:    Patron HTTP client
Name:       rubygem-%{oname}
Version:    0.4.9
Release:    %mkrel 1
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
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
cp -a .%{ruby_gemdir}/* %{buildroot}%{ruby_gemdir}
rm -rf %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/ext/

# install the so file in sitearchdir
mkdir -p %{buildroot}%{ruby_sitearchdir}
mv %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/lib/patron/*.so %{buildroot}%{ruby_sitearchdir}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/spec/
%{ruby_gemdir}/gems/%{oname}-%{version}/.require_paths
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/LICENSE
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/VERSION.yml
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
%{ruby_sitearchdir}/*.so
