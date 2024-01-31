#!/usr/bin/env ruby
# This is a Ruby script that accepts one argument and pass it to a regular expression that must match a 10 digit phone number.

puts ARGV[0].scan(/^[0-9]{10}$/).join
