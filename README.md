# Vaccine Finder

A simple python script to send you emails whenever a COVID-19 vaccination appointment opens up near you.

## Prerequisites

* `python 3`
* `pipenv` (If you don't have this, simply `pip3 install pipenv`)
* A throwaway gmail account set to [work with less secure apps](https://myaccount.google.com/lesssecureapps) 
(used as the "from" email address)

This may work with earlier versions of python. I haven't tested with anything but `3.8.2`

## Configuration
Copy/rename `sample_config.py` to `config.py` and modify to configure your geographical and email settings.
## Installation
```
$ pipenv install

$ pipenv run vaccine_finder.py
```

## License
This project is licensed under the terms of the [MIT license](./LICENSE.txt).

## Thanks
Huge thanks to @GUI for his work on https://www.vaccinespotter.org and the [api](https://www.vaccinespotter.org/api/)
used by this script!
