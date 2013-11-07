import dimuons as dm

def test_dummy():
    assert 'a' == 'a'

#def test_dummy2():
#    assert 'a'=='b'

def test_zero_particles():
    particles = []
    pairs = dm.find_pairs(particles)
    assert len(pairs)==0

def test_one_particles():
    particles = [None]
    pairs = dm.find_pairs(particles)
    assert len(pairs)==0

def test_two_particles():
    particles = [1,-1,2,3]
    pairs = dm.find_pairs(particles)
    assert len(pairs)==1
