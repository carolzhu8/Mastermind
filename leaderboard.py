class Leaderboard:
    """
    Leaderboard class is used to read and write the leaderboard
    """
    def __init__(self, file_name):
        """
         FUNCTION - __init__()
         This function is the constructor。

         PARAMETERS:
         file_name -- a string

         RETURNS:
         None
         """
        self.file_name = file_name
        self.if_file_exist = self.check_file_existence()  # wanna know if file exits at the begining

    def check_file_existence(self):
        """
        FUNCTION - check_file_existence()
        This function is check if file exists.

        PARAMETERS:
        None

        RETURNS:
        A boolean
        """
        try:
            with open(self.file_name, mode="r", encoding="utf-8"):
                return True
        except FileNotFoundError:
            return False

    def read_file(self):
        """
        FUNCTION - read_file()
        This function is read the leader board file

        PARAMETERS:
        None

        RETURNS:
        A nested list of leaderboard.
        """
        output = []
        if self.if_file_exist:
            with open(self.file_name, mode="r", encoding="utf-8") as file:
                content = file.read()
                lines = content.split("\n")
                for line in lines:
                    line_split = line.split(":")
                    score = line_split[0]
                    name = line_split[1]
                    output.append([score, name])
                return output
        else:
            return output

    def write_file(self, leaderboard_list):
        """
        FUNCTION - write_file()
        This function is write leader board into the file

        PARAMETERS:
        None

        RETURNS:
        None
        """
        sorted_list = self.sort_leaderboard_list(leaderboard_list)
        for i in range(len(sorted_list)):
            sorted_list[i][0] = str(sorted_list[i][0])
            sorted_list[i] = ":".join(sorted_list[i])
        content = "\n".join(sorted_list)
        with open(self.file_name, mode="w", encoding="utf-8") as file:
            file.write(content)

    def sort_leaderboard_list(self, leaderboard_list):
        """
        FUNCTION - write_file()
        This function is sort the leaderboard_list

        PARAMETERS:
        leaderboard_list - a nested list. Each list in second layer contains
        name and score.

        RETURNS:
        A nested list. Each list in second layer contains name and score.
        """
        # make score to int to compare
        for i in range(len(leaderboard_list)):
            leaderboard_list[i][0] = int(leaderboard_list[i][0])
        # bubble sort
        for i in range(len(leaderboard_list)):
            for j in range(0, len(leaderboard_list) - i - 1):
                if leaderboard_list[j][0] > leaderboard_list[j + 1][0]:  # if the next score is better than previous one
                    leaderboard_list[j], leaderboard_list[j + 1] = leaderboard_list[j + 1], leaderboard_list[j]  # sort
        # change score back to string
        for i in range(len(leaderboard_list)):
            leaderboard_list[i][0] = str(leaderboard_list[i][0])
        return leaderboard_list

    def add_record(self, record, leaderboard_list):
        """
        FUNCTION - add_record()
        This function is add records into a leaderboard list.

        PARAMETERS:
        leaderboard_list - a nested list. Each list in second layer contains
        name and score.

        RETURNS:
        None
        """
        for i in range(len(leaderboard_list)):
            if record[1] == leaderboard_list[i][1]: # has previous record
                if int(record[0]) < int(leaderboard_list[i][0]): # better score
                    leaderboard_list[i][0] = record[0]
                return
        leaderboard_list.append(record) # if name never shows up so no previous record









