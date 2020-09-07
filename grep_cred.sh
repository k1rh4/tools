#!/bin/sh
$1 | grep "/bin/sh" |grep "system" |grep "passw" | grep "token" |grep secret | grep "upload" | grep "download" | grep "tar " | grep "unzip " | grep "hash" 
