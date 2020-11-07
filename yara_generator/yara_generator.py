
from os import path
import random
from ml_yara_generator.dataset import file_extractor
from ml_yara_generator.conf import conf
from ml_yara_generator.classifiers.default_classifier import Classifier

DATASET_LOC = "dataset"
ROOT_DIR = path.dirname(path.abspath(__file__))


class YaraGenerator:
    """
    This class generates the Yara signature.
    """
    def fill_template(self, strings, filetype):
        """
        This function returns a valid yara rule for the given dataset
        :param strings: List of meaningful strings
        :param magic: Magic of the file type
        :return:
        """
        magic = conf.MAGIC[filetype]
        rule_name = filetype + "_" +str(random.randint(10000, 100000))
        template = """
rule """ + rule_name + """
{
    strings:
        
        $magic =  """ + magic + """
        """ + \
        "\n\t\t".join([ "$c" + str(idx) + " = \""+string+"\"" for idx, string in enumerate(strings)]) + """
    condition:
        ($magic at 0) and (all of ($c*))
}        
"""
        return template

    def collect_meaningful_strings(self, filetype):
        """

        :return:
        """
        # Extraction of the malicious / benign files
        df = file_extractor.FileExtractor.extract(filetype)

        # Learning of TFIDF followed by RandomForest classifier
        pipe = Classifier()
        pipe.fit(df["document"], df["label"])

        feat_labels = list(pipe.pipe.named_steps["vect"].vocabulary_.keys())
        importance = pipe.pipe.named_steps["clf"].feature_importances_
        indexes = importance.argsort()[-5:][::-1]
        return [feat_labels[x] for x in indexes]

    def __init__(self, filetype):
        """
        This function generates the yara rule
        :param malware_folder: location of the malware dataset
        :param filetype: filetype to be considered
        """

        strings = self.collect_meaningful_strings(filetype)

        yara = self.fill_template(strings, filetype)
        print(yara)





