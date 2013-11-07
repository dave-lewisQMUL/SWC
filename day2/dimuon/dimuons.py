#Reads events and creates histograms of dimuon masses

import ROOT as r

if __name__=='__main__':
    print "Creating histograms..."
    data_file = r.TFile("/users/lewis/GitFiles/SWC/day2/data/events.root")
    tree_ = data_file.Get("events")
    tree_.Print()
    n_events = tree_.GetEntries()
    for i in xrange(n_events):
        tree_.GetEntry(i)
        n_particles = tree_.nPart
        
        
