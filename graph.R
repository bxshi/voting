#!/usr/bin/env Rscript

library(sfsmisc)

print_graph = function(file_path, title, sequence, prefix, xlabel, dividedx=1){
	
	data = read.table(file_path, header=TRUE, sep=",")
	time = c()
	time_sd = c()
	memory = c()
	memory_sd = c()
	io_time = c()
	io_sd = c()
	average_mutex_time = c()
	mutex_sd = c()
	
	for (i in sequence) {
		time[length(time)+1] = mean(data[data[,title] == i, "time"])
		time_sd[length(time_sd)+1] = sd(as.vector(data[data[,title] == i, "time"], "numeric"), na.rm=TRUE)
		memory[length(memory)+1] = mean(data[data[,title] == i, 'memory']) / 1024
		memory_sd[length(memory_sd)+1] = sd( as.vector(data[data[,title] == i, "memory"] / 1024, "numeric"), na.rm=TRUE)
		io_time[length(io_time)+1] = mean(data[data[,title] == i, 'io_time'])
		io_sd[length(io_sd)+1] = sd( as.vector(data[data[,title] == i, "io_time"], "numeric"), na.rm=TRUE)
		average_mutex_time[length(average_mutex_time)+1] = mean(data[data[,title] == i, 'mutex_time']) * 1000
		mutex_sd[length(mutex_sd)+1] = sd( as.vector(data[data[,title] == i, "mutex_time"] * 1000, "numeric"), na.rm=TRUE)
	}
		
	sequence = sequence / dividedx
	
	pdf(paste(prefix, '_time.pdf', sep=""))
	errbar(sequence, time, time + time_sd, time - time_sd,ylab="Execution Time (Seconds)", xlab=xlabel)
	lines(sequence, time, type="o", pch=21, lty=1)
	dev.off()
	
	pdf(paste(prefix, '_memory.pdf', sep=""))
	errbar(sequence, memory, memory + memory_sd, memory - memory_sd, ylab="Memory (MBytes)", xlab=xlabel)
	lines(sequence, memory, type="o", pch=21, lty=1)
	dev.off()
		
	pdf(paste(prefix, '_io.pdf', sep=""))
	errbar(sequence, io_time, io_time + io_sd, io_time - io_sd, ylab="I/O Time (Seconds)", xlab=xlabel)
	lines(sequence, io_time, type="o", pch=21, lty=1)
	dev.off()
	
	pdf(paste(prefix, '_mutex.pdf', sep=""))
	errbar(sequence, average_mutex_time, average_mutex_time + mutex_sd, average_mutex_time - mutex_sd, ylab="Average Mutex Operation Time (Milliseconds)", xlab=xlabel)
	lines(sequence, average_mutex_time, type="o", pch=21, lty=1)
	dev.off()
	
}

print_graph(file_path='c_all', title='number', sequence=seq(1, 14, 1), prefix="core", xlabel="Number of Cores")

print_graph(file_path='bs_all', title='number', sequence=seq(20, 1000000, 100000), prefix="block", xlabel="Block Size of Reading (KBytes)", dividedx=1024)
 
print_graph(file_path='fh_all', title='zipf', sequence=seq(10, 19, 1), prefix="file_he", xlabel="Zipf Distribution Ratio", dividedx=10)
 
print_graph(file_path='nf_all', title='number', sequence=seq(11, 150, 10), prefix="file_num", xlabel="Number of Files")
 
print_graph(file_path='fsh_all', title='zipf', sequence=seq(10, 19, 1), prefix="file_size", xlabel="Zipf Distribution Ratio", dividedx=10)

