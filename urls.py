urls = '';
f=open('urls.txt','w')
for x in range(0, 35):
    urls = 'https://orwelldiaries.wordpress.com/page/%d\n' % (x)
    f.write(urls)
f.close