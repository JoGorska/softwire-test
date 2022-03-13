class MusicianFactory(object):
    '''
    creates a Musician, returns the created Musician
    '''
    # Creates a Musician
    # returns the created Musician
    def __init__(self, Musician):
        self.Musician = Musician

    def create_musician(self):
        '''
        creates a Musician, returns the created Musician
        '''
        return Musician


class Instrument:
    '''
    creates a Instrument, returns the created Instrument
    '''
    def __init__(self, sound):
    self.sound = sound

    def play(self, sound):
        '''
        when instrument plays it makes a sound
        '''
        return sound


class DrummerFactory(MusicianFactory):
    '''
    creates a Drummer, returns the created Drumer
    '''
    def __init__(self, Musician, Drum):
        self.Drum = Drum
        super().__init__(Musician)

    def create_musician_with_a_drum(self):
        '''
        creates a Musician with a Drum
        '''
        return Musician and Drum


class Drum(Instrument):
    '''
    Drum extends the class instrument
    '''
    pass


class Musician:
    '''
    Musician can play instruments
    '''
    def __init__(self, instrument):
        raise Exception('Waiting to be implemented!')

    def play_instrument(self):
        '''
        method on Musician class
        '''
        raise Exception('Waiting to be implemented!')