from match import match
perfect_unison, minor_second, augmented_unison, major_second,\
    diminished_third, minor_third, augmented_second, major_third,\
    diminished_fourth, perfect_fourth, augmented_third, diminished_fifth,\
    augmented_fourth, perfect_fifth, diminished_sixth, minor_sixth,\
    augmented_fifth, major_sixth, diminished_seventh, minor_seventh,\
    augmented_sixth, major_seventh, diminished_octave, perfect_octave,\
    octave, augmented_seventh = 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7,\
    7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 12
INTERVAL = {
    0: ('perfect unison', ),
    1: ('minor second', 'augmented unison'),
    2: ('major second', 'diminished third'),
    3: ('minor third', 'augmented second'),
    4: ('major third', 'diminished fourth'),
    5: ('perfect fourth', 'augmented third'),
    6: ('diminished fifth', 'augmented fourth'),
    7: ('perfect fifth', 'diminished sixth'),
    8: ('minor sixth', 'augmented fifth'),
    9: ('major sixth', 'diminished seventh'),
    10: ('minor seventh', 'augmented sixth'),
    11: ('major seventh', 'diminished octave'),
    12: ('perfect octave', 'octave', 'augmented seventh')
}
NAME_OF_INTERVAL = {
    'perfect unison': 0,
    'minor second': 1,
    'augmented unison': 1,
    'major second': 2,
    'diminished third': 2,
    'minor third': 3,
    'augmented second': 3,
    'major third': 4,
    'diminished fourth': 4,
    'perfect fourth': 5,
    'augmented third': 5,
    'diminished fifth': 6,
    'augmented fourth': 6,
    'perfect fifth': 7,
    'diminished sixth': 7,
    'minor sixth': 8,
    'augmented fifth': 8,
    'major sixth': 9,
    'diminished seventh': 9,
    'minor seventh': 10,
    'augmented sixth': 10,
    'major seventh': 11,
    'diminished octave': 11,
    'perfect octave': 12,
    'octave': 12,
    'augmented seventh': 12
}
standard = {
    'C': 0,
    'C#': 1,
    'D': 2,
    'D#': 3,
    'E': 4,
    'F': 5,
    'F#': 6,
    'G': 7,
    'G#': 8,
    'A': 9,
    'A#': 10,
    'B': 11,
    'Bb': 10,
    'Eb': 3,
    'Ab': 8,
    'Db': 1,
    'Gb': 6
}
standard2 = {
    'C': 0,
    'C#': 1,
    'D': 2,
    'D#': 3,
    'E': 4,
    'F': 5,
    'F#': 6,
    'G': 7,
    'G#': 8,
    'A': 9,
    'A#': 10,
    'B': 11
}
scaleTypes = match({
    ('major', ): [2, 2, 1, 2, 2, 2, 1],
    ('minor', ): [2, 1, 2, 2, 1, 2, 2],
    ('melodic minor', ): [2, 1, 2, 2, 2, 2, 1],
    ('harmonic minor', ): [2, 1, 2, 2, 1, 3, 1],
    ('lydian', ): [2, 2, 2, 1, 2, 2, 1],
    ('dorian', ): [2, 1, 2, 2, 2, 1, 2],
    ('phrygian', ): [1, 2, 2, 2, 1, 2, 2],
    ('mixolydian', ): [2, 2, 1, 2, 2, 1, 2],
    ('locrian', ): [1, 2, 2, 1, 2, 2, 2],
    ('whole tone', ): [2, 2, 2, 2, 2, 2],
    ('12', ): [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
})
modern_modes = [
    'major', 'dorian', 'phrygian', 'lydian', 'mixolydian', 'minor', 'locrian'
]
chordTypes = match({
    ('major', 'M', 'maj', 'majorthird'): ((4, 7), ),
    ('minor', 'm', 'minorthird', 'min'): ((3, 7), ),
    ('maj7', 'M7', 'major7th', 'majorseventh'): ((4, 7, 11), ),
    ('m7', 'min7', 'minor7th', 'minorseventh'): ((3, 7, 10), ),
    ('7', 'seven', 'seventh', 'dominant seventh', 'dom7', 'dominant7', 'germansixth'):
    ((4, 7, 10), ),
    ('minormajor7', 'minor major 7', 'mM7'): ((3, 7, 11), ),
    ('dim', 'dim3', '-'): ((3, 6), ),
    ('dim7', '-7'): ((3, 6, 9), ),
    ('half-diminished7', 'ø7', 'ø', 'half-diminished', 'half-dim', 'o7', 'o', 'm7b5'):
    ((3, 6, 10), ),
    ('aug', 'augmented', '+', 'aug3', '+3'): ((4, 8), ),
    ('aug7', 'augmented7', '+7'): ((4, 8, 10), ),
    ('augmaj7', 'augmented-major7', '+maj7'): ((4, 8, 11), ),
    ('aug6', 'augmented6', '+6', 'italian-sixth'): ((4, 10), ),
    ('frenchsixth', ): ((4, 6, 10), ),
    ('aug9', '+9'): ((4, 8, 10, 14), ),
    ('augmaj9', '+maj9'): ((4, 8, 11, 14), ),
    ('sus', 'sus4'): ((5, 7), ),
    ('sus2', ): ((2, 7), ),
    ('9', 'dominant9', 'dominant-ninth', 'ninth'): ((4, 7, 10, 14), ),
    ('maj9', 'major-ninth', 'major9th'): ((4, 7, 11, 14), ),
    ('m9', 'minor9', 'minor9th'): ((3, 7, 10, 14), ),
    ('add6', '6', 'sixth'): ((4, 7, 9), ),
    ('m6', 'minorsixth'): ((3, 7, 9), ),
    ('add2', '+2'): ((2, 4, 7), ),
    ('add9', '+9'): ((4, 7, 14), ),
    ('madd2', 'm+2'): ((2, 3, 7), ),
    ('madd9', 'm+9'): ((3, 7, 14), ),
    ('7sus4', '7sus'): ((5, 7, 10), ),
    ('7sus2', ): ((2, 7, 10), ),
    ('maj7sus4', 'maj7sus', 'M7sus4'): ((5, 7, 11), ),
    ('maj7sus2', 'M7sus2'): ((2, 7, 11), ),
    ('9sus4', '9sus'): ((5, 7, 10, 14), ),
    ('9sus2', ): ((2, 7, 10, 14), ),
    ('maj9sus4', 'maj9sus'): ((5, 7, 11, 14), ),
    ('13sus4', '13sus'): ((5, 7, 10, 14, 21), (7, 10, 14, 17, 21)),
    ('13sus2', ): ((2, 7, 10, 17, 21),),
    ('maj13sus4', 'maj13sus'): ((5, 7, 11, 14, 21), (7, 11, 14, 17, 21)),
    ('maj13sus2', ): ((2, 7, 11, 17, 21), ),
    ('add4', '+4'): ((4, 5, 7), ),
    ('madd4', 'm+4'): ((3, 5, 7), ),
    ('add24', '24', 'sus2sus4'): ((2, 5), ),
    ('add2omit5', ): ((2, 4), ),
    ('madd2omit5', ): ((2, 3), ),
    ('maj7#11', ): ((4, 7, 11, 18), ),
    ('m7#11', ): ((3, 7, 10, 18), ),
    ('7#11', ): ((4, 7, 10, 18), ),
    ('maj9#11', ): ((4, 7, 11, 14, 18), ),
    ('m9#11', ): ((3, 7, 10, 14, 18), ),
    ('9#11', ): ((4, 7, 10, 14, 18), ),
    ('69', '6/9', 'add69'): ((4, 7, 9, 14), ),
    ('m69', 'madd69'): ((3, 7, 9, 14), ),
    ('6sus4', '6sus'): ((5, 7, 9), ),
    ('6sus2', ): ((2, 7, 9), ),
    ('5', 'power chord'): ((7, ), ),
    ('5(+octave)', 'power chord(with octave)'): ((7, 12), ),
    ('11', 'M11', 'maj11', 'eleventh', 'major 11', 'major eleventh'):
    ((4, 7, 11, 14, 17), ),
    ('m11', 'minor eleventh', 'minor 11'): ((3, 7, 10, 14, 17), ),
    ('dominant11', 'dominant eleventh'): ((4, 7, 10, 14, 17), ),
    ('13', 'dominant 13'): ((4, 7, 10, 14, 17, 21), ),
    ('maj13', 'major 13'): ((4, 7, 11, 14, 17, 21), ),
    ('m13', 'minor 13'): ((3, 7, 10, 14, 17, 21), ),
    ('maj7add13', ): ((4, 7, 11, 21), ),
    ('maj7#13', ): ((4, 7, 11, 14, 22), ),
    ('maj13#11', ): ((4, 7, 11, 14, 18, 21), ),
    ('13#11', ): ((4, 7, 10, 14, 18, 21), ),
    ('m13#11', ): ((3, 7, 10, 14, 18, 21), ),
    ('fifth 9th', ): ((7, 14), ),
    ('minormajor9', 'minor major 9', 'mM9'): ((3, 7, 11, 14), )
})
standard_reverse = {j: i for i, j in standard2.items()}
detectScale = scaleTypes.reverse()
detectTypes = chordTypes.reverse()
notedict = {
    'C': 'C',
    'c': 'C#',
    'D': 'D',
    'd': 'D#',
    'E': 'E',
    'F': 'F',
    'f': 'F#',
    'G': 'G',
    'g': 'G#',
    'A': 'A',
    'a': 'A#',
    'B': 'B',
    ' ': 'interval'
}

instruments = {
    'Acoustic Grand Piano': 1,
    'Bright Acoustic Piano': 2,
    'Electric Grand Piano': 3,
    'Honky-tonk Piano': 4,
    'Electric Piano 1': 5,
    'Electric Piano 2': 6,
    'Harpsichord': 7,
    'Clavi': 8,
    'Celesta': 9,
    'Glockenspiel': 10,
    'Music Box': 11,
    'Vibraphone': 12,
    'Marimba': 13,
    'Xylophone': 14,
    'Tubular Bells': 15,
    'Dulcimer': 16,
    'Drawbar Organ': 17,
    'Percussive Organ': 18,
    'Rock Organ': 19,
    'Church Organ': 20,
    'Reed Organ': 21,
    'Accordion': 22,
    'Harmonica': 23,
    'Tango Accordion': 24,
    'Acoustic Guitar (nylon)': 25,
    'Acoustic Guitar (steel)': 26,
    'Electric Guitar (jazz)': 27,
    'Electric Guitar (clean)': 28,
    'Electric Guitar (muted)': 29,
    'Overdriven Guitar': 30,
    'Distortion Guitar': 31,
    'Guitar harmonics': 32,
    'Acoustic Bass': 33,
    'Electric Bass (finger)': 34,
    'Electric Bass (pick)': 35,
    'Fretless Bass': 36,
    'Slap Bass 1': 37,
    'Slap Bass 2': 38,
    'Synth Bass 1': 39,
    'Synth Bass 2': 40,
    'Violin': 41,
    'Viola': 42,
    'Cello': 43,
    'Contrabass': 44,
    'Tremolo Strings': 45,
    'Pizzicato Strings': 46,
    'Orchestral Harp': 47,
    'Timpani': 48,
    'String Ensemble 1': 49,
    'String Ensemble 2': 50,
    'SynthStrings 1': 51,
    'SynthStrings 2': 52,
    'Choir Aahs': 53,
    'Voice Oohs': 54,
    'Synth Voice': 55,
    'Orchestra Hit': 56,
    'Trumpet': 57,
    'Trombone': 58,
    'Tuba': 59,
    'Muted Trumpet': 60,
    'French Horn': 61,
    'Brass Section': 62,
    'SynthBrass 1': 63,
    'SynthBrass 2': 64,
    'Soprano Sax': 65,
    'Alto Sax': 66,
    'Tenor Sax': 67,
    'Baritone Sax': 68,
    'Oboe': 69,
    'English Horn': 70,
    'Bassoon': 71,
    'Clarinet': 72,
    'Piccolo': 73,
    'Flute': 74,
    'Recorder': 75,
    'Pan Flute': 76,
    'Blown Bottle': 77,
    'Shakuhachi': 78,
    'Whistle': 79,
    'Ocarina': 80,
    'Lead 1 (square)': 81,
    'Lead 2 (sawtooth)': 82,
    'Lead 3 (calliope)': 83,
    'Lead 4 (chiff)': 84,
    'Lead 5 (charang)': 85,
    'Lead 6 (voice)': 86,
    'Lead 7 (fifths)': 87,
    'Lead 8 (bass + lead)': 88,
    'Pad 1 (new age)': 89,
    'Pad 2 (warm)': 90,
    'Pad 3 (polysynth)': 91,
    'Pad 4 (choir)': 92,
    'Pad 5 (bowed)': 93,
    'Pad 6 (metallic)': 94,
    'Pad 7 (halo)': 95,
    'Pad 8 (sweep)': 96,
    'FX 1 (rain)': 97,
    'FX 2 (soundtrack)': 98,
    'FX 3 (crystal)': 99,
    'FX 4 (atmosphere)': 100,
    'FX 5 (brightness)': 101,
    'FX 6 (goblins)': 102,
    'FX 7 (echoes)': 103,
    'FX 8 (sci-fi)': 104,
    'Sitar': 105,
    'Banjo': 106,
    'Shamisen': 107,
    'Koto': 108,
    'Kalimba': 109,
    'Bag pipe': 110,
    'Fiddle': 111,
    'Shanai': 112,
    'Tinkle Bell': 113,
    'Agogo': 114,
    'Steel Drums': 115,
    'Woodblock': 116,
    'Taiko Drum': 117,
    'Melodic Tom': 118,
    'Synth Drum': 119,
    'Reverse Cymbal': 120,
    'Guitar Fret Noise': 121,
    'Breath Noise': 122,
    'Seashore': 123,
    'Bird Tweet': 124,
    'Telephone Ring': 125,
    'Helicopter': 126,
    'Applause': 127,
    'Gunshot': 128
}
