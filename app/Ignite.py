class flame:
  def __init__(self, *args, **kwargs): #contructor
    import logging
    self.ignite_logger = logging.getLogger('Ignite')
    self.ignite_logger.warn("Ignite Started")
    print("Ignited")
    #code
  def test(self):
    return "Operational"
  def start_pcxy(self):
    import temp
  def get_blocklist(self):
    return ["www.discord.com","discord.com"]
  def check(self,host):
    print(host)
    self.ignite_logger.warn(str(host))
    block = self.get_blocklist()
    for items in block:
      if items == host:
        print("Blocked")
        return False
    return True
