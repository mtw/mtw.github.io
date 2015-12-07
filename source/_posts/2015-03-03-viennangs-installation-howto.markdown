---
layout: post
title: "ViennaNGS Installation HOWTO"
date: 2015-03-03 11:45:50 +0100
comments: true
categories: ViennaNGS
---
[ViennaNGS](http://search.cpan.org/dist/Bio-ViennaNGS) is a Perl distribution
for rapid development of next-generation sequencing analysis pipelines. It comes
with a set of modules and [Moose-based](http://moose.iinteractive.com/en/)
classes for accomplishing standard and non-standard tasks in NGS processing.
ViennaNGS' feature-richness, however, comes at some cost: dependencies on third
party Perl modules and external tools and libraries, which can be tedious to
install. I have therefore compiled this little __ViennaNGS Installation HOWTO__
to help prospective users getting the software up and running quickly on their
systems.  

Let's get started. The installation process provided here has been prepared for
Linux systems, however the steps should be reproducible on MacOS X given that
you have the common GNU tools and  Perl 5.10.0 or higher available, e.g. via
[MacPorts](https://www.macports.org).

### First things first: third party dependencies

*ViennaNGS* depends on set of third party bioinf tools and libraries, which are
required either for specific filtering and file format conversion tasks or for
building internally used Perl modules. Before continuing with the *ViennaNGS*
installation, you will need to download and install the following software and
ensure that all executables are accessible to the Perl interpreter:

* A recent version of [bedtools2](https://github.com/arq5x/bedtools2) (latest version as of writing was v2.23)
* The *bedGraphToBigWig* and *fetchChromSizes* [UCSC Genome Browser application binaries](http://hgdownload.cse.ucsc.edu/admin/exe/)
* The [R Statistics Package](http://www.r-project.org/)  
* [samtools <= v0.1.19](https://github.com/samtools/samtools/releases/tag/0.1.19). More recent HTSlib-based versions will **not work** with [Bio::DB::Sam](http://search.cpan.org/~lds/Bio-SamTools/lib/Bio/DB/Sam.pm)

The last dependency is in fact a bit peculiar. *Bio::DB::Sam* up to version
1.41, which we use for all kind of direct BAM manipulation within *ViennaNGS*,
for some reason will not compile with recent, HTSlib-based versions of
*samtools*. *samtools 0.1.19* seems to be the last version that is compatible
with current versions of *Bio::DB::Sam*. So let's download *samtools 0.1.19* to
a local folder, say `/scratch/software`, uncompress the tarball and compile the
samtools library:
```
mkdir -p /scratch/software
cd /scratch/software
wget https://github.com/samtools/samtools/archive/0.1.19.tar.gz
tar xvf 0.1.19.tar.gz
cd samtools-0.1.19
make CFLAGS="-g -O2 -Wall -Wno-unused -Wno-unused-result -fPIC"
```
The extra `-Wno*` CFLAGS options prevent some unused variable warnings with
recent versions of *gcc*, whereas the `-fPIC` CFLAGS option prohibits a
relocation error on x64_64 architectures (see also the [Bio::DB::Sam
README](http://cpansearch.perl.org/src/LDS/Bio-SamTools-1.41/README)). If
everything works out fine,  *samtools* is now compiled, and a static library
file `libbam.a` will be created in the current working directory. Remember the
absolute path to `libbabm.a` (in our example this is
`/scratch/software/samtools-0.1.19`), since we will need this later for
compiling *Bio::DB::Sam*.

### Setting up a local Perl module directory with cpanminus

Once all thrid-party dependencies are installed, we can now focus on the Perl
dependencies of *ViennaNGS*, e.g. the *BioPerl* suite, the *Moose* object
framework and many more. Fortunately, installation of custom Perl modules (i.e.
those that are not considered Perl core modules or shipped with a Linux
distribution) is a fairly trivial task these days, thanks to a tool called
[cpanminus](https://cpanmin.us). *cpanminus* renders installation of a custom
Perl module as easy as typing `cpanm` and the module's name on the command line.
Moreover, it provides automatic dependency resolution, which comes in handy when
you're installing Perl modules or distributions that depend on other modules,
which again depend on a bunch of modules etc. Forget about the *CPAN shell* or
*cpanplus*, use *cpanminus*.

Before starting with *cpanminus* we'll need to set a few environment variables
that tell *cpanm* and the Perl interpreter where to keep and look for locally
installed Perl modules. We'll keep up with the *cpanminus* default location,
`${HOME}/perl5` and add the following lines to the end of `.bashrc`:
```
export PERL_MM_OPT="INSTALL_BASE=${HOME}/perl5"
export PERL_MB_OPT="--install_base ${HOME}/perl5"
export PERL5LIB=${HOME}/perl5/lib/perl5:${PERL5LIB}
```
We will also modify our `PATH` variable to include `${HOME}/perl5/bin`, where
executable scripts that are shipped with custom Perl modules will be installed:
```
export PATH=${HOME}/perl5/bin:${PATH}
```
We can now install *cpanminus*, either the version shipped with our Linux
distribution (example given for Debian/Ubuntu must be executed with root
privileges)
```
apt-get install cpanminus
```
or directly from https://cpanmin.us
```
curl -L https://cpanmin.us | perl - App::cpanminus
```

### Installing the ViennaNGS Perl dependencies

After all we are now ready to install the *ViennaNGS* Perl dependencies. Let's start with *Bio::DB::Sam*
```
cpanm Bio::DB::Sam
```
Depending on your system setup, *cpanm* will now start to download and install
all dependencies of *Bio::DB::Sam* and will then ask for the location of the
static `libbam.a` library:
```
Configuring Bio-SamTools-1.41 ... Please enter the location of the bam.h and compiled libbam.a files:
```
Our *samtools* folder is `/scratch/software/samtools-0.1.19` (see above), so let's enter this here:
```
/scratch/software/samtools-0.1.19
```
This was basically the only module that we had to install manually due to the
*samtools* location constraint. Actually, we could have installed
*Bio::ViennaNGS* directly and *cpanm* would have asked for the *samtools*
location, but I thought this was a good chance to demonstrate *cpanm* usage for
didactic reasons.

### Installing Bio::ViennaNGS

Here comes the easiest part. Since we've got `cpanm` up and running on our
system, all we need to type is
```
cpanm Bio::ViennaNGS
```
and wait for *cpanm* to install all dependencies and finish. Beware that
*ViennaNGS* depends on
[Statistics::R](http://search.cpan.org/~fangly/Statistics-R/lib/Statistics/R.pm),
which requires a running installation of the [R Statistics
Package](http://www.r-project.org/) on your system. If for any reason *cpanm*
fails (e.g. R is not available), it will stop and report an error. You can then
install the missing component and call the above command again. Moreover,
whenever there is a new *ViennaNGS* release available on CPAN, just type `cpanm
Bio::ViennaNGS` and you'll get the latest version in just a couple of seconds.

Congratulations! You now have a running installation of *Bio::ViennaNGS*. If you
sticked with the paths in our example, the modules/classes are located in
`${HOME}/perl5/lib/perl5/Bio/ViennaNGS/lib` and the *ViennaNGS utilities* can be
found in `${HOME}/perl5/bin`.

The *ViennaNGS* authors are looking forward to getting your feedback. Please use
the [ViennaNGS GitHub Issue
Tracker](https://github.com/mtw/Bio-ViennaNGS/issues) for reporting bugs.
