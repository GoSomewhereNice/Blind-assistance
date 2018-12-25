#!/usr/bin/expect
set user "pi"
set passwd "raspberry"
spawn ssh $user@192.168.1.116

expect {
"yes/no" { send "yes\r"; exp_continue}
"password:" { send "$passwd\r" }
}
expect "]*"
send "sudo python Blind-assistance/iBeaSender/HC-SR501.py > /dev/null &\r"
expect "]*"
send "exit\r"
