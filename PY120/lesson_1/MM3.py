class Candidate:
    
    def __init__(self, name):
        self.name = name
        self.votes = 0
        
    def __iadd__(self, vote):
        if not isinstance(vote, int):
            return NotImplemented
        
        self.votes += vote
        return self

class Election:
    def __init__(self, candidate_dict):
        self.candidates = candidate_dict

    def results(self):
        total_votes = 0
        max_votes = 0
        winner = None
        for candidate in self.candidates:
            if candidate.votes > max_votes:
                winner = candidate
                max_votes = candidate.votes
            total_votes += candidate.votes
        for candidate in self.candidates:
            print( f'{candidate.name}: {candidate.votes} votes')
        print(f'\n{winner.name} won: {(max_votes/total_votes) *100}% of votes')

mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()