import argparse

"""
 author   : Matthew J Swann
 mod date : 2014-08-17
"""

if __name__ == '__main__':
    pass
    
# args
parser = argparse.ArgumentParser(prog='books')
parser.add_argument( '--filter',  help='show a subset of books, looks for the argument as a substring of any of the fields' )
parser.add_argument( '--year',    help='sort the books by year, ascending instead of default sort', action='store_true' )
parser.add_argument( '--reverse', help='reverse sort', action='store_true')

args = parser.parse_args()

# data structure for response
repository = []

# csv file processing and insertion to display structure    
with open('csv') as the_file:
    csv = the_file.readlines()
    
    for line in csv:
        
        # if no filter or if filter string is contained, add the dict entry
        if ( not args.filter or args.filter in line ):
            
            line = line.split(',')
        
            repository.append( {'last_name':line[1].strip(), 'first_name':line[2].strip(), 'year':line[3].strip(), 'title':line[0].strip() } )

# pipe file processing and insertion to display structure          
with open('pipe') as the_file:
    pipe = the_file.readlines()
    
    for line in pipe:
        
        # if no filter or if filter string is contained, add the dict entry
        if ( not args.filter or args.filter in line ):
        
            line = line.split('|')
        
            repository.append( {'last_name':line[1].strip(), 'first_name':line[0].strip(), 'year':line[3].strip(), 'title':line[2].strip() } )

# slash file processing and insertion to display structure          
with open('slash') as the_file:
    slash = the_file.readlines()
    
    for line in slash:
        
        # if no filter or if filter string is contained, add the dict entry
        if ( not args.filter or args.filter in line ):
        
            line = line.split('/')
        
            repository.append( {'last_name':line[2].strip(), 'first_name':line[1].strip(), 'year':line[0].strip(), 'title':line[3].strip() } )

# sorting based on arg flags
if not ( args.reverse and args.year ) :
    
    repository = sorted(repository, key=lambda k:k['last_name']) 

if args.reverse :
    
    repository = sorted(repository, key=lambda k:k['last_name'], reverse=True)

if args.year :
    
    repository = sorted(repository, key=lambda k:k['year'])
        
# display formatting   
print '\n'
for entry in repository:
    print ('%s, %s, %s, %s') % (entry['last_name'], entry['first_name'], entry['title'], entry['year'])

print '\n'