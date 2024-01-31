#!/usr/bin/env ruby
# This is a Ruby script that accepts one argument and pass it to a regular expression that matches the following cases:
# htn (match)
# hbtn (match)
# hbbtn
# hbbbtn

puts ARGV[0].scan(/^hb{0,1}tn$/).join
