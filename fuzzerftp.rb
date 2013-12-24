#Metasploit

require 'msf/core'
class Metasploit3 < Msf::Auxiliary
        include Msf::Auxiliary::Scanner
        def initialize
                super(
                        'Name'           => 'Simple FTP Fuzzer', 
                        'License'        => MSF_LICENSE
                )
                register_options( [
                Opt::RPORT(21)
                ], self.class)
        end
        
     def run_host(ip)
                # Create an unbound UDP socket
                udp_sock = Rex::Socket::Udp.create(
                        'Context'   =>
                                {
                                        'Msf'        => framework,
                                        'MsfExploit' => self,
                                }
                )
                
                       
#! /usr/bin/env ruby

begin
	require 'rainbow'
	require 'socket'
	
rescue LoadError => e
	puts "ERROR: Looks like you are missing a ruby gem."
	puts e.inspect
end

unless ARGV.length == 1
	puts "The correct use of fuzzerftp.rb is as follows:"
	puts "Usage: ruby fuzzerftp.rb Target_IP"
	exit
end

targetIP = ARGV[0]


fuzz_String = ["A"]
counter = 2
while fuzz_String.length <= 50
	fuzz_String << A * counter
	Counter += counter
end


Commands = ["MKD", "RMD", "STOR"]
socket = TCPSocket.new(targetIP, 21)
socket.puts('USER msfadmin\r\n')
puts socket.gets
socket.puts('PASS msfadmin\r\n')
puts socket.gets
commands.each {|cmd|
	fuzz_String.each {|str|
		puts "Sending #{cmd} command with #{str.length} bytes"
		sockets.puts(cmd + " " + str + "\r\n")
		puts socket.gets
socket.puts('QUIT \r\n')
socket.close
