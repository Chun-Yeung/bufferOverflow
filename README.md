# bufferOverflow
Only modifying the last byte can not make the return address to win().
Use a loop to input one more byte to the binary.
The offset between vuln() and win() hass exeeded the page limit.
To brute-force the canary, break one byte of the canary one time.
Modify the return address of the vuln function by making it to the win() function.
To determine the overflow size, use cyclic function in pwntool to generate a patterned sequence and determine the overflow size in gdb
Run gdb and break at the vuln function and input the sequence and see where an error is caused.
Count the number of characters from the beginning of the sequence to where it causes an error.(that's the number of overflow size)
