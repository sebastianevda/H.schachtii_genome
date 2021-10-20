A collection of commands for assembly and manual finishing of the H. schachtii genome to provide a record of all parameters specified.

For custom script parse_GFF_of_changes_to_new_genome.py
1. System requirements
Windows
All software dependencies and operating systems (including version numbers)
Python 3.9.6
Versions the software has been tested on
Python 3.9.6
Any required non-standard hardware
None

2. Installation guide
No installation required

3. Demo
Demo data and output are included
vcf_file = "cat.sorted.gff"
#requires a gff format of the output as exported by apollo but sorted by scaf (smallest first), then location (largest first) 
fasta_file = "Cam_Hsc_genome1.1.fa"
output_filename = "new_fasta_file.fa"

Instructions to run on data
Expected output
new_fasta_file.fa - introduced changes to Cam_Hsc_genome1.1.fa to give rise to Cam_Hsc_genome1.2.fa
Expected run time for demo on a "normal" desktop computer
1 minutes

4. Instructions for use
Install python, run script in same directory as input files.




For custom script Parse_vcf_to_find_adjacent_indels_for_manual_inspection.py
1. System requirements
Windows
All software dependencies and operating systems (including version numbers)
Python 3.9.6
Versions the software has been tested on
Python 3.9.6
Any required non-standard hardware
None

2. Installation guide
No installation required

3. Demo
Demo data and output are included
vcf_file = "pilon.out.vcf.indels.vcf.recode.vcf"
output_filename = "pilon.out.vcf.indels.vcf.recode.vcf.parsed_correct_4bp_apart_indels"

Instructions to run on data
Expected output
"pilon.out.vcf.indels.vcf.recode.vcf.parsed_correct_4bp_apart_indels" - identify only those indels that are up to 4bp from another indel.
Expected run time for demo on a "normal" desktop computer
10 seconds

4. Instructions for use
Install python, run script in same directory as input file.
