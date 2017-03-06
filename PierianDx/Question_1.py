#======================== Opening of Files =====================
9038647752 - vikas prouthit

open_vcf = open('mutect_immediate.vcf','r')
open_bed = open('truseq.bed','r')
open_xls = open('accepted.xls','w')

#======================== Reading Files ========================
vcf = open_vcf.readlines()
bed = open_bed.readlines()

#===============================================================
for line in vcf:
	if line.startswith('#CHR'):	# Header line
		open_xls.write(line)
	elif not line.startswith('#'):	# Checks entries for without '#'
		chr_pos = line.split()[0:2]
#=================== Comparing with bed file for accepted entries as per question ====================
		for i in range(0,len(bed)):
			split_bed = bed[i].rstrip()
			split_bed = split_bed.split('\t')
			if (int(chr_pos[1]) >= int(split_bed[1])) and (int(chr_pos[1]) <= int(split_bed[2])) and (chr_pos[0] == split_bed[0]):
				open_xls.write(line)
				break
open_vcf.close()
open_bed.close()
open_xls.close()
#======================== Files Closed =====================
