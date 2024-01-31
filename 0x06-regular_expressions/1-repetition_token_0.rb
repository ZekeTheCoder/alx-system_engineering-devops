#!/usr/bin/env ruby
# This is a Ruby script that accepts one argument and pass it to a regular expression that matches the following cases:
# hbn
# hbtn
# hbttn
# hbtttn
# hbttttn
# hbtttttn
# hbttttttn

puts ARGV[0].scan(/hbt{2,5}n/).join
