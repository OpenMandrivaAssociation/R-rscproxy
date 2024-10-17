%global packname  rscproxy
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.0.5
Release:          3
Summary:          statconn: provides portable C-style interface to R (StatConnector)
Group:            Sciences/Mathematics
License:          GPL-2
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/rscproxy_2.0-5.tar.gz
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 

%description
rscproxy library provides an interface to R used by third party
applications, most notable, but not limited to, statconnDCOM, ROOo and
other systems.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/libs


%changelog
* Sat Feb 18 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3_1-1
+ Revision: 776346
- Import R-rscproxy
- Import R-rscproxy


