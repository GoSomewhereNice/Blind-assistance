#!/usr/bin/expect
set user "pi"
set passwd "raspberry"
spawn ssh $user@192.168.1.116

expect {
"yes/no" { send "yes\r"; exp_continue}
"password:" { send "$passwd\r" }
}
expect "]*"
send "sudo ./Blind-assistance/iBeaSender/stopSdrBee.sh\r"
expect "]*"
send "echo Finish...\r"
expect "]*"
send "exit\r"
