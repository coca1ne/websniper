class showprints:
    def __init__(self):
        pass
    
    def out(self, output=""):
        print output
        return
    
    def prompt(self):
        return "websniper>"

    def listmodsdesc(self, shopt):
        if  shopt == 'modules':
            print ""
            print "Modules"
            print "------------------------------------"
            print ""
            print ' Command                                     Author                   Description'
            print ""
            print ' modules/recon/httpheaderanalyzer            httphacker               Checks for vulnerability on http header response'
            print ' modules/recon/subdomainfinder               shipcode                 Harvest domain from the target'
            print ' modules/vulnerability/dnsmisconfig          shipcode                 Check if target is vulnerable to DNS misconfiguration'
            print ' modules/discovery/vhostfinder               m1xr4t                   Enumerates vhosts on specified target'
            print ' modules/recon/shodanlookup                  shipcode                 Shodan Host Lookup'
            print ' modules/recon/metaextractor                 semprix                  Extracts httpmeta data from the target application'
            print ""

        elif shopt == 'exploits':
            print ""
            print "Exploits"
            print "------------------------------------"
            print ""
            print ' Command                                     Author                   Description'
            print ' modules/exploits/whmcs                      shipcode                 Exploits the local file disclosure vulnerability of WHMCS version 3.x.x'
            print ' modules/exploits/shellshock                 shipcode                 Checks if the cgi-bin of the target is vulnerable to Shellshock'
            print ""

        elif shopt == 'payloads':
            print ""
            print "Payloads"
            print "------------------------------------"
            print ""
            print ' Name                                     Added by                 Description'
            print ' payloads/backup_files                    shipcode                 Name list of backup files'
            print ' payloads/lfi                             shipcode                 Local file inclusion'
            print ""

        else:
            print ""
            print "Show options:"
            print "modules, exploits, payloads\n"

    def listmods(self):
            print ""
            print "Modules"
            print "------------------------------------"
            print ""
            print ' Command                                     Author                   Description'
            print ""
            print ' modules/recon/httpheaderanalyzer            httphacker               Checks for vulnerability on http header response'
            print ' modules/recon/subdomainfinder               shipcode                 Harvest domain from the target'
            print ' modules/vulnerability/dnsmisconfig          shipcode                 Check if target is vulnerable to DNS misconfiguration'
            print ' modules/discovery/vhostfinder               m1xr4t                   Enumerates vhosts on specified target'
            print ' modules/recon/shodanlookup                  shipcode                 Shodan Host Lookup'
            print ' modules/recon/metaextractor                 semprix                  Extracts httpmeta data from the target application'
            print ""
