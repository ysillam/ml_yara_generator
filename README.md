# ml_yara_generator
This projects gives ability to automatically generate yara rules based on ML analysis of malicious samples.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.


```bash
git clone https://github.com/ysillam/ml_yara_generator.git
cd ml_yara_generator
pyton setup.py install
```
And that's it !

Once the project will be on PiPy, the project will be available from :

```bash
pip install ml_yara_generator
```

## Usage

```python
from ml_yara_generator import YaraGenerator

a = YaraGenerator('xls', dataset_benign, dataset_malicious)
a.export_yara("output.yar")
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)