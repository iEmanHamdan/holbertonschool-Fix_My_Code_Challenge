#!/usr/bin/env ruby

result = []
ARGV.each do |arg|
  # Check if the argument is a valid integer string
  next unless arg =~ /\A-?\d+\z/
  
  val = arg.to_i
  inserted = false
  
  result.each_with_index do |item, index|
    if val < item
      result.insert(index, val)
      inserted = true
      break
    end
  end
  
  result << val unless inserted
end

result.each do |res|
  puts res
end
