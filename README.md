# conan-nlJson [![badge](https://img.shields.io/badge/conan.io-nlJson%2F2.0.2-green.svg?logo=data:image/png;base64%2CiVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAMAAAAolt3jAAAA1VBMVEUAAABhlctjlstkl8tlmMtlmMxlmcxmmcxnmsxpnMxpnM1qnc1sn85voM91oM11oc1xotB2oc56pNF6pNJ2ptJ8ptJ8ptN9ptN8p9N5qNJ9p9N9p9R8qtOBqdSAqtOAqtR%2BrNSCrNJ/rdWDrNWCsNWCsNaJs9eLs9iRvNuVvdyVv9yXwd2Zwt6axN6dxt%2Bfx%2BChyeGiyuGjyuCjyuGly%2BGlzOKmzOGozuKoz%2BKqz%2BOq0OOv1OWw1OWw1eWx1eWy1uay1%2Baz1%2Baz1%2Bez2Oe02Oe12ee22ujUGwH3AAAAAXRSTlMAQObYZgAAAAFiS0dEAIgFHUgAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfgBQkREyOxFIh/AAAAiklEQVQI12NgAAMbOwY4sLZ2NtQ1coVKWNvoc/Eq8XDr2wB5Ig62ekza9vaOqpK2TpoMzOxaFtwqZua2Bm4makIM7OzMAjoaCqYuxooSUqJALjs7o4yVpbowvzSUy87KqSwmxQfnsrPISyFzWeWAXCkpMaBVIC4bmCsOdgiUKwh3JojLgAQ4ZCE0AMm2D29tZwe6AAAAAElFTkSuQmCC)](http://www.conan.io/source/nlJson/2.0.2/arnemertz/stable)

Simple conan package for the header-only "JSON for modern C++" library by Niels Lohmann (https://github.com/nlohmann/json).

# Usage

In your conanfile, add `nlJson/2.0.8@arnemertz/stable` in the `[requires]` section. Since the library is header-only, settings do not apply.

## Options

There is an option `path` to change the path where the header gets deployed to. The default is empty, i.e. the header gets deployed directly into the include directory of the package and can be included via `#include <json.hpp>`.

To change this, specify the relative path, e.g. use

    conan build .. -o nlJson:path=nlohmann

or add the line

    nlJson:path=nlohmann

to the `[options]` section of your `conanfile.txt`, and then include the headers via `#include <nlohmann/json.hpp>`.

