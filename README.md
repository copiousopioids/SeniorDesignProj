<snippet>
  <content><![CDATA[
# ${1:sWiFixer: A WiFi Heatmapper using Python}

The purpose of this project is to measure, store, and map wireless signal strength both spatially and over time. By measuring RSSI of the desired network at fixed or dynamic locations, one can build a visual diagram of the signal over a given space. This technology could have many use cases, from IT, to network planning, or even network security and monitoring. A robust program with these goals could save time and money for many organizations.

## Installation

Make sure you have the latest stable version of python 3.

Python Libraries:
 - matplotlib
 - pandas
 - scipy

## Usage

Run the Server:
```
python manage.py runserver
```
Run a test of the Heatmapper:
```
python heatmap.py "input/apartment-trans.png" "input/apartment.csv" "output/apartment-map.png"
```
## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Credits

Beau Gunderson (HeatMap base algorithm)

## License

TODO: Write license
