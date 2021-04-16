input_filename = "mcl_level4.txt"
infile = open(input_filename)
read = infile.read()
import re
output_filename = "mcl_level4.txt.counts"
withmatchedid = open(output_filename, "w")
#cleaninfile = read.replace("\n","")
#rep = cleaninfile.replace (">","\n>")
splitrep = read.split("\n")
#print splitrep
#NAMES_DICT = {}
count = 0

list_of_search_terms = ("orysa_pan", "AT[1-5]G", "medtr_pan", "sorbi_pan", "vitvi_pan", "bradi_pan", "Mba[0-9][0-9]_", "musac_pan", "thecc_pan", "Manes", "maldo_pan", "cucsa_pan", "cajca", "HORVU", "phavu", "Cs[0-9]g", "PGSC", "evm_27", "XP_", "cicar_pan", "Cc[0-9][0-9]_", "Cg[0-9]g", "MELO", "Ca_[0-9]", "brana_pan", "DCAR", "ipotf_pan", "FvH", "cocnu_pan", "capan_pan", "XP_", "ORGLA", "Oeu", "itb", "Bv[0-9]_", "soybn_pan", "Solyc", "HanXRQ", "AUR", "Cm[0-9][0-9][0-9]", "braol_pan", "tritu_pan", "maize_pan", "Sspon", "brarr_pan", "Dr[0-9][0-9]")

outstring = "Oryza sativa	Arabidopsis thaliana	Medicago truncatula	Sorghum bicolor	Vitis vinifera	Brachypodium distachyon	Musa balbisiana	Musa acuminata	Theobroma cacao	Manihot esculenta	Malus domestica	Cucumis sativus	Cajanus cajan	Hordeum vulgare	Phaseolus vulgaris	Citrus sinensis	Solanum tuberosum	Amborella trichopoda	Elaeis guineensis	Cicer arietinum	Coffea canephora	Citrus maxima	Cucumis melo	Coffea arabica	Brassica napus	Daucus carota	Ipomoea trifida	Fragaria vesca	Cocos nucifera	Capsicum annuum	Phoenix dactylifera	Oryza glaberrima	Olea europaea	Ipomoea triloba	Beta vulgaris	Glycine max	Solanum lycopersicum	Helianthus annuus	Chenopodium quinoa	Citrus medica	Brassica oleracea	Triticum turgidum	Zea mays	Saccharum spontaneum	Brassica rapa subsp. rapa	Dioscorea rotundata\n"

for line in splitrep:
    if len(line)>0:
        for entry in list_of_search_terms:
            #print entry
            #number = re.finditer("orysa_pan",line)
            #print len(re.findall(entry,line))
            outstring = outstring + str(len(re.findall(entry,line))) + "\t"
        outstring = outstring + "\n"
        #print (line)



withmatchedid.write(outstring)
withmatchedid.close()
            
