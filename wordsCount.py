# import re
# def cleanhtml(raw_html):
#     # CLEANR = re.compile('<.*?>') 
#     CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    
#     cleantext = re.sub(CLEANR, '', raw_html)
#     # CLEANR = re.compile('/(^|\n)\s*([a-z]+)\s*\{[^\}]*\}/gi')
#     # cleantext = re.sub(CLEANR, '', raw_html)
#     return cleantext

from bs4 import BeautifulSoup
# driver code
if __name__ == "__main__":
    with open('/Users/lauchiulam/Projects/DevOpsTechnicalChallenge/output/file.txt') as f:
        contents = f.read()
        soup = BeautifulSoup(contents).get_text()
        #open text file
        clean_content = open("/Users/lauchiulam/Projects/DevOpsTechnicalChallenge/output/clean_content.txt", "w")
        #write string to file
        clean_content.write(soup)
        #close file
        clean_content.close()
        #clean_contents = cleanhtml(contents)
        #print(soup)
        str = soup
        from collections import Counter
        str_list = str.split()
        counts = Counter(str_list).most_common(2)
        print(counts)

