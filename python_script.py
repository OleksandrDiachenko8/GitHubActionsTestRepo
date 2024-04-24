import csv
with open("title.basics.tsv") as file:    
    tsv_file = csv.reader(file, delimiter="\t")    
    linenumber = 0
    for line in tsv_file:
        linenumber += 1        
        print(line)
        with open("movies.txt", 'a') as f:
            f.write(line + '\n')
        if linenumber > 25:
          break
          
