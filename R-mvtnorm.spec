#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mvtnorm
Version  : 1.0.6
Release  : 33
URL      : https://cran.r-project.org/src/contrib/mvtnorm_1.0-6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mvtnorm_1.0-6.tar.gz
Summary  : Multivariate Normal and t Distributions
Group    : Development/Tools
License  : GPL-2.0
Requires: R-mvtnorm-lib
BuildRequires : clr-R-helpers

%description
No detailed description available

%package lib
Summary: lib components for the R-mvtnorm package.
Group: Libraries

%description lib
lib components for the R-mvtnorm package.


%prep
%setup -q -c -n mvtnorm

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489128855

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1489128855
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mvtnorm
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library mvtnorm


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/mvtnorm/CITATION
/usr/lib64/R/library/mvtnorm/C_API_Example/DESCRIPTION
/usr/lib64/R/library/mvtnorm/C_API_Example/NAMESPACE
/usr/lib64/R/library/mvtnorm/C_API_Example/R/test.R
/usr/lib64/R/library/mvtnorm/C_API_Example/src/test.c
/usr/lib64/R/library/mvtnorm/C_API_Example/tests/test.R
/usr/lib64/R/library/mvtnorm/DESCRIPTION
/usr/lib64/R/library/mvtnorm/INDEX
/usr/lib64/R/library/mvtnorm/Meta/Rd.rds
/usr/lib64/R/library/mvtnorm/Meta/hsearch.rds
/usr/lib64/R/library/mvtnorm/Meta/links.rds
/usr/lib64/R/library/mvtnorm/Meta/nsInfo.rds
/usr/lib64/R/library/mvtnorm/Meta/package.rds
/usr/lib64/R/library/mvtnorm/Meta/vignette.rds
/usr/lib64/R/library/mvtnorm/NAMESPACE
/usr/lib64/R/library/mvtnorm/NEWS
/usr/lib64/R/library/mvtnorm/R/mvtnorm
/usr/lib64/R/library/mvtnorm/R/mvtnorm.rdb
/usr/lib64/R/library/mvtnorm/R/mvtnorm.rdx
/usr/lib64/R/library/mvtnorm/doc/MVT_Rnews.R
/usr/lib64/R/library/mvtnorm/doc/MVT_Rnews.Rnw
/usr/lib64/R/library/mvtnorm/doc/MVT_Rnews.pdf
/usr/lib64/R/library/mvtnorm/doc/index.html
/usr/lib64/R/library/mvtnorm/help/AnIndex
/usr/lib64/R/library/mvtnorm/help/aliases.rds
/usr/lib64/R/library/mvtnorm/help/mvtnorm.rdb
/usr/lib64/R/library/mvtnorm/help/mvtnorm.rdx
/usr/lib64/R/library/mvtnorm/help/paths.rds
/usr/lib64/R/library/mvtnorm/html/00Index.html
/usr/lib64/R/library/mvtnorm/html/R.css
/usr/lib64/R/library/mvtnorm/include/mvtnorm.h
/usr/lib64/R/library/mvtnorm/include/mvtnormAPI.h
/usr/lib64/R/library/mvtnorm/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/mvtnorm/libs/mvtnorm.so
