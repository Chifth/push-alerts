#!/usr/bin/python2.7
import cookielib 
import urllib2 
import mechanize 
import time

#create browser object
br = mechanize.Browser() 

token = '8ec07a6cefadbaf7b92f6ed5aa203124'

#enable cookie support for urllib2 
cookiejar = cookielib.LWPCookieJar() 
br.set_cookiejar( cookiejar ) 

#set browser options 
br.set_handle_equiv( True ) 
br.set_handle_gzip( True ) 
br.set_handle_redirect( True ) 
br.set_handle_referer( True ) 
br.set_handle_robots( False ) 

br.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time = 1 ) 

br.addheaders = [ ( 'User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1' ) ] 

#authenticate 
br.open('http://sdrintel.com/database/login.php') 
br.select_form( name="login" ) 

#pass token
br[ "token" ] = token
res = br.submit() 

#open search page after auth
search = br.open('http://sdrintel.com/database/search.php?faiien') 

search_details = search.read()
print search_details

#details = br.open('http://sdrintel.com/database/db_lookup.php')
#read_details = details.read()
#print read_details





