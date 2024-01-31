#!/usr/bin/env ruby
# This is a Ruby script that accepts one argument and pass it to a regular expression that must be only matching: capital letters.

puts ARGV[0].scan(/[A-Z]/).join
