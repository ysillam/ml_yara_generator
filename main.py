from ml_yara_generator.src.yara_generator.yara_generator import YaraGenerator

def main():
    """
    Main function of the code
    :return:
    """
    files_location = r"malware_folder"
    generator = YaraGenerator(
        "xls",
        r"C:\Users\yohann\PycharmProjects\ml_yara_generator\ml_yara_generator\src\dataset\xls\benign",
        r"C:\Users\yohann\PycharmProjects\ml_yara_generator\ml_yara_generator\src\dataset\xls\malicious"
    )
    print(generator.yara)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
