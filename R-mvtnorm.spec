#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mvtnorm
Version  : 1.1.3
Release  : 96
URL      : https://cran.r-project.org/src/contrib/mvtnorm_1.1-3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mvtnorm_1.1-3.tar.gz
Summary  : Multivariate Normal and t Distributions
Group    : Development/Tools
License  : GPL-2.0
Requires: R-mvtnorm-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
random deviates and densities.

%package lib
Summary: lib components for the R-mvtnorm package.
Group: Libraries

%description lib
lib components for the R-mvtnorm package.


%prep
%setup -q -c -n mvtnorm
cd %{_builddir}/mvtnorm

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641065466

%install
export SOURCE_DATE_EPOCH=1641065466
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mvtnorm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mvtnorm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mvtnorm
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc mvtnorm || :


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
/usr/lib64/R/library/mvtnorm/tests/Examples/mvtnorma-Ex.Rout.save
/usr/lib64/R/library/mvtnorm/tests/bugfix-tests.R
/usr/lib64/R/library/mvtnorm/tests/bugfix-tests.Rout.save
/usr/lib64/R/library/mvtnorm/tests/regtest-TVPACK.R
/usr/lib64/R/library/mvtnorm/tests/regtest-TVPACK.Rout.save
/usr/lib64/R/library/mvtnorm/tests/rmvnorm.R
/usr/lib64/R/library/mvtnorm/tests/test-getInt.R
/usr/lib64/R/library/mvtnorm/tests/test-noisy-root.R
/usr/lib64/R/library/mvtnorm/tests/test-noisy-root.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/mvtnorm/libs/mvtnorm.so
/usr/lib64/R/library/mvtnorm/libs/mvtnorm.so.avx2
/usr/lib64/R/library/mvtnorm/libs/mvtnorm.so.avx512
