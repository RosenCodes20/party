class Party:
    def __init__(self):
        self.people = []


party = Party()
lines = input()
while lines != "End":
    party.people.append(lines)
    lines = input()
print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")
