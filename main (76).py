class Horse:
    def __init__(self, name, age, breed, height, weight, medical_notes=None, behavioral_notes=None):
        self.name = name
        self.age = age
        self.breed = breed
        self.height = height
        self.weight = weight
        self.medical_notes = medical_notes or []
        self.behavioral_notes = behavioral_notes or []
        self.is_available = True
        self.rider = None
        self.schedule = []

    def add_medical_notes(self, notes):
        self.medical_notes.append(notes)

    def add_behavioral_notes(self, notes):
        self.behavioral_notes.append(notes)

    def assign_rider(self, rider):
        if self.is_available:
            self.rider = rider
            self.is_available = False
        else:
            print("This horse is already assigned to a rider.")

    def unassign_rider(self):
        if not self.is_available:
            self.rider = None
            self.is_available = True
        else:
            print("This horse is already available.")

    def add_to_schedule(self, event):
        self.schedule.append(event)

    def remove_from_schedule(self, event):
        if event in self.schedule:
            self.schedule.remove(event)
        else:
            print("This event is not on the schedule.")
