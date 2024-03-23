#!/usr/bin/env ruby
# This is a Ruby script that accepts one argument and pass it to a regular expression 
# that matches the following cases and does not contain square brackets:
# hbn (match)
# hbon
# hbtn (match)
# hbttn (match)
# hbtttn (match)
# hbttttn (match)

puts ARGV[0].scan(/hbt*n/).join
