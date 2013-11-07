#Reads events and creates histograms of dimuon masses

import ROOT as r

def tree_from_file(file_):
    global data_file
    data_file = r.TFile(file_)
    return data_file.Get("events")

def mass_hist(tree_):
    return r.TH1F()

def find_pairs(particles):
    pairs = []
    for i in range(0,len(particles)):
        for j in range(i+1,len(particles)):
            if (particle[i].qpt * particle[j].qpt) < 0:
                pairs.append((particles[i],particles[j]))
    return pairs

if __name__=='__main__':
    print "Creating histograms..."
    file_ = "/users/lewis/GitFiles/SWC/day2/data/events.root"
    tree_ = tree_from_file(file_)
    tree_.Print()
    n_events = tree_.GetEntries()
    for i in xrange(n_events):
        tree_.GetEntry(i)
        n_particles = tree_.nPart
    hist_ =  mass_hist(tree_)
    hist_.Draw()
    raw_input("Press enter to exit")
