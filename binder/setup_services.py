def setup_pythonservice():
  return {
    'command': ['wrattler-python-service']
  }

def setup_datastore():
  return {
    'command': ['wrattler-data-store']
  }


def setup_rservice():
  return {
    'command': ['Rscript','wrattler/server/R/app.R']
  }


def setup_client():
  return {
    'command': ['http-server','wrattler/client/public','-c-1','--cors']
  }
