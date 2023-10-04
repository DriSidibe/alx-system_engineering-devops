#!/usr/bin/env ruby
sender = ARGV[0].scan(/(from:\w+)|(from:\+?\d*)/).join()
answer = sender.split(":")[1] + ","
receiver = ARGV[0].scan(/(to:\w+)|(to:\+?\d*)/).join()
answer = answer + receiver.split(":")[1] + ","
flags = ARGV[0].scan(/flags:-?\d:-?\d:-?\d:-?\d:-?\d/).join()
flags = flags.split(":")
flags.delete_at(0)
answer = answer + flags.join(":")
puts answer
