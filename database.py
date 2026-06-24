import json
import os

class ActivityLog:
    def __init__(self, timestamp, log_type, distance=0.0, avg_hr=0, duration=0, urge_count=0, pulse_checked=True, note=""):
        self.timestamp = timestamp      
        self.log_type = log_type        
        self.distance = float(distance)        
        self.avg_hr = int(avg_hr)            
        self.duration = int(duration)        
        self.urge_count = int(urge_count)    
        self.pulse_checked = bool(pulse_checked) 
        self.note = note                

    def to_dict(self):
        return self.__dict__

class DatabaseEngine:
    def __init__(self, db_filename="dopamine_db_v2.json"):
        self.db_filename = db_filename
        self.logs = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.db_filename):
            with open(self.db_filename, "r", encoding="utf-8") as f:
                try:
                    raw_data = json.load(f)
                    self.logs = [ActivityLog(**item) for item in raw_data]
                    self.logs.sort(key=lambda x: x.timestamp, reverse=True)
                except:
                    self.logs = []
        else:
            self.logs = []

    def save_data(self):
        serialized_data = [log.to_dict() for log in self.logs]
        with open(self.db_filename, "w", encoding="utf-8") as f:
            json.dump(serialized_data, f, indent=4, ensure_ascii=False)
