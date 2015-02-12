# Goals 
* Batchio: Batch framework for the rest of us *

What it does:
-------------
1. Runs command or series of commands using a script
2. Provides cron scheduling for commands, jobs
3. Provides a import, export of batch configuration for multi-environment maintainbility
4. Provides a simple interface for installation and maintainance
5. Provides a notification system for job success and failure
6. Provides an api for programmatic callbacks on job successe, interuptions and failures
7. First class data store 

What it is not for:
-------------------
1. Distributed job map-reduce type system. Jobs are intended to run on a single box 
