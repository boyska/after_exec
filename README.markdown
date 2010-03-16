Sometimes you launch a command from shell, then you realize you should have run 'command1;command2'

so, run
source after.sh
wait_pname command1 'command2'

NOTE: command2 could be even a complex one, like 'dmesg|tail', or 'ls|wc -l'. Whatever it is, just quote it :)

WARNING: it still is in "experimental" state, so this could not work at all, or not as expected
