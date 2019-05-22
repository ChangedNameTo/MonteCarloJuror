import random

JURY_SIZE = 108

class JuryList():
    jurors_w_duplicates = []
    jurors_wo_duplicates = []

    # Creates a Franklin County jury listing
    def __init__(self):
        # White non duplicates
        for x in range(4127):
            self.jurors_w_duplicates.append(JuryMember('White', False))
            self.jurors_wo_duplicates.append(JuryMember('White', False))

        # White duplicates
        for x in range(1059):
            self.jurors_w_duplicates.append(JuryMember('White', True))

        # Black non duplicates
        for x in range(405):
            self.jurors_w_duplicates.append(JuryMember('Black', False))
            self.jurors_wo_duplicates.append(JuryMember('Black', False))

        # Black duplicates
        for x in range(55):
            self.jurors_w_duplicates.append(JuryMember('Black', True))

        # Other non duplicates
        for x in range(46):
            self.jurors_w_duplicates.append(JuryMember('Other', False))
            self.jurors_wo_duplicates.append(JuryMember('Other', False))

        # Other duplicates
        for x in range(3):
            self.jurors_w_duplicates.append(JuryMember('Other', True))

    # Takes the jury list and generates a random jury.
    def create_jury(self, duplicates=False):
        if duplicates:
            return random.sample(self.jurors_w_duplicates, JURY_SIZE)
        return random.sample(self.jurors_wo_duplicates, JURY_SIZE)

    def race_count(self, jury_list):
        race_dict = {'White':0, 'Black':0, 'Other':0}

        for juror in jury_list:
            race_dict[juror.race] = race_dict[juror.race] + 1

        return race_dict


class JuryMember():
    race      = ''
    duplicate = ''

    def __init__(self, race='White', duplicate=False):
        self.race      = race
        self.duplicate = duplicate

    def race(self):
        return self.race

    def is_duplicate(self):
        return self.duplicate