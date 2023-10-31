#!/usr/bin/env ruby
# This script matches a repetition of a character t
puts ARGV[0].scan(/hbt{2,5}n/).join
