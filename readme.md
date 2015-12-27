Lumberjack
==========

	I'm a lumberjack, and I'm okay.
	I sleep all night and I work all day.

Lumberjack follows a log file and splits it into other log files if they match
patterns in the configuration file.

Requires: pygtail  (sudo pip install pygtail)
Does not require: women's clothing and hanging around in bars

Usage
-----

python lumberjack.py settings.json


Config
------
log_path: the log file to follow   
log_splits: the files to put log lines into if they match any one of the list of patterns (simple substring match)   
rest: time to rest if at the end of the log file   

    {
        "log_path": "test.log",
        "log_splits": {
            "output_example/path.log": ["pattern1", "patternN"],
            "output_example/silly.log": ["silly walk"]
        },
        "rest": 5
    }


