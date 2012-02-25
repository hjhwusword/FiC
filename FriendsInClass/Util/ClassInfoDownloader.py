import urllib2, re

DEBUG = True

# URLs
UW_SCHEDULE_PAGE = 'http://www.washington.edu/students/timeschd/'

######## re ############
DEPT_REG = r'<li><a href=\"([a-z]+?.html)\">([A-Za-z \-]+?) \((.+?)\)</a>' # Ignore case
COURSES_REG = r'<br>\n\n(.+?</table>)\n\n' # Multiple lines
PARSE_TITLE = r'<A NAME=(\D+?)(\d{3})>'
SECTIONS_REG = r'<table width="100%" >(.+?)</table>' # Multiple lines
PARSE_SECTION = r'\d{5}</A>\s*([A-Z]+)'
PARSE_TIME_LOCATION = r'\s+?([MTWhF]+)\s+([0-9P]+)-([0-9P]+)\s+<A HREF=/students/maps/map.cgi?.+>(.+?)</A>\s+([A-Za-z0-9]*)'
PARSE_TIME_ONLY = r'\s+?([MTWhF]+)\s+([0-9P]+)-([0-9P]+)\s+[0-9A-Za-z$]+'

HTML_ESCAPE = {
		"&": "&amp;",
		'"': "&quot;",
		"'": "&apos;",
		">": "&gt;",
		"<": "&lt;",
}

class ClassInfoDownloader:
	def __init__(self, quarter, year):
		self.__debug('Initializing.......')
		self.quarter = quarter
		self.year = year
		self.url = UW_SCHEDULE_PAGE + self.quarter + self.year
	
	def __fetchPage(self, url):
		req = urllib2.Request(url)
		try:
			f = urllib2.urlopen(req)
		except urllib2.HTTPError, e:
			print 'The server could not fulfile the request.'
			print 'Error code: ', e.code
		except urllib2.URLError, e:
			print 'We failed to reach a server.'
			print 'Reason: ', e.reason
		else:
			return f.read()
	
	def __eliminateDup(self, l):
		return tuple(set(l))

	def __html_escape(self, txt):
		return "".join(HTML_ESCAPE.get(c,c) for c in txt)

	def __debug(self, string):
		if DEBUG:
			print string
	
	def getDepts(self):
		self.__debug('get dept page names....')
		html = self.__fetchPage(self.url)
		ret_list = re.findall(DEPT_REG, html, re.I)
		ret_list =  self.__eliminateDup(ret_list)
		return ret_list

	def getCourses(self, dept):
		html = self.__fetchPage(self.url + "/" + dept)
		courses = re.findall(COURSES_REG, html, re.S)
		for course in courses:
			self.getSections(course)

	def getSections(self, course):
		abb_num = re.findall(PARSE_TITLE, course)[0]
		print abb_num
		sections = re.findall(SECTIONS_REG, course, re.S)
		for section in sections:
			self.getSingleSection(section)

	def getSingleSection(self, section):
		section_name = re.findall(PARSE_SECTION, section)
		section_time_loc = re.findall(PARSE_TIME_LOCATION, section)
		section_time = re.findall(PARSE_TIME_ONLY, section)
		print section_name
		if section_time_loc:
			print section_time_loc
		if section_time:
			print section_time
		print ""
		


x = ClassInfoDownloader('SPR', '2012')
depts = x.getDepts()
for dept in depts:
	x.getCourses(dept[0])
	raw_input("press enter")
