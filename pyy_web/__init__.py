from httpmessage import *

def resolve(urls, request, response):
  for regex, pageclass in urls:
    match = re.match(regex, request.uri)
    if match:
      request.get.update(match.groupdict())
      return pageclass(request, response)
  raise ValueError("URI did not resolve to a class.")
