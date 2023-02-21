# Gcore-IP-range-finder
This is a tool that extracts all IPv4 and IPv6 from official JSON file

This tool is not really useful in general but most of users in countries such as Iran and China or any country dealing with censorship needs all IP ranges for any kind of CDN, this is due to fact that poeple use CDN to hide thier server IP.

Since governments could not ban all of CDN IPs, they deploy noises and prevent most used ones from working properly, Cloudflare luckily shares its IPv4 and IPv6 list while CDNs such as Amazon or Gcore share their IP as JSON data block, this tool helps you exctract all of these IPs and use proper tools to check them, I suggest [This tool](https://github.com/hoseinnikkhah/better-cloudflare-ip-english) in order to check all IPs at once, simply put text files in same directory and run the tool, it saves 10 most fast IPs for you in an csv file. Pick the one that suits you and enjoy.
