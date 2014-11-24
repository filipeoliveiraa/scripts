#!/usr/bin/perl -w
my $infilename = $ARGV[0];
my $basevar = $ARGV[1];

my $pickatrandom = 1;
if (($ARGV[2]) && ($ARGV[2] eq "all"))
{
    $pickatrandom = 0;
}

# Seed the output file
my $outfilename = "/tmp/pyro.txt";
open(OUTFILE, "> $outfilename")
    or die "Couldn't open $outfilename for writing: $!\n";
print OUTFILE $basevar;
close(OUTFILE);

local $/;
undef $/;

open(INFILE, $infilename)
    or die "Couldn't open $infilename for reading: $!\n";
$infilecontents = <INFILE>; 
close(INFILE);

open(OUTFILE, "< $outfilename")
    or die "Couldn't open $outfilename for reading: $!\n";
$outfilecontents = <OUTFILE>;
close(OUTFILE);

while ($outfilecontents =~ /\@[A-Za-z0-9]+\@/)
{
    local $/;
    undef $/;

    open(OUTFILE, "< $outfilename")
        or die "Couldn't open $outfilename for reading: $!\n";
    $outfilecontents = <OUTFILE>;
    close(OUTFILE);

    # $baseline is the first line in OUTFILE with a variable.

    if ($outfilecontents =~ /^(.*?)(\@\w+\@)(.*?)$/m)
    {
        $baseline = "$1$2$3";
        $varname=$2;
    }
    chomp $varname;

    if ($infilecontents =~ /\#$varname\n(.*?)\n\n/s)
    {
        $varblock = "$1\n";
    }
    else
    {
        die "Did not find variable $varname in $infilename.\n";
    }

    @varblockarr = split (/\n/, $varblock);
    @outlinesarr = ();
 
    if ($pickatrandom)
    {
        # Generate a random string from the input elements
        $randline = $varblockarr [ rand @varblockarr ];
        $curline = $baseline;
        chomp ($curline);
        chomp ($randline);
        $curline =~ s/$varname/$randline/;
        push (@outlinesarr, $curline);
    }
    else
    {
        # Generate all possible combinations of the input elements
        foreach $varline (@varblockarr)
        {
            $curline = $baseline;
            chomp ($curline);
            chomp ($varline);
            $curline =~ s/$varname/$varline/;
            push (@outlinesarr, $curline);
        }
    }

    $outlines = join ("\n", @outlinesarr);
    $outfilecontents =~ s/\Q$baseline\E/$outlines/s
        or die "baseline not found.\n";
    $outfilecontents =~ s/\n\n/\n/mg;
    open(OUTFILE, "> $outfilename")
        or die "Couldn't open $outfilename for writing: $!\n";
    print OUTFILE $outfilecontents;
    close(OUTFILE);
}

if ($pickatrandom)
{
    print $outfilecontents;
}
