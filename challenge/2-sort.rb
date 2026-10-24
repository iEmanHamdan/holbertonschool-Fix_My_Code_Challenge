#!/usr/bin/env ruby
# Sort arguments numerically

# Convert all arguments to integers, sort them, and print each one
ARGV.map(&:to_i).sort.each do |arg|
  puts arg
end
