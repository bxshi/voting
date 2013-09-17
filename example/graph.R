#!/usr/bin/env Rscript
# File Heterogeneity

fh_data = read.table('fh_all', header=TRUE, sep=",")

fh_alpha_seq = seq(1, 4.5, 0.5)
fh_time = c()
fh_memory = c()
fh_ratio = c()
fh_thread = c()
fh_mutex = c()

for (i in seq(10, 45, 5)) {

	fh_time[length(fh_time)+1] = mean(fh_data[fh_data[,"zipf"]==i/10,'time'])
	fh_memory[length(fh_memory)+1] = mean(fh_data[fh_data[,"zipf"]==i/10,'memory'])/1024
	fh_ratio[length(fh_ratio)+1] = mean(fh_data[fh_data[,"zipf"]==i/10,'ratio'])
	fh_thread[length(fh_thread)+1] = mean(fh_data[fh_data[,"zipf"]==i/10,'thread'])
	fh_mutex[length(fh_mutex)+1] = mean(fh_data[fh_data[,"zipf"]==i/10,'mutex'])
	
}

pdf('fh_time.pdf')
plot(fh_alpha_seq, fh_time, xlab="Zipf Distribution Factor", ylab="Execution Time (Second)", type="o", pch=21, lty=1)
legend(fh_alpha_seq[which.min(fh_alpha_seq)]+0.2, fh_time[which.max(fh_time)], c("Zipf distribution"), cex=0.8, pch=21, lty=1)
dev.off()

pdf('fh_memory.pdf')
plot(fh_alpha_seq, fh_memory, xlab="Zipf Distribution Factor", ylab="Memory (MBytes)", type="o",pch=21, lty=1)
legend(fh_alpha_seq[which.min(fh_alpha_seq)]+0.2, fh_memory[which.max(fh_memory)], c("Zipf distribution"), cex=0.8, pch=21, lty=1)
dev.off()

pdf('fh_io.pdf')
plot(fh_alpha_seq, fh_ratio, xlab="Zipf Distribution Factor", ylab="I/O Versus Computing", type="o")
legend(fh_alpha_seq[which.min(fh_alpha_seq)]+0.2, fh_ratio[which.max(fh_ratio)], c("Zipf distribution"), cex=0.8, pch=21, lty=1)
dev.off()

pdf('fh_critical.pdf')
plot(fh_alpha_seq, fh_thread, xlab="Zipf Distribution Factor", ylab="Critical Zone Time (Second)", type="o")
legend(fh_alpha_seq[which.min(fh_alpha_seq)]+0.2, fh_thread[which.max(fh_thread)], c("Zipf distribution"), cex=0.8, pch=21, lty=1)
dev.off()

pdf('fh_mutex.pdf')
plot(fh_alpha_seq, fh_mutex, xlab="Zipf Distribution Factor", ylab="Mutex Call Times", type="o")
legend(fh_alpha_seq[which.min(fh_alpha_seq)]+0.2, fh_mutex[which.max(fh_mutex)], c("Zipf distribution"), cex=0.8, pch=21, lty=1)
dev.off()

# Number of Files

nf_data = read.table('nf_all', header=TRUE, sep=",")
nf_number_seq = seq(1, 451, 50)
nf_time = c()
nf_memory = c()
nf_ratio = c()
nf_thread = c()
nf_mutex = c()
for (i in nf_number_seq) {

	nf_time[length(nf_time)+1] = mean(nf_data[nf_data[,"number"]==i,'time'])
	nf_memory[length(nf_memory)+1] = mean(nf_data[nf_data[,"number"]==i,'memory'])/1024
	nf_ratio[length(nf_ratio)+1] = mean(nf_data[nf_data[,"number"]==i,'ratio'])
	nf_thread[length(nf_thread)+1] = mean(nf_data[nf_data[,"number"]==i,'thread'])
	nf_mutex[length(nf_mutex)+1] = mean(nf_data[nf_data[,"number"]==i,'mutex'])
	
}

pdf('nf_time.pdf')
plot(nf_number_seq, nf_time, xlab="Number of Files", ylab="Execution Time (Second)", type="o", pch=21, lty=1)
legend(nf_number_seq[which.min(nf_number_seq)]+0.2, nf_time[which.max(nf_time)], c("File of Numbers"), cex=0.8, pch=21, lty=1)
dev.off()

pdf('nf_memory.pdf')
plot(nf_number_seq, nf_memory, xlab="Number of Files", ylab="Memory (MBytes)", type="o", pch=21, lty=1)
legend(nf_number_seq[which.min(nf_number_seq)]+0.2, nf_memory[which.max(nf_memory)], c("File of Numbers"), cex=0.8, pch=21, lty=1)
dev.off()

