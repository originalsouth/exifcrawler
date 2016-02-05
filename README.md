# exifcrawler
Ever wanted to scrape some GPS data of the internet?
```
#By BC van Zuiden -- Leiden, November 2016 */
#Probably very buggy USE AT OWN RISK this will brick everything you own */
#NOBODY but YOU is liable for anything that happened in result of using this */
#WARNING: DON'T RUN THIS PROGRAM THIS WILL DESTROY YOUR COMPUTER AND/OR HOUSE */
#Any copyrighted piece of code within this code is NOT mine */
#Inclusion of that code is forced upon me by a scary anonymous guy with a gun*/
```
Feel free to reuse and contribute, pull requests are very welcome!
This code is (and forever will be) a work in progress.

### Running
This program is written for python3.
You will need BeautifulSoup, UserAgent and  p3exiv2 to run.
You can use pip to install the.
Scraping from a "random" site:
```
./exifcrawler.py
```
Scraping from a "random" site and follow links up to n orders (where n is an integer)
```
./exifcrawler.py n
```
Scraping from a specific site and follow links up to n orders
```
./exifcrawler.py url n
```
