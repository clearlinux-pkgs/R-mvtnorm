#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v2
# autospec commit: e661f3a
#
Name     : R-mvtnorm
Version  : 1.2.4
Release  : 105
URL      : https://cran.r-project.org/src/contrib/mvtnorm_1.2-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mvtnorm_1.2-4.tar.gz
Summary  : Multivariate Normal and t Distributions
Group    : Development/Tools
License  : GPL-2.0
Requires: R-mvtnorm-lib = %{version}-%{release}
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
and densities. Log-likelihoods for multivariate Gaussian models and Gaussian copulae 
  parameterised by Cholesky factors of covariance or precision matrices are implemented 
  for interval-censored and exact data, or a mix thereof. Score functions for these 
  log-likelihoods are available. A class representing multiple lower triangular matrices 
  and corresponding methods are part of this package.

%package lib
Summary: lib components for the R-mvtnorm package.
Group: Libraries

%description lib
lib components for the R-mvtnorm package.


%prep
%setup -q -n mvtnorm
pushd ..
cp -a mvtnorm buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1701117163

%install
export SOURCE_DATE_EPOCH=1701117163
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/mvtnorm/Meta/features.rds
/usr/lib64/R/library/mvtnorm/Meta/hsearch.rds
/usr/lib64/R/library/mvtnorm/Meta/links.rds
/usr/lib64/R/library/mvtnorm/Meta/nsInfo.rds
/usr/lib64/R/library/mvtnorm/Meta/package.rds
/usr/lib64/R/library/mvtnorm/Meta/vignette.rds
/usr/lib64/R/library/mvtnorm/NAMESPACE
/usr/lib64/R/library/mvtnorm/NEWS.Rd
/usr/lib64/R/library/mvtnorm/NEWS.old
/usr/lib64/R/library/mvtnorm/R/mvtnorm
/usr/lib64/R/library/mvtnorm/R/mvtnorm.rdb
/usr/lib64/R/library/mvtnorm/R/mvtnorm.rdx
/usr/lib64/R/library/mvtnorm/doc/MVT_Rnews.R
/usr/lib64/R/library/mvtnorm/doc/MVT_Rnews.Rnw
/usr/lib64/R/library/mvtnorm/doc/MVT_Rnews.pdf
/usr/lib64/R/library/mvtnorm/doc/index.html
/usr/lib64/R/library/mvtnorm/doc/lmvnorm_src.R
/usr/lib64/R/library/mvtnorm/doc/lmvnorm_src.Rnw
/usr/lib64/R/library/mvtnorm/doc/lmvnorm_src.pdf
/usr/lib64/R/library/mvtnorm/help/AnIndex
/usr/lib64/R/library/mvtnorm/help/aliases.rds
/usr/lib64/R/library/mvtnorm/help/mvtnorm.rdb
/usr/lib64/R/library/mvtnorm/help/mvtnorm.rdx
/usr/lib64/R/library/mvtnorm/help/paths.rds
/usr/lib64/R/library/mvtnorm/html/00Index.html
/usr/lib64/R/library/mvtnorm/html/R.css
/usr/lib64/R/library/mvtnorm/include/mvtnorm.h
/usr/lib64/R/library/mvtnorm/include/mvtnormAPI.h
/usr/lib64/R/library/mvtnorm/litdb.bib
/usr/lib64/R/library/mvtnorm/tests/Examples/mvtnorma-Ex.Rout.save
/usr/lib64/R/library/mvtnorm/tests/bugfix-tests.R
/usr/lib64/R/library/mvtnorm/tests/bugfix-tests.Rout.save
/usr/lib64/R/library/mvtnorm/tests/dmvnorm-Ex.R
/usr/lib64/R/library/mvtnorm/tests/plmvnorm-Ex.R
/usr/lib64/R/library/mvtnorm/tests/plmvnorm-Ex.Rout.save
/usr/lib64/R/library/mvtnorm/tests/regtest-TVPACK.R
/usr/lib64/R/library/mvtnorm/tests/regtest-TVPACK.Rout.save
/usr/lib64/R/library/mvtnorm/tests/regtest-scores.R
/usr/lib64/R/library/mvtnorm/tests/regtest-scores.Rout.save
/usr/lib64/R/library/mvtnorm/tests/rmvnorm.R
/usr/lib64/R/library/mvtnorm/tests/slpmvnorm.R
/usr/lib64/R/library/mvtnorm/tests/test-getInt.R
/usr/lib64/R/library/mvtnorm/tests/test-noisy-root.R
/usr/lib64/R/library/mvtnorm/tests/test-noisy-root.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/mvtnorm/libs/mvtnorm.so
/usr/lib64/R/library/mvtnorm/libs/mvtnorm.so.avx2
/usr/lib64/R/library/mvtnorm/libs/mvtnorm.so.avx512
