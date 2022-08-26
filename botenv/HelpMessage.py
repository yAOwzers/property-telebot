helpMessage = ""

def sendHelp():
  greet = "Welcome to PropertyBot! I envision sharing with you the top 5 properties from various property souces :) We only have hardcoded params atm :("
  currentSources = "Current, we have the following sources:\n1. 99.co"
  functions = "To accesss the source, you can use the following handlers\n1. /get_99co"

  helpMessage = greet + "\n\n" + currentSources + "\n\n" + functions
  
  return helpMessage