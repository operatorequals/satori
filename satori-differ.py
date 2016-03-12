#!/usr/bin/python
#-*- coding: utf-8 -*-

import platform as plat

import logging as log
import argparse

import lib.image_differ as differ
import lib.image_io as io
import lib.definitions as defs


header = '''
Welcome to {0} Differ
OS filesystem image Difference Finder
Version {1}
'''.format(defs.program_name, defs.version)


log.basicConfig(format = "%(message)s")

__log = log.getLogger( __name__ )



if __name__ == "__main__" :

	os_def_name = plat.platform()

	parser = argparse.ArgumentParser( description = 'Deeply diffs 2 satori Images' )

	parser.add_argument( 'original', help = "Satori image to be treated as 'original'", type = str )
	parser.add_argument( 'subject', help = "Satori image to be examined", type = str )


	parser.add_argument( '--type', '-t', help = 'Choose the file type of the images saved/loaded',\
										type = str, choices = ['pickle', 'json', 'sqlite'], default = 'json')

	parser.add_argument( '--no-gzip', '-ng', help = 'Image IO will *NOT* use gzip (larger but readable files)', action = 'store_true', default = False)

	verb = parser.add_mutually_exclusive_group()
	verb.add_argument( '-v', '--verbose' , help = 'verbose mode', action = 'count', default = 0 )
	verb.add_argument( '--debug' , '-d', help = 'debugging mode', action = 'store_true', default = False )
	verb.add_argument( '--quiet', '-q' , help = 'quiet mode (show only critical differences)', action = 'store_true', default = False )


	args = parser.parse_args()



	'''	================================================ VERBOSITY CHECKS ================================================ '''

	if args.debug :
		__log.setLevel( log.DEBUG )
	elif args.quiet :
		__log.setLevel( log.ERROR )

	elif args.verbose == 0 :
		__log.setLevel( log.WARNING )

	elif args.verbose == 1 :
		__log.setLevel( log.INFO )




	'''	================================================ HEADER + INFO ================================================ '''

	__log.warning(header)
	if args.debug :
		__log.debug("* Debugging mode *")
	else :
		__log.warning("Verbosity set to: %d" % args.verbose)



	'''	================================================ COMPRESSION OPTION ================================================ '''

	if args.no_gzip :
		__log.info( "* Compression is Disabled! *" )
	else :
		__log.info( "Compression is Enabled!" )
		io.__use_gzip = True



	image1 = io.loadImage( args.original, args.type )
	image2 = io.loadImage( args.subject, args.type )
	differ.diffSystem( image1, image2 )
	__log.warning( "\n" )