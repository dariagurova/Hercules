require 'oauth2'
require 'json'

keys = File.read('keys.json')
data = JSON.parse(keys)

client = OAuth2::Client.new(data['UID'], data['SECRET'], site: 'https://api.intra.42.fr')
token = client.client_credentials.get_token

def display_location(info)
  puts 'USER'.ljust(20) + 'LOCATION'.rjust(18)

  info.each do |user|
    login = user[0]
    machine = user[1]
    color = user[2]

    print login.ljust(20)
    print machine.rjust(18)
    puts "\n"
  end
end

if ARGV.size != 1
  print 'Usage: ruby hind.rb <argument.txt>'
  exit
end

getFile = ARGV[0]

loginLocation = []

print 'wait... '

File.open(getFile, 'r') do |file|
  file.each do |fileLogins|
    fakeUser = 0
    endpoint = "/v2/locations/?user_id=#{fileLogins}&filter[active]=true"
    getInfo = token.get(endpoint) rescue fakeUser = 1

    if fakeUser == 0
      if getInfo.parsed.empty?
        loginLocation << [fileLogins.chomp, 'UNAVAILABLE']
      else
        parsedInfo = getInfo.parsed[0]

        userLogin = parsedInfo['user']['login']
        machineNum = parsedInfo['host']

        loginLocation << [userLogin, machineNum]
      end
    else
      loginLocation << [fileLogins.chomp, 'FAKE USER']
    end
  end
  puts "\n"
end

if loginLocation.empty?
  print 'Nothing in the file.'.ljust(25)
else
  display_location(loginLocation)
end