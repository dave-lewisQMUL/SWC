#Reads events and creates histograms of dimuon masses

import ROOT as r

def tree_from_file(file_):
    global data_file
    data_file = r.TFile(file_)
    return data_file.Get("events")

if __name__=='__main__':
    print "Creating histograms..."
    file_ = "/users/lewis/GitFiles/SWC/day2/data/events.root"
    tree_ = tree_from_file(file_)
    tree_.Print()
    n_events = tree_.GetEntries()
    for i in xrange(n_events):
        tree_.GetEntry(i)
        n_particles = tree_.nPart
        
        
