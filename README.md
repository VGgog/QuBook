QuoBooks
=========

This api returns a quote from different books, and different authors.

The flask micro-framework is used as a tool.  
The PostgreSQL is used as a date base.

The quotes data itself is missing, only the api logic is presented.

Documentation
--------------
### GET-methods
Available at:  /api/quobook  
Returns one or more quotes.  
Parameters are set directly in the url input line.  
###### Params
count - Number of quotes that the api will return (default 1)  
id - Returns 1 quote with the given id.  
author - Returns quotes from a specific author, in a specified amount.  
book_title - Returns a quote for a given title, in a given quantity.  

If "id" is given, then other parameters are ignored.  
If "id" is not set, then the presence of the "author" parameter is checked, if it is absent.  
Then the presence of the "book_title" parameter, otherwise it will return 1 random quote.  
If only the "count" parameter is specified (if it is not specified, then count = 1), then returns random quotes in the specified quantity.  

### POST-methods
Available at: /api/quobook/new  
Writes a new quote (ID adds itself).  
###### Accepts a json-file, which should be like this:  
        {'Author': '<Quote Author>',
         'Book title': '<Title of the book where the quote is from>',
         'Quote': '<Quote itself>'
        }

###### Returns a json-file with a dictionary in this format:  
        {'Author': '<Quote Author>',
         'Book title': '<Title of the book where the quote is from>',
         'ID': '<id under which the quote is available>'
         'Quote': '<Quote itself>'
        }
        
### PUT-methods
Available at: /api/quobook/put
If the specified 'ID' exists, then the quote will be overwritten.
If the specified 'ID' does not exist then a new quote will be created.

###### Accepts a json-file, which should be like this:
    {'Author': '<Quote Author>',
     'Book title': '<Title of the book where the quote is from>',
     'ID': '<id under which the quote is available>'
     'Quote': '<Quote itself>'
     }

###### Returns a json-file with a dictionary in this format:
    {'Author': '<Quote Author>',
     'Book title': '<Title of the book where the quote is from>',
     'ID': '<id under which the quote is available>'
     'Quote': '<Quote itself>'
    }
    
### DELETE-methods
Availiable at: /api/quobook/del
Removes quote by "id"   
"id" of the quote is set in the url-parameter  
###### Returns a json file with the deleted quote dictionary in the following format:
    {'Author': '<Quote Author>',
     'Book title': '<Title of the book where the quote is from>',
     'ID': '<id under which the quote is available>'
     'Quote': '<Quote itself>'
    }