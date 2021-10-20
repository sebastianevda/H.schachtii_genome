vcf_file = "cat.sorted.gff"
#requires a gff format of the output as exported by apollo but sorted by scaf (smallest first), then location (largest first) 

fasta_file = "Cam_Hsc_genome1.1_349.fa"

output_filename = "new_fasta_file.fa"

vcf = open(vcf_file)
read = vcf.read()
#cleaninfile = read.replace("\n","")
#rep = cleaninfile.replace (">","\n>")
splitrep = read.split("\n")


fasta = open (fasta_file)
read_fasta = fasta.read()
split_fasta = read_fasta.split(">")
final_out = ""
for entry in split_fasta:
    if len(entry) >0:
        linesplits = entry.split("\n")
        name_of_scaff = linesplits[0]
        s = ""
        fasta_sequence = s.join(linesplits[1:])
        new_fasta_sequence = fasta_sequence
        #print (fasta_sequence)
        #print (">"+linesplits[0] + "\n" + s.join(linesplits[1:])) # dont forget to add back the ) to the first entry
        for line in splitrep:
            if len(line)>0:
                #print (line)
                linesplit = line.split("\t")
                name_of_entry = linesplit[0]
                if name_of_entry in name_of_scaff:
                    ID = linesplit[8]
                    ID_split = ID.split("=")
                    #print (ID_split[3])
                    deletion_length = len(ID_split[3])
                    if "deletion" in linesplit[2]:
                        #print (line)
                        coord1 = int(linesplit[3])
                        coord2 = int(linesplit[4])
                        print (str(coord1))
                        new_new_fasta_sequence = new_fasta_sequence[:coord1-1] + new_fasta_sequence[coord2:]
                        #this works for all sized deletions.
                        new_fasta_sequence = new_new_fasta_sequence
                    if "insertion" in linesplit[2]:
                        #print (line)
                        coord1 = int(linesplit[3])
                        coord2 = int(linesplit[4])
                        print (str(coord1))
                        new_new_fasta_sequence = new_fasta_sequence[:coord1-1] + ID_split[3] + new_fasta_sequence[coord2:]
                        new_fasta_sequence = new_new_fasta_sequence
                        #this should work for any sized insertion
        len_fasta = len(new_fasta_sequence)
        fasta_splitter = list(new_fasta_sequence)
        
        out = ""
        count = 0
        for x in fasta_splitter:
            if len(x)>0:
                #print(x)
                out = out + x
                count = count + 1
                if int(count/80):
                    count = 0
                    #print("test")
                    out = out + "\n"
                
        final_out = final_out + ">" + name_of_scaff + "\n" + out + "\n"
        
                
#print (new_fasta_sequence)
        
withmatchedid = open(output_filename,'w')
withmatchedid.write(final_out)
withmatchedid.close()
