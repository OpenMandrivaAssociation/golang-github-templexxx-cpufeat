# https://github.com/templexxx/cpufeat
%global goipath github.com/templexxx/cpufeat
%global commit  cef66df7f161dee20f4d650da7268d77eaaec82d
%global date    20180724

%gometa

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        Implementation of internal/cpu in Go
License:        BSD

URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package        devel
Summary:        %{summary}

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%gosetup -q


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Sun Sep 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.4.20180724gitcef66df
- Bump to commit cef66df.
- Update to use spec 3.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20170927.git3794dfb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20170927.git3794dfb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.1.20170927.git3794dfb
- First package for Fedora

