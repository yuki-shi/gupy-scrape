# gupyuki: i don't wanna be a NEET anymore
simple CLI script for Gupy-related job-hunting.

returns a table with the latest job listings if there were any posted in the same day.

## usage
after cloning, create an env and install required dependecies by running:

```bash
$ chmod a+rx init.sh
$ ./init.sh
```
then search for jobs with:
```bash
$ ./main.py -k JOB_NAME
```
where JOB_NAME is the keyword to be searched on Gupy.
