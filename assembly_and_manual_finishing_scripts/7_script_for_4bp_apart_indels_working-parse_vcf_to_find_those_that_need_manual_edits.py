vcf_file = "pilon.out.vcf.indels.vcf.recode.vcf"

output_filename = "pilon.out.vcf.indels.vcf.recode.vcf.parsed_correct_4bp_apart_indels"

vcf = open(vcf_file)
read = vcf.read()
#cleaninfile = read.replace("\n","")
#rep = cleaninfile.replace (">","\n>")
splitrep = read.split("\n")

lenght_of_vcf = len(splitrep)
line_count = 0
list_of_flags = ""
for line in splitrep:
    if len(line)>0:
        outcome = 1
        line_count = line_count + 1 
        if line.startswith("Hsc_scaff"):
            
            #print (line)
            linesplit = line.split("\t")
            #print (linesplit)
            length_diff = len(linesplit[3])-len(linesplit[4])
            #print (str(abs(length_diff)))
            if abs(length_diff) <2:
                
                #print(str(linesplit[3])+"  "+ str(linesplit[4]))
                position = int(linesplit[1])
                #print (str(position))

                #print (splitrep[line_count-2])

                line_neg_1 = splitrep[line_count-2]
                
                #print (line_neg_1)
                if line_neg_1.startswith("#"):
                    position_neg_1 = 0
                else:
                    linesplit_neg_1 = line_neg_1.split("\t")
                    length_diff_neg = len(linesplit_neg_1[3])-len(linesplit_neg_1[4])
                    if abs(length_diff_neg) <2:
                        position_neg_1 = int(linesplit_neg_1[1])
                        #print (str(position))
                        #print (str(position_neg_1))
                    else:
                        position_neg_1 = 0
                if position - position_neg_1 <5:
                    if position - position_neg_1 >0:
                        outcome = 2
                else:
                    outcome = 1
        else:
            outcome = 2
        #print (line)
        #print (str(outcome))
    
        list_of_flags = list_of_flags + str(outcome)+","
list_of_flags_split = list_of_flags.split(",")
#print (list_of_flags_split)
#print (str(len(list_of_flags_split)))
count = 0
final_output = ""
for entry in list_of_flags_split:
    if len(entry)>0:
        testint = int(entry)
        #print (entry)
        if testint is 2:
            #print (entry)
            final_output = final_output + splitrep[count] + "\n"
        count = count + 1

#print (final_output)
        
withmatchedid = open(output_filename,'w')
withmatchedid.write(final_output)
withmatchedid.close()

