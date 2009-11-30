# ---+ Extensions
# ---++ GenPDFAddOn
# **PATH M**
# htmldoc executable including complete path.
$Foswiki::cfg{Extensions}{GenPDFAddOn}{htmldocCmd} = '/usr/bin/htmldoc';
# **PERL H**
# This setting is required to enable executing genpdf script from the bin directory
$Foswiki::cfg{SwitchBoard}{genpdf} = {
    package  => 'Foswiki::Contrib::GenPDF',
    function => 'viewPDF',
    context  => { view => 1 },
    };

1;
