from bs4 import BeautifulSoup
from lxml import etree, html
import sys

classes = str(sys.argv[1]).split(', ')


with open("test.html", "r") as f:
    
  contents = f.read()

  soup = BeautifulSoup(contents, 'lxml')

  for element in soup.find_all(class_=True):
    newclass = '{'
    for count, i in enumerate(element['class']):
      if(i in classes):
        if(i == element['class'][-1]):
          newclass += 'classes.' + i 
        else:
          newclass += 'classes.' + i + ' + '
      else:
        if(count + 1 < len(element['class']) and element['class'][count+1] not in classes and count == 0):
          newclass += '"' + i + ' '
        elif(count + 1 < len(element['class']) and element['class'][count+1] not in classes and count != 0):
          newclass += i + ' '
        elif(count + 1 < len(element['class']) and element['class'][count+1] in classes and count != 0):
          newclass += i + ' " + '
        else:
          if(len(element['class']) == 1 or (count - 1 >= 0 and element['class'][count-1] in classes)):
            newclass += '"' + i + '"' 
          elif(i == element['class'][-1]):
            newclass += i + '"'
          else:
            newclass += '"' + i + ' " + ' 
    newclass += '}'
    element['class'] = newclass
  newsoup = str(soup).replace("class='", 'className=')
  newsoup = newsoup.replace('class="', 'className=')
  newsoup = newsoup.replace("}'" , "}")
  newsoup = newsoup.replace('}"' , "}")
  newsoup = newsoup.replace("<html><body>", "")
  newsoup = newsoup.replace("</body></html>", "")
  with open("output.html", "w") as file:
    file.write(newsoup)

      

