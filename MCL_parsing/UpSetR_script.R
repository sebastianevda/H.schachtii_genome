#!/usr/bin/env r
setwd("/home_old/se389/H.schachtii/Ortho_groups/Output/Upset_plant/final")

files <- list("d24f.groups.matrix", "h10.groups.matrix", "d12f.groups.matrix", "h48.groups.matrix", "d12m.groups.matrix")

library(UpSetR)
for (file in files){
print(file)
movies <- read.csv(file, header = T, sep = "\t",stringsAsFactors=FALSE)
pdf(file = sprintf("plot_%s.pdf", file))
#plot<- upset(movies, order.by = "degree", keep.order = TRUE, empty.intersections = "on", intersections = list(list("Hscha","Hglyc_1","Gpalli", "Grosto", "Mhapl", "Mgrami", "Bxylo","Celeg"), list("Hscha","Hglyc_1","Gpalli", "Grosto", "Mhapl", "Mgrami", "Bxylo"), list("Hscha","Hglyc_1","Gpalli", "Grosto", "Mhapl","Mgrami"), list("Hscha","Hglyc_1","Gpalli", "Grosto"), list("Hglyc_1", "Hscha"), list("Hscha")), queries = list(list(query = intersects, params = list("Hscha","Hglyc_1","Gpalli", "Grosto", "Mhapl", "Mgrami", "Bxylo","Celeg"), active = T),list(query = intersects, params = list("Hscha","Hglyc_1","Gpalli", "Grosto", "Mhapl", "Mgrami", "Bxylo"), active = T),list(query = intersects, params = list("Hscha","Hglyc_1","Gpalli", "Grosto", "Mhapl", "Mgrami"), active = T),list(query = intersects, params = list("Hscha","Hglyc_1","Gpalli", "Grosto"), active = T),list(query = intersects, params = list("Hscha","Hglyc_1","Gpalli", "Grosto"), active = T),list(query = intersects, params = list("Hscha","Hglyc_1"), active = T),list(query = intersects, params = list("Hscha"), active = T)), expression = "Orthogroup < 1")
plot<- upset(movies, order.by = "degree", keep.order = TRUE, empty.intersections = "on", intersections = list(list("Arabidopsis_thaliana","Brassica_rapa_subsp._rapa","Glycine_max","Solanum_tuberosum","Solanum_lycopersicum","Zea_mays","Hordeum_vulgare", "Amborella_trichopoda"),list("Arabidopsis_thaliana","Brassica_rapa_subsp._rapa","Glycine_max","Solanum_tuberosum","Solanum_lycopersicum","Zea_mays","Hordeum_vulgare"),list("Arabidopsis_thaliana","Brassica_rapa_subsp._rapa","Glycine_max","Solanum_tuberosum","Solanum_lycopersicum"),list("Arabidopsis_thaliana","Brassica_rapa_subsp._rapa","Glycine_max"),list("Arabidopsis_thaliana","Brassica_rapa_subsp._rapa"),list("Arabidopsis_thaliana")))
print(plot)
dev.off()
}
