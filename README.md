Sometimes when I'm on Libby browsing for audiobooks, I see books 30 hours long that I know don't take that long to read, and others that are long page-wise but their listening time is only a few hours. The only explanation is that some audiobook narrators are slower than others. This project's goal is to figure out if some audiobook narrators are slower than others.

Everything is done in Python, and eventually I plan to move the data into Excel or SQL to do some analysis and make visualizations. The "updated-libby-scraping" file scrapes info on the first 100 pages of audiobooks (24 per page, 2,400 total) for the genre given at the beginning; I've used it on fiction and juvenile fiction, to see if juvenile fiction readers are slower.

The next step is to scrape the library catalog for page numbers for those same books and compare durations and page numbers.
