# ---+ Extensions
# ---++ GenPDFAddOn
# **PATH M**
# Path to the htmldoc executable.
$Foswiki::cfg{Extensions}{GenPDFAddOn}{htmldocCmd} = '/path/to/htmldoc/bin/htmldoc';
# **PERL H**
# This setting is required to enable executing genpdf script from the bin directory
$Foswiki::cfg{SwitchBoard}{genpdf} =  [ 'Foswiki::Contrib::GenPDF', 'viewPDF' ]; 
1;
