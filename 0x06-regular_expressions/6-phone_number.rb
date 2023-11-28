#!/usr/bin/env ruby
puts ARGV[0].scan(/1?[\s-]?\(?(d{3})\)?[\s-]?\d{3}[\s-]?\d{4}/).join
