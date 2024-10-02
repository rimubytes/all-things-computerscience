# Introduction to MPI (Message Passing Interface)

MPI is a standard for passing messages between nodes in aparallel computing environment. It is widely used in High-Performing Computing applications, allowing tasks to be distributed across multiple processors.

**Key Concepts**:

- **Processes**: In MPI, tasks are split into independent processes that can run on separate nodes.
- **Communication**: Processes can communicate by passing messages, either synchronously (both processes wait) or asynchronously (non-blocking).
- **Rank**: Each process has a unique ID, called a "rank." This rank is used to identify which part of the problem the process is responsible for.

**Basic MPI Functions**:

1. MPI_Init: Initializes the MPI environment.
2. MPI_Comm_size: Determines the number of processes involved.
3. MPI_Comm_rank: Gets the rank of the current process.
4. MPI_Send and MPI_Recv: For sending and receiving messages between processes.
5. MPI_Finalize: Ends the MPI environment.

Hello World in MPI,

```c
#include <mpi.h>
#include <stdio.h>

int main(int argc, char** argv) {
    MPI_Init(NULL, NULL); // Initialize the MPI environment

    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size); // Get the number of processes

    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank); // Get the rank of the process

    printf("Hello World from rank %d out of %d processes\n", world_rank, world_size);

    MPI_Finalize(); // Finalize the MPI environment
}
```
