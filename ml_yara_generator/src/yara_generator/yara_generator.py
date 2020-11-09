from os import path
import random
from ml_yara_generator.src.dataset import file_extractor
from ml_yara_generator.src.conf import conf
from ml_yara_generator.src.classifiers.default_classifier import Classifier

DATASET_LOC = "dataset"
ROOT_DIR = path.dirname(path.abspath(__file__))


class YaraGenerator:
    """
    This class generates the Yara signature.
    """

    def __init__(self, filetype, set_benign, set_malicious):
        """
        This function generates the yara rule
        :param filetype: filetype to be considered
        """
        self.yara = None

        strings = self.collect_meaningful_strings(filetype, set_benign, set_malicious)

        self.yara = self.fill_template(strings, filetype)

    def fill_template(self, strings, filetype):
        """
        This function returns a valid yara rule for the given dataset
        :param strings: List of meaningful strings
        :param magic: Magic of the file type
        :return:
        """
        magic = conf.MAGIC[filetype]
        rule_name = filetype + "_" + str(random.randint(10000, 100000))
        strings = [bytes(string, "ISO-8859-1").hex() for string in strings]
        
        if magic is not None:
            template = """
        
rule """ + rule_name + """
{
    strings:
        
        $magic =  """ + magic + """
        """ + \
        "\n\t".join(["$c" + str(idx) + " = {" + string + "}" for idx, string in enumerate(strings)]) + """
    condition:
        ($magic at 0) and (all of ($c*))
}        
"""
            
        else:       
            template = """
        
rule """ + rule_name + """
{
    strings:
        
        """ + \
        "\n\t".join(["$c" + str(idx) + " = {" + string + "}" for idx, string in enumerate(strings)]) + """
    condition:
        (all of ($c*))
}        
"""
        return template

    def collect_meaningful_strings(self, filetype, set_benign, set_malicious):
        """

        :return:
        """
        # Extraction of the malicious / benign files
        df = file_extractor.FileExtractor.extract(filetype, set_benign, set_malicious)
        if len(df.loc[df.label == 1]) == 0:
               return []

        # Learning of TFIDF followed by RandomForest classifier
        pipe = Classifier()
        pipe.fit(df["document"], df["label"])

        feat_labels = list(pipe.pipe.named_steps["vect"].vocabulary_.keys())
        importance = pipe.pipe.named_steps["clf"].feature_importances_
        indexes = importance.argsort()[-5:][::-1]
        return [feat_labels[x] for x in indexes]

    def export_yara(self, output_dir):
        """
        Export yara to file
        :param output_dir: Output location
        :return: None
        """
        try:
            with open(output_dir, "w") as file:
                file.write(self.yara)
        except:
            print("Impossible to write yara")
