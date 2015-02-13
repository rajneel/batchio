# Goals 

Batchio: Batch framework for the rest of us

What it does:
-------------
1. Runs command or series of commands using a script
2. Provides cron scheduling for commands, jobs
3. Provides a import, export of batch configuration for multi-environment maintainbility
4. Provides a simple interface for installation and maintainance
5. Provides a notification system for job success and failure
6. Provides an api for programmatic callbacks on job successe, interuptions and failures
7. First class data store 
8. Supports calendar logic overrides such that scheduler will override previous cron entries
9. Support archiving of artifacts such as files on file system via SFTP 

What it is not for:
-------------------
1. Distributed job map-reduce type system. Jobs are intended to run on a single box 


Nice to Haves:
--------------
1. LDAP integration
2. Dropbox integration

