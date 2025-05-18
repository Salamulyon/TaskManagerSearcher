import csv
import time
import os



class CsvManager:
    def __init__(self):
        pass

    def _create_path(self,file_path: str):
        """
        
        """
        if not file_path:
            # Get the user's desktop path
            self.file_path = os.path.join(os.path.expanduser("~"), "Desktop")
        else:
            self.file_path = file_path

    def get_curr_time(self):
        self.curr_time = time.ctime(time.time)

    def write_to_csv(self,data: dict,file_path: str = ""):
        self._create_path(file_path)
        self.get_curr_time()
        with open(f"{self.file_path}_TaskMgr_{self.curr_time}",'w') as csv_file:
            fieldnames = ["TaskName","Task Duties"]
            writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
            writer.writeheader()
            for key,value in data.items():
                writer.writerow({fieldnames[0]:key,
                                 fieldnames[1]:value})

