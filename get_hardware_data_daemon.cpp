#include <iostream>
#include <cstdlib>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>


/* This is a simple daemon that will be responsible for gathering hardware data, such as sensor voltages, and writing it to a named pipe for other processes to read. 
For now, it just writes a message to the pipe every 5 seconds.*/

int main() {
    pid_t pid = fork();

    // Check if the fork process has failed.
    if (pid < 0) {
        std::cerr << "The fork process has failed." << std::endl;
        exit(1);
        return 1;
    }

    // The child process will run the daemon code, while the parent process will exit.
    if (pid > 0) {
        std::cout << "Daemon process for gathering sensor voltage information has been created with PID: " << pid << std::endl;
        exit(0);
    }

    const char* pipePath = "/tmp/sensor_voltage_pipe";
    mkfifo(pipePath, 0666);
    while(true){
        int fd = open(pipePath, O_WRONLY);
        std::string msg = "Data from voltage collection daemon\n";
        write(fd, msg.c_str(), msg.length());
        close(fd);

        // My background process will be here eventually. For now, it just writes a message to the pipe every 5 seconds.

        sleep(5);
    }
    return 0;
}