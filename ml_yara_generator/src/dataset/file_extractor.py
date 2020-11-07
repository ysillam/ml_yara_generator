import pandas as pd
import os
import glob
from sklearn.feature_extraction.text import TfidfVectorizer

DATASET_LOC_BEN = "dataset", "xls", "benign"
DATASET_LOC_MAL = "dataset", "xls", "malicious"
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class FileExtractor:
    """
    This class parses the given CSV dataset.
    """

    @staticmethod
    def get_file_list(subfolder, extension):
        """

        :param subfolder: sublocation where to look for files
        :return:
        """
        location = ROOT_DIR
        for subitem in subfolder:
            location = os.path.join(location, subitem)

        list_of_files = []

        if os.path.exists(location):
            path = location + r"/*." + extension
            print("Searching ", path)
            for filename in glob.glob(path):
                with open(filename, "rb") as file:
                    content = file.read()
                    list_of_files.append(content)
        return list_of_files
    @staticmethod
    def extract(file_type):
        """
        This function extracts the files content from the location "/ROOT/dataset/FILE_TYPE"
        :param file_type:
        :return:
        """
        benign  = FileExtractor.get_file_list(DATASET_LOC_BEN, file_type)
        malicious = FileExtractor.get_file_list(DATASET_LOC_MAL, file_type)
        df = pd.DataFrame()
        df["document"] = benign + malicious
        df["label"] =  [0] * len(benign) + [1] * len(malicious)

        return df
