from selenium import webdriver

print("Enter the URL you wish to search:")

inp=input()

url = webdriver.Chrome(executable_path=r'C:\Users\Yokesh\Downloads\chromedriver_win32\chromedriver.exe')
 
url.get("https://google.com/")

search = url.find_element_by_name('q')

search.send_keys(inp)

search.submit()



 