pdf('nf_io.pdf')
plot(nf_number_seq, nf_ratio, xlab="Number of Files", ylab="I/O Versus Computing", type="o", pch=21, lty=1)
legend(nf_number_seq[which.min(nf_number_seq)]+0.2, nf_ratio[which.max(nf_ratio)], c("File of Numbers"), cex=0.8, pch=21, lty=1)
dev.off()

pdf('nf_critical.pdf')
plot(nf_number_seq, nf_thread, xlab="Number of Files", ylab="Critical Zone Time (Second)", type="o", pch=21, lty=1)
legend(nf_number_seq[which.min(nf_number_seq)]+0.2, nf_thread[which.max(nf_thread)], c("File of Numbers"), cex=0.8, pch=21, lty=1)
dev.off()

pdf('nf_mutex.pdf')
plot(nf_number_seq, nf_mutex, xlab="Number of Files", ylab="Mutex Call Times", type="o", pch=21, lty=1)
legend(nf_number_seq[which.min(nf_number_seq)]+0.2, nf_mutex[which.max(nf_mutex)], c("File of Numbers"), cex=0.8, pch=21, lty=1)
dev.off()

# File Size Heterogeneity

fsh_data = read.table('fsh_all', header=TRUE, sep=",")
fsh_alpha_seq = seq(1, 4.5, 0.5)
fsh_time = c()
fsh_memory = c()
fsh_ratio = c()
fsh_thread = c()
fsh_mutex = c()
for (i in fsh_alpha_seq) {

	fsh_time[length(fsh_time)+1] = mean(fsh_data[fsh_data[,"zipf"]==i,'time'])
	fsh_memory[length(fsh_memory)+1] = mean(fsh_data[fsh_data[,"zipf"]==i,'memory'])/1024
	fsh_ratio[length(fsh_ratio)+1] = mean(fsh_data[fsh_data[,"zipf"]==i,'ratio'])
	fsh_thread[length(fsh_thread)+1] = mean(fsh_data[fsh_data[,"zipf"]==i,'thread'])
	fsh_mutex[length(fsh_mutex)+1] = mean(fsh_data[fsh_data[,"zipf"]==i,'mutex'])
	
}

pdf('fsh_time.pdf')
plot(fsh_alpha_seq, fsh_time, xlab="Zipf Distribution Ratio", ylab="Execution Time (Second)", type="o", pch=21, lty=1)
legend(fsh_alpha_seq[which.min(fsh_alpha_seq)]+0.2, fsh_time[which.max(fsh_time)], c("Zipf Distribution Ratio"), cex=0.8, pch=21, lty=1)
dev.off()

pdf('fsh_memory.pdf')
plot(fsh_alpha_seq, fsh_memory, xlab="Zipf Distribution Ratio", ylab="Memory (MBytes)", type="o", pch=21, lty=1)
legend(fsh_alpha_seq[which.min(fsh_alpha_seq)]+0.2, fsh_memory[which.max(fsh_memory)], c("Zipf Distribution Ratio"), cex=0.8, pch=21, lty=1)
dev.off()

pdf('fsh_io.pdf')
plot(fsh_alpha_seq, fsh_ratio, xlab="Zipf Distribution Ratio", ylab="I/O Versus Computing", type="o", pch=21, lty=1)
legend(fsh_alpha_seq[which.min(fsh_alpha_seq)]+0.2, fsh_ratio[which.max(fsh_ratio)], c("Zipf Distribution Ratio"), cex=0.8, pch=21, lty=1)
dev.off()

pdf('fsh_critical.pdf')
plot(fsh_alpha_seq, fsh_thread, xlab="Zipf Distribution Ratio", ylab="Critical Zone Time (Second)", type="o", pch=21, lty=1)
legend(fsh_alpha_seq[which.min(fsh_alpha_seq)]+0.2, fsh_thread[which.max(fsh_thread)], c("Zipf Distribution Ratio"), cex=0.8, pch=21, lty=1)
dev.off()

pdf('fsh_mutex.pdf')
plot(fsh_alpha_seq, fsh_mutex, xlab="Zipf Distribution Ratio", ylab="Mutex Call Times", type="o", pch=21, lty=1)
legend(fsh_alpha_seq[which.min(fsh_alpha_seq)]+0.2, fsh_mutex[which.max(fsh_mutex)], c("Zipf Distribution Ratio"), cex=0.8, pch=21, lty=1)
dev.off()
