import requests

def getPage(url):
    try:
        response = requests.get(url)
        response.encoding = 'utf-8'
        return response.text
    except:
        return ""

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

page = getPage("https://www.imdb.com/title/tt1375666/")
parser = MyHTMLParser()
parser.feed(page)

class Movie:
    def getId(self, url):
        s = re.search(r'tt\d+', url)
        return s.group()
    def getNameYear(self, r):
        sel = '#title-overview-widget > div.vital > div.title_block > div > div.titleBar > div.title_wrapper > h1'
        s = r.html.find(sel, first=True).text
        year = re.search(r'\(\d+\)', s).group().strip("()")
        name = re.sub(r'\(\d+\)', "", s).strip()
        return name, year
    def getRateTimeGenre(self, r):
        sel = '#title-overview-widget > div.vital > div.title_block > div > div.titleBar > div.title_wrapper > div'
        s = r.html.find(sel, first=True).text
        s = s.split('|')
        rate = s[0].strip()
        duration = s[1].strip()
        genre = s[2].strip()
        return rate, duration, genre
    def getRating(self, r):
        sel = '#title-overview-widget > div.vital > div.title_block > div > div.ratings_wrapper > div.imdbRating > div.ratingValue > strong > span'
        return r.html.find(sel, first=True).text
    def getRatingCount(self, r):
        sel = '#title-overview-widget > div.vital > div.title_block > div > div.ratings_wrapper > div.imdbRating > a > span'
        return r.html.find(sel, first=True).text
    def getGenderRating(self, r):
        r = session.get(url)
        sel_m = "#main > section > div > table:nth-child(14) > tbody > tr:nth-child(3) > td:nth-child(2) > div.bigcell"
        sel_f = "#main > section > div > table:nth-child(14) > tbody > tr:nth-child(4) > td:nth-child(2) > div.bigcell"
        return r.html.find(sel_m, first=True).text, r.html.find(sel_f, first=True).text
    def getDirector(self, r):
        sel = "#title-overview-widget > div.plot_summary_wrapper > div.plot_summary > div:nth-child(2) > a"
        return r.html.find(sel, first=True).text
    def getWriter(self, r):
        sel = "#title-overview-widget > div.plot_summary_wrapper > div.plot_summary > div:nth-child(3) > a"
        return r.html.find(sel, first=True).text
    def getStar(self, r):
        # Just get the first
        sel = "#title-overview-widget > div.plot_summary_wrapper > div.plot_summary > div:nth-child(4) > a"
        return r.html.find(sel, first=True).text
    def getMetascore(self, r):
        sel = "#title-overview-widget > div.plot_summary_wrapper > div.titleReviewBar > div:nth-child(1) > a > div > span"
        return r.html.find(sel, first=True).text
    def getKeywords(self, r):
        sel = "#titleStoryLine > div:nth-child(6) > a > span"
        s = r.html.find(sel)
        keywords = []
        for word in s:
            keywords.append(word.text)
        return keywords
    def getTagline(self, r):
        sel = "#titleStoryLine > div:nth-child(8)"
        taglines = r.html.find(sel, first=True).text.split('\n')
        return taglines[1]
    def getCompany(self, r):
        sel = "#titleDetails > div:nth-child(19) > a:nth-child(2)"
        return r.html.find(sel, first=True).text
    def getBudget(self, r):
        sel = "#titleDetails > div:nth-child(12)"
        result = r.html.find(sel, first=True).text.split('\n')
        result = re.sub(r'\(.*\)', "", result[1])
        return result
    def getGross(self, r):
        sel = "#titleDetails > div:nth-child(15)"
        result = r.html.find(sel, first=True).text.split('\n')
        return result[1]
    def __init__(self, url):
        self.Id = self.getId(url)
        session = HTMLSession()
        r = session.get(url)
        self.Name, self.Year = self.getNameYear(r)
        self.MPAA, self.Duration, self.Genre = self.getRateTimeGenre(r)
        self.Rating = self.getRating(r)
        self.RatingCount = self.getRatingCount(r)
        self.Director = self.getDirector(r)
        self.Writer = self.getWriter(r)
        self.Star = self.getStar(r)
        self.Metascore = self.getMetascore(r)
        self.Keywords = self.getKeywords(r)
        self.Tagline = self.getTagline(r)
        self.Company = self.getCompany(r)
        self.Budget = self.getBudget(r)
        self.Gross = self.getGross(r)
        session.close()
    def printInfo(self):
        print("Id: " + self.Id)
        print("Name: " + self.Name)
        print("Release Year: " + self.Year)
        print("MPAA Rating: " + self.MPAA)
        print("Duration: " + self.Duration)
        print("Genre: " + self.Genre)
        print("Rating Count: " + self.RatingCount)
        print("Rating: " + self.Rating)
        print("Metascore: " + self.Metascore)
        print("Director: " + self.Director)
        print("Writer: " + self.Writer)
        print("Main Star: " + self.Star)
        print("Keywords: " + str(self.Keywords))
        print("Tagline: " + self.Tagline)
        print("Production Company: " + self.Company)
        print("Budget: " + self.Budget)
        print("Worldwide Gross: " + self.Gross)