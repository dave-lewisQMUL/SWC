#Reads events and creates histograms of dimuon masses

import ROOT as r

if __name__=='__main__':
    print "Creating histograms..."
    data_file = r.TFile("/users/lewis/GitFiles/SWC/day2/data/events.root")

