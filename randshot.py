#!/usr/bin/env python

import httplib2, sys, os, random, string

ENDLINE = '\033[0m'
BOLD = '\033[1m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
GREEN = '\033[92m'
RED = '\033[91m'
GREYBACK = '\033[40m'

dirname = 'Lightshotr'

pngCount = 0
foundss = 0

def generate_id(size=6):
	return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(size))

def save_pic(content, pic_id, ext):
	f = open(dirname + '/' +str(pic_id) + ext,'wb')
	f.write(content)
	f.close

def print_status(png_count, link, color):
	print BLUE + BOLD + '[+] ' + ENDLINE + str(png_count) + ' Screenshots Found - ' + color + BOLD + link + ENDLINE

def abort():
	print '\n\n' + GREEN + BOLD + '[+]' + ENDLINE + ' All found Screenshots were saved to: ' + BOLD + os.getcwd() + '/' + dirname + ENDLINE + ' . Enjoy ;)\n'
	sys.exit(0)

print YELLOW + BOLD + '''
  _____                 _  _____ _           _   
 |  __ \               | |/ ____| |         | |  
 | |__) |__ _ _ __   __| | (___ | |__   ___ | |_ 
 |  _  // _` | '_ \ / _` |\___ \| '_ \ / _ \| __|
 | | \ \ (_| | | | | (_| |____) | | | | (_) | |_ 
 |_|  \_\__,_|_| |_|\__,_|_____/|_| |_|\___/ \__|

 ''' + ENDLINE + GREYBACK + YELLOW + BOLD + 'Author:' + ENDLINE + ' @xD4rker\n'

if not os.path.exists(dirname):
    os.makedirs(dirname)

while 1:

	try:

		status_color = RED
		pic_id = generate_id()
		link = 'https://prnt.sc/' + pic_id + '/direct'
		h = httplib2.Http(timeout=100)
		resp = h.request(link)

		if 'content-location' in resp[0]:
			pngUrl = resp[0]['content-location']
			ext = '.' + pngUrl[-3:]

			if (pngUrl != 'http://i.imgur.com/8tdUI8N.png') & (ext == '.png' or ext == '.jpg'):
				pngCount += 1
				save_pic(resp[1], pic_id, ext)
				status_color = GREEN
			
		print_status(pngCount, link, status_color)

	except httplib2.RelativeURIError:
		pass
	except KeyboardInterrupt:
		abort()
	except Exception as e:
		print '\n\n' + GREEN + BOLD + '[+]' + ENDLINE + ' An error occurred: ' + str(e)
		sys.exit(1)
