class Browser:
    def __init__(i):
        i.stack = []
        i.f_stack = []

    def go(i, url):
        i.stack.append(url)
        i.f_stack.clear()

    def back(i):
        if len(i.stack) > 1:
            i.f_stack.append(i.stack.pop())
            return i.stack[-1]

    def forward(i):
        if i.f_stack:
            i.stack.append(i.f_stack.pop())
            return i.stack[-1]

    def printAll(i):
        print(*i.stack)


browser = Browser()
browser.go("google.com")
browser.go("ukdw.ac.id")
browser.go("facebook.com")
print(browser.back()) 
print(browser.back()) 
print(browser.forward())
browser.go("twitter.com") 
browser.printAll() 